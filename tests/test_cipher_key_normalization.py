from cipher_engine import CaesarCipher

def test_key_multiple_of_alphabet_is_identity():
    assert CaesarCipher(26).encrypt("ABC xyz") == "ABC xyz"

def test_large_key_matches_normalized_key():
    assert CaesarCipher(55).encrypt("ATTACK") == CaesarCipher(3).encrypt("ATTACK")