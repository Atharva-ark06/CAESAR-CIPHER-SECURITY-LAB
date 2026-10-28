from cipher_engine import CaesarCipher

def test_spaces_punctuation_and_digits_are_preserved():
    assert CaesarCipher(3).encrypt("Hi, Bob! 123") == "Kl, Ere! 123"