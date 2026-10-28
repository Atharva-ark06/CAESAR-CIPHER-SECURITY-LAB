# Manual QA checklist

- [ ] Encrypt HELLO with key 3 and confirm KHOOR.
- [ ] Decrypt KHOOR with key 3 and confirm HELLO.
- [ ] Check uppercase, lowercase, spaces, punctuation, and digits.
- [ ] Try keys 0, 25, 26, negative values, and values above 26.
- [ ] Confirm brute force returns 26 candidates.
- [ ] Run frequency analysis on letters and on punctuation-only input.
- [ ] Reject blank input and input above the documented length limit.
- [ ] Inspect audit-history behavior with synthetic, non-sensitive messages.
- [ ] Verify the interface clearly states that the cipher is insecure.