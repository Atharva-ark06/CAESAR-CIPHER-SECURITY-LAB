# Testing strategy

Tests should cover ordinary cases, boundaries, invalid inputs, and round-trip properties. The cipher engine is deterministic, so known-answer examples and property-style loops can verify behavior without network access.

Keep tests independent: use temporary directories for SQLite, avoid shared mutable state, and assert observable behavior. Run `python -m pytest` from the repository root before merging changes. The workflow added in this branch runs the same test command on supported Python versions.