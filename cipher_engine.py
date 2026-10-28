class CaesarCipher:
    """
    Caesar Cipher implementation for the ASCII English alphabet.

    Only A-Z and a-z are shifted. Unicode letters, spaces, digits,
    and punctuation are preserved unchanged.
    """

    def __init__(self, key: int):
        self.key = key % 26

    def _shift_character(self, char: str, shift: int) -> str:
        if "A" <= char <= "Z":
            return chr((ord(char) - ord("A") + shift) % 26 + ord("A"))

        if "a" <= char <= "z":
            return chr((ord(char) - ord("a") + shift) % 26 + ord("a"))

        return char

    def transform(self, text: str, shift: int) -> str:
        return "".join(self._shift_character(char, shift) for char in text)

    def encrypt(self, plaintext: str) -> str:
        return self.transform(plaintext, self.key)

    def decrypt(self, ciphertext: str) -> str:
        return self.transform(ciphertext, -self.key)

    def get_mapping(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return {
            letter: alphabet[(index + self.key) % 26]
            for index, letter in enumerate(alphabet)
        }
