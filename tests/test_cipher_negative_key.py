from cipher_engine import CaesarCipher

def test_negative_key_wraps_around():
    assert CaesarCipher(-1).encrypt("ABC") == "ZAB"