## Worker rules

- Keep process startup and composition in the host project.
- Keep orchestration in application services and adapters in infrastructure.
- Propagate cancellation through I/O and background work.
- Bound concurrency and clean temporary workspaces.
- Do not log credentials, tokens, or private URLs.
- Test public protocol behavior and failure handling.
