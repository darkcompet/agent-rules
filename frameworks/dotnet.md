## .NET rules

- Follow `.editorconfig`, nullable annotations, and existing project targets.
- Keep dependencies directional and avoid architecture cycles.
- Keep domain rules independent from HTTP and persistence.
- Keep HTTP adapters thin and application workflows explicit.
- Use async APIs and propagate the available cancellation token.
- Generate migrations with repository scripts.
- Never hand-edit generated output, migrations, or snapshots.
- Write concise English comments and XML documentation.
- Comment non-obvious decisions, constraints, ordering, and invariants.
- Omit comments that only narrate obvious code.
- Run targeted tests before broad validation.
