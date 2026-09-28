class CaesarCipher:
    """
    Caesar Cipher implementation.

    Supports:
    - Uppercase letters
    - Lowercase letters
    - Spaces and punctuation
    """

    def __init__(self, key: int):
        self.key = key % 26

    def _shift_character(self, char: str, shift: int) -> str:
        if char.isupper():
            return chr(
                (ord(char) - ord("A") + shift) % 26 + ord("A")
            )

        if char.islower():
            return chr(
                (ord(char) - ord("a") + shift) % 26 + ord("a")
            )

        return char

    def transform(self, text: str, shift: int) -> str:
        return "".join(
            self._shift_character(char, shift)
            for char in text
        )

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