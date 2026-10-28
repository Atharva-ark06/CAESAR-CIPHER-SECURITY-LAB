# Key space and brute force

A Caesar Cipher has 26 distinct shifts for the English alphabet. An attacker can try every shift and inspect the resulting candidates; the search is tiny and does not require specialized hardware.

The lab's brute-force output is a list of candidates, not an automatic guarantee that the correct plaintext has been identified. Natural-language scoring may help rank candidates, but scoring heuristics can fail on short, unusual, or multilingual text.