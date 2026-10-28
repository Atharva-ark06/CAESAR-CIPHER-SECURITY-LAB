# Caesar Cipher mathematics

Map letters A–Z to integers 0–25. For key k, encryption is E(x) = (x + k) mod 26 and decryption is D(y) = (y - k) mod 26. Modulo arithmetic wraps Z after the alphabet ends.

For example, with k = 3, H (7) becomes K (10). Decryption subtracts 3 and recovers H. Keys differing by a multiple of 26 produce the same transformation, so normalize keys with k mod 26.

The transformation affects alphabetic characters only; spaces and punctuation are preserved by this implementation.