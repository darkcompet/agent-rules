# Agent rules

This repository contains shared agent rules and `sync.py` for publishing them to the targets listed in `local/targets.tsv`. Keep it beside the target projects.

## Sync shared rules

Run from this repository:

```sh
python3 sync.py
```

> On Windows: `py -3 sync.py`.
>
> The script copies shared and framework rules to `.agent-rules/`, installs the local generator, updates shared documentation, and regenerates the agent files in each target. Set `WORKSPACE_PROJECTS_ROOT` to use a different projects root.

## Generate agent files

Run from a target project:

```sh
./scripts/gen-agent-rules.py
```

> `sync.py` copies the generator into each target's `scripts/` directory. It generates `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` from `.agent-rules/base.md`, `.agent-rules/framework.md`, and the optional `.agent-rules/project.md`.
