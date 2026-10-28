from cipher_engine import CaesarCipher

def test_known_encryption_answer():
    assert CaesarCipher(3).encrypt("HELLO") == "KHOOR"

def test_known_decryption_answer():
    assert CaesarCipher(3).decrypt("KHOOR") == "HELLO"