#!/usr/bin/env python3
"""Publish canonical agent rules and shared documentation to configured projects."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


SOURCE_ROOT = Path(__file__).resolve().parent
WORKSPACE_ROOT = SOURCE_ROOT.parent
if WORKSPACE_ROOT.name == "projects":
	# Use this workspace when project repositories are siblings of the rules repo.
	DEFAULT_PROJECTS_ROOT = WORKSPACE_ROOT
else:
	# Support workspaces that contain project repositories in a projects folder.
	DEFAULT_PROJECTS_ROOT = WORKSPACE_ROOT / "projects"
WORKSPACE_PROJECTS_ROOT = Path(os.environ.get("WORKSPACE_PROJECTS_ROOT", DEFAULT_PROJECTS_ROOT))
TARGETS_FILE = SOURCE_ROOT / "targets.tsv"
TASK_DOCS_README_SOURCE = SOURCE_ROOT / "templates" / "task-docs-readme.md"
AGENT_GENERATOR_SOURCE = SOURCE_ROOT / "templates" / "gen-agent-rules.py"
SPECS_README_SOURCE = SOURCE_ROOT / "shared" / "specs" / "README.md"
START_MARKER = "<!-- BEGIN SHARED TASK DOC RULES -->"
END_MARKER = "<!-- END SHARED TASK DOC RULES -->"


def validate_sources() -> None:
	"""Check the canonical inputs before modifying any targets."""
	sources = (
		(SOURCE_ROOT / "shared" / "base.md", "shared rules or targets.tsv are missing"),
		(TARGETS_FILE, "source rules or targets.tsv are missing"),
		(TASK_DOCS_README_SOURCE, "task docs README source is missing"),
		(AGENT_GENERATOR_SOURCE, "agent generator template is missing"),
		(SPECS_README_SOURCE, "spec docs README source is missing"),
	)
	# Report the first missing input and stop before any target is changed.
	for path, message in sources:
		if not path.is_file():
			print(f"---> {message}: {path}", file=sys.stderr)
			raise SystemExit(2)


def read_targets() -> list[tuple[str, str]]:
	"""Load target and framework pairs from the pipe-delimited target map."""
	targets: list[tuple[str, str]] = []
	with TARGETS_FILE.open(encoding="utf-8") as target_file:
		# Ignore blank and comment lines in the target map.
		for line_number, raw_line in enumerate(target_file, start=1):
			line = raw_line.strip()
			if not line or line.startswith("#"):
				continue
			fields = [field.strip() for field in line.split("|")]
			if len(fields) != 2 or not all(fields):
				print(f"---> invalid target mapping at {TARGETS_FILE}:{line_number}", file=sys.stderr)
				raise SystemExit(2)
			targets.append((fields[0], fields[1]))
	return targets


def sync_task_docs_readme(target_dir: Path) -> None:
	"""Replace the managed task naming section and preserve local index content."""
	readme = target_dir / "docs" / "README.md"
	readme.parent.mkdir(parents=True, exist_ok=True)
	if not readme.is_file():
		# Create the documentation index when the target does not have one.
		readme.write_text("# Documentation\n", encoding="utf-8")

	content = readme.read_text(encoding="utf-8")
	lines = content.splitlines()
	start_count = sum(line == START_MARKER for line in lines)
	end_count = sum(line == END_MARKER for line in lines)
	if start_count != end_count:
		# Preserve local content when the managed block markers are malformed.
		raise ValueError(f"shared task docs markers are incomplete: {readme}")

	kept_lines: list[str] = []
	inside_block = False
	# Remove all prior managed blocks while keeping lines outside them.
	for line in lines:
		if line == START_MARKER:
			inside_block = True
			continue
		if line == END_MARKER:
			inside_block = False
			continue
		if not inside_block:
			kept_lines.append(line)
	while kept_lines and not kept_lines[-1]:
		kept_lines.pop()

	shared_content = TASK_DOCS_README_SOURCE.read_text(encoding="utf-8").rstrip("\r\n")
	updated = "\n".join(kept_lines)
	updated += f"\n\n{START_MARKER}\n\n{shared_content}\n{END_MARKER}\n"
	temp_path: Path | None = None
	try:
		# Replace the index atomically after the complete managed section is ready.
		with tempfile.NamedTemporaryFile(
			mode="w",
			encoding="utf-8",
			newline="\n",
			dir=readme.parent,
			delete=False,
		) as temp_file:
			temp_path = Path(temp_file.name)
			temp_file.write(updated)
		os.replace(temp_path, readme)
	finally:
		# Remove the temporary file if writing or replacement failed.
		if temp_path is not None and temp_path.exists():
			temp_path.unlink()


def process_target(relative_target: str, framework_name: str) -> None:
	"""Publish the shared rule files and documentation for one target."""
	target_dir = WORKSPACE_PROJECTS_ROOT / relative_target
	framework_file = SOURCE_ROOT / "shared" / "frameworks" / f"{framework_name}.md"
	if not target_dir.is_dir():
		# Report configured targets that are absent from this workspace.
		raise FileNotFoundError(f"target is missing: {relative_target}")
	if not framework_file.is_file():
		# Report framework names that have no canonical source file.
		raise FileNotFoundError(f"framework is missing: {framework_name}")

	rules_dir = target_dir / ".agent-rules"
	scripts_dir = target_dir / "scripts"
	rules_dir.mkdir(parents=True, exist_ok=True)
	scripts_dir.mkdir(parents=True, exist_ok=True)
	(target_dir / "docs" / "specs").mkdir(parents=True, exist_ok=True)
	# Copy canonical shared rules, documentation, and the local generator.
	shutil.copyfile(SOURCE_ROOT / "shared" / "base.md", rules_dir / "base.md")
	shutil.copyfile(framework_file, rules_dir / "framework.md")
	generator = scripts_dir / "gen-agent-rules.py"
	shutil.copyfile(AGENT_GENERATOR_SOURCE, generator)
	generator.chmod(generator.stat().st_mode | 0o111)
	sync_task_docs_readme(target_dir)
	shutil.copyfile(SPECS_README_SOURCE, target_dir / "docs" / "specs" / "README.md")
	print(f"---> updated shared rules for {relative_target}")
	# Regenerate the target's agent files after all source rules are current.
	subprocess.run([sys.executable, str(generator)], cwd=target_dir, check=True)


def main() -> int:
	"""Validate canonical inputs and publish them to every configured target."""
	validate_sources()
	targets = read_targets()
	failed = False
	# Continue publishing other targets after reporting an individual failure.
	for relative_target, framework_name in targets:
		try:
			process_target(relative_target, framework_name)
		except (OSError, ValueError, subprocess.CalledProcessError) as error:
			print(f"---> {error}", file=sys.stderr)
			failed = True
	return 1 if failed else 0


if __name__ == "__main__":
	# Return the sync result as the process exit status.
	raise SystemExit(main())
