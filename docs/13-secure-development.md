# Secure development checklist

- Validate input at the boundary.
- Use parameterized SQL queries for user-controlled values.
- Avoid storing plaintext unless required for the demonstration.
- Keep secrets and local state out of version control.
- Make security claims proportional to evidence.
- Add regression tests when fixing a bug.
- Review dependency changes and CI output before merging.
- Keep educational attacks limited to the toy cipher implemented here.