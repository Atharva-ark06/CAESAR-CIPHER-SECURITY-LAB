# Audit-log privacy notes

The SQLite history is intended for local classroom demonstrations. Operation rows currently include the message and result, which can contain plaintext. Treat the database as sensitive even when the cipher itself is weak.

For real applications, prefer recording event metadata instead of raw content, define retention and deletion policies, restrict filesystem access, and document who can view logs. Never paste confidential data into this educational lab.