"""Show why key values repeat modulo the alphabet size."""
from cipher_engine import CaesarCipher
if __name__=="__main__":
    for sample in ("HELLO","ATTACK AT DAWN"):
        assert CaesarCipher(3).encrypt(sample)==CaesarCipher(29).encrypt(sample)
    print("Keys 3 and 29 produce the same transformation.")