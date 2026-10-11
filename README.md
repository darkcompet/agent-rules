# Agent rules source repository

This directory is the canonical source for shared agent rules.

Keep this repository beside the project repositories.

The central sync script publishes shared sources to each target repository.
Each target repository owns its project-specific rules.
Each target also receives a self-contained `gen-agent-rules.sh`.

## Source files

- `base.md` contains rules shared by every repository.
- `frameworks/` contains stack-specific rules.
- `targets.tsv` maps targets to framework rules and generator paths.
- `templates/gen-agent-rules.sh` is the local project generator script.
- `.agent-rules/` contains generated copies inside each target repository.

Keep target-specific rules in `<target>/.agent-rules/project.md`.
`AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` are local generated output.
Do not edit them manually.

AI agents should change `project.md` for project-only rules.
They should change this repository for shared or framework rules.
Project developers can regenerate files without this repository.

## Sync steps

Run from this directory.

### Publish shared rules

```bash
./sync-agent-rules.sh
```

Expected: every target receives updated `base.md`, `framework.md`, and its generator script.

The central script never overwrites `project.md` or final agent files.
Run the local script inside each project to regenerate final agent files.

### Sync from a project repository

Run inside the project repository:

```bash
./scripts/gen-agent-rules.sh
```

Expected: `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` match `.agent-rules/`.

## Safety

The central script overwrites shared copies and local sync scripts.
It never overwrites `.agent-rules/project.md` or final agent files.
The local script overwrites final agent files directly.
Use Git to review or restore generated changes.
