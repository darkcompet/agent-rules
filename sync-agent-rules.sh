#!/usr/bin/env bash
set -euo pipefail

SOURCE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="$(cd "$SOURCE_ROOT/.." && pwd)"
if [[ "$(basename "$WORKSPACE_ROOT")" == "projects" ]]; then
	DEFAULT_PROJECTS_ROOT="$WORKSPACE_ROOT"
else
	DEFAULT_PROJECTS_ROOT="$WORKSPACE_ROOT/projects"
fi
WORKSPACE_PROJECTS_ROOT="${WORKSPACE_PROJECTS_ROOT:-$DEFAULT_PROJECTS_ROOT}"
TARGETS_FILE="$SOURCE_ROOT/targets.tsv"
LOCAL_SYNC_SOURCE="$SOURCE_ROOT/templates/gen-agent-rules.sh"

if [[ ! -f "$SOURCE_ROOT/base.md" || ! -f "$TARGETS_FILE" || ! -f "$LOCAL_SYNC_SOURCE" ]]; then
	echo "Source rules or targets.tsv are missing under: $SOURCE_ROOT" >&2
	exit 2
fi

process_target() {
	local relative_target="$1"
	local framework_name="$2"
	local generator_path="${3:-scripts/gen-agent-rules.sh}"
	local target_dir="$WORKSPACE_PROJECTS_ROOT/$relative_target"
	local target_rules="$target_dir/.agent-rules"
	local target_base="$target_rules/base.md"
	local target_framework="$target_rules/framework.md"
	local target_generator="$target_dir/$generator_path"
	local framework_file="$SOURCE_ROOT/frameworks/$framework_name.md"

	if [[ ! -d "$target_dir" ]]; then
		echo "MISSING  $relative_target"
		return 1
	fi
	if [[ ! -f "$framework_file" ]]; then
		echo "MISSING  framework $framework_name"
		return 1
	fi

	mkdir -p "$target_rules"
	mkdir -p "$(dirname "$target_generator")"
	cp "$SOURCE_ROOT/base.md" "$target_base"
	cp "$framework_file" "$target_framework"
	cp "$LOCAL_SYNC_SOURCE" "$target_generator"
	chmod +x "$target_generator"
	echo "SYNCED   $relative_target"
}

failed=0
while IFS='|' read -r relative_target framework_name generator_path; do
	[[ -z "$relative_target" || "$relative_target" == \#* ]] && continue
	if ! process_target "$relative_target" "$framework_name" "$generator_path"; then
		failed=1
	fi
done < "$TARGETS_FILE"

exit "$failed"

