# Agent rules

> This repository keeps shared AI agent rules and a sync script.

Configure it once to point at the project repositories you own, then run `sync.py` whenever you want to publish the shared rules to them.

## 1. Choose your folder layout

> The folder names below are placeholders for a possible workspace layout:

```text
<your-workspace>/
├── <agent-rules-repo>/
└── <your-projects-root>/
    ├── <your-api-repo>/
    └── <your-web-app-repo>/
```

Choose folder names that suit your workspace.

> The script infers a default projects root from the location of this repository. Setting the variable lets you use any folder name and layout.

For the example layout above, set `WORKSPACE_PROJECTS_ROOT` to the full path of `<your-projects-root>`. If you use the inferred default root, skip this setting. Target paths in `local/targets.tsv` are relative to the selected root. See [Setting the projects root](#setting-the-projects-root) for the OS-specific command.

Install Python 3.10 or newer. Check the version with `python3 --version` on macOS/Linux or `py -3 --version` in Windows PowerShell.

## 2. Configure your target projects

Run the setup commands from the `agent-rules` repository directory. Create your private target list from the template. It contains commented examples only, so it does not configure any targets until you uncomment or replace the rows.

macOS/Linux:

```sh
mkdir -p local
cp templates/targets.template.tsv local/targets.tsv
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force local | Out-Null
Copy-Item templates/targets.template.tsv local/targets.tsv
```

Run the copy command only when creating the file. If `local/targets.tsv` already exists, edit it directly so you do not overwrite your target list.

Edit `local/targets.tsv`. Keep one target per line in this format:

```text
relative/path/from/your-projects-root|framework
```

For example:

```text
my-api|dotnet
my-web-app|react
```

Uncomment and replace the example rows with your own project paths. Each path must point to an existing project directory beneath the configured projects root, or `sync.py` will report that target as missing. Use `/` between path segments on every OS, for example `group/my-api|dotnet`. Do not include the `agent-rules` directory itself or use paths starting with `..`.

Choose a framework name that matches a file under `shared/frameworks/` (omit `.md`):

| Framework value | Rules file |
| --- | --- |
| `common` | `shared/frameworks/common.md` |
| `dotnet` | `shared/frameworks/dotnet.md` |
| `ops-runbook` | `shared/frameworks/ops-runbook.md` |
| `python` | `shared/frameworks/python.md` |
| `react` | `shared/frameworks/react.md` |
| `worker` | `shared/frameworks/worker.md` |

> `local/targets.tsv` is intentionally git-ignored because it contains your personal project list and is not included when you clone this repository.

Keep the file on your machine.

### Example: PlayTogether Auto on Windows

> The PlayTogether Auto project described in the review document uses Python 3.12, Tkinter, OpenCV, NumPy, ADB, and PyInstaller.

On the friend's Windows machine, set the projects root to the directory containing `PlayTogetherAuto`, then add this row to `local/targets.tsv`:

```text
PlayTogetherAuto|python
```

> The target path is `C:\Users\Admin\Minh\PlayTogetherAuto`.

Set the projects root to its parent directory:

```powershell
$env:WORKSPACE_PROJECTS_ROOT = "C:\Users\Admin\Minh"
```

Keep app-specific requirements—such as farming restrictions, forbidden game actions, unknown-screen handling, and the `--no-run` requirement—in that project's `.agent-rules/project.md`. The `python` framework contains reusable Python guidance and does not replace the app's own rules.

## 3. Sync the rules

Run this from the `agent-rules` directory:

Before the first sync, move any project-specific instructions from existing `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.agent-rules/base.md`, or `.agent-rules/framework.md` files into `.agent-rules/project.md`. The sync regenerates those files. It also replaces `docs/specs/README.md`; the managed section of `docs/README.md` is updated while content outside that section is kept.

```sh
python3 sync.py
```

On Windows, run:

```powershell
py -3 sync.py
```

> For each configured target, the script copies the shared and selected framework rules into `.agent-rules/`, installs `scripts/gen-agent-rules.py`, updates the managed shared section in `docs/README.md`, copies the shared spec index to `docs/specs/README.md`, and regenerates `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md`.

> The script publishes rules to project folders already present on your machine. It does not clone, pull, or otherwise update the project repositories themselves.

Review the printed target list and any errors after each run.

Check that canonical copies, shared documentation, and all three generated
entrypoints are current without changing any files:

```sh
python3 sync.py --check
```

Use `py -3 sync.py --check` on Windows. A nonzero exit code means a target is
missing, stale, or blocked by a nonempty root `AGENTS.override.md`. Sync does not
remove overrides: merge any rules you need into `.agent-rules/project.md`, then
remove the override yourself. Codex selects the override instead of `AGENTS.md`
in the same directory; describing it as an extension does not merge the files.

## Updating project-specific rules

In a target project, put project-only instructions in `.agent-rules/project.md`. Then regenerate that project's agent files with:

```sh
./scripts/gen-agent-rules.py
```

On Windows, use:

```powershell
py -3 scripts/gen-agent-rules.py
```

Run `python3 scripts/gen-agent-rules.py --check` (Windows: `py -3`) to check the
three entrypoints against the project's local sources without writing files.
This local check does not compare shared copies with the central repository;
use `sync.py --check` there for that. Generated files label each source section.

After syncing, verify instruction loading in a fresh agent session at the
working directory you actually use. Check nested instructions and global
overrides too; the scripts only detect overrides at configured target roots.
Codex's default project instruction budget is 32 KiB across the discovered
chain. The generator warns when a single generated file reaches that size;
smaller files can still exceed the combined budget in nested projects. See the
[official discovery rules](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

Do not edit `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.agent-rules/base.md`, or `.agent-rules/framework.md` directly; the generator or next sync will replace those files.

## Setting the projects root

Set `WORKSPACE_PROJECTS_ROOT` to the directory containing your target project folders. Replace the example path below with its full path on your machine, then run `sync.py` in the same terminal session. The paths in `local/targets.tsv` remain relative to this directory.

macOS/Linux:

```sh
export WORKSPACE_PROJECTS_ROOT="/path/to/your-projects-root"
```

PowerShell:

```powershell
$env:WORKSPACE_PROJECTS_ROOT = "C:\path\to\your-projects-root"
```

## Contributing shared rules

Edit the canonical files in `shared/` or `templates/` in this repository, then run the sync command from step 3 to publish the changes to your configured targets. Commit changes to shared rules and templates as usual; do not commit `local/targets.tsv`.

Write rules with an explicit trigger, required action, exceptions, and behavior
when blocked. Distinguish mandatory constraints from preferences. Keep universal
constraints in `base.md`, stack rules in framework files, and project contracts
in project rules/specs. Put detailed procedures in referenced documents and state
when to read them. Use formatter, linter, tests, or CI for mechanically checkable
requirements; prose alone cannot guarantee compliance.

When changing behavior guidance, compare fresh agent sessions on representative
tasks: a typo fix, a bug covered by an approved requirement, a new behavior
without approval, invalid runtime input, and removal of newly unused source.
Inspect actual actions and diffs against the applicable rules, not just the
agent's statement that it read them. Automated sync checks verify delivery of
instructions, not model compliance.
