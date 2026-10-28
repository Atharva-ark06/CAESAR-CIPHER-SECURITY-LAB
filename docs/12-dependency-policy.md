# Dependency policy

Keep runtime dependencies minimal. Add a new package only when it solves a clear need, and document why it is required. Development-only tools should be listed separately from runtime packages.

Review dependency release notes and compatibility before upgrading. Do not commit virtual environments, caches, local databases, credentials, or generated reports. The CI workflow should install dependencies in a clean environment to expose missing declarations.