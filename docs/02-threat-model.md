# Lightweight threat model

## Assets
- User-entered plaintext and ciphertext
- Selected cipher key and operation history
- Application availability and integrity

## Trust boundaries
The Streamlit browser interface sends input to Python code. The Python process may write operation history to a local SQLite database. Local users with filesystem access may be able to inspect that database.

## Risks and mitigations
- **Plaintext persisted in history:** avoid real secrets; minimize stored content and disclose logging behavior.
- **Malformed input:** validate type, empty values, and length at the application boundary.
- **False sense of security:** label Caesar Cipher as educational and cryptographically weak.
- **Dependency risk:** pin or constrain dependencies and review updates.

This is an educational threat model, not a formal security assessment.