# Input validation

Validation should happen before expensive work or persistence. This project rejects non-string messages, blank messages, and messages longer than its configured limit.

Validation is not a substitute for output encoding, authorization, safe storage, or dependency management. If the application is expanded, validate keys and operation names at every external boundary and show concise, actionable error messages without exposing internal tracebacks to end users.