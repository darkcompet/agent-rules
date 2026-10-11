# Shared agent rules

These rules apply to AI agents working in this repository.

Produce small, correct, verified changes.

## Rule file ownership

- Treat `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` as generated output; never edit them directly.
- Put project-specific rules in `.agent-rules/project.md`.
- Put shared rules in the central `agent-rules` repository.
- Put framework rules in the matching central `frameworks/*.md` file.
- Treat `.agent-rules/base.md` and `framework.md` as generated copies.
- Run `./scripts/gen-agent-rules.sh` after changing rule sources.

## Before editing

- Read applicable instructions and the smallest relevant files.
- Inspect `git status` and the relevant diff before editing.
- Identify acceptance criteria and the narrowest verification command.
- Ask only when ambiguity changes behavior; otherwise make a reasonable assumption.
- Never invent missing repository facts.

## Keep changes narrow

- Implement the smallest change satisfying the request.
- Preserve existing patterns, workflows, and formatting.
- Do not add speculative features, abstractions, configuration, or dependencies.
- Do not refactor, rename, reformat, or clean unrelated code.
- Remove only unused code created by the change.

## Verify and report

- Run the narrowest relevant check after editing.
- Never weaken checks to obtain a pass.
- Report changed files, exact checks, and unresolved risks.
- Never claim an unrun check passed.
