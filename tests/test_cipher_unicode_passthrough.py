from cipher_engine import CaesarCipher

def test_non_ascii_letters_and_symbols_are_preserved():
    assert CaesarCipher(4).encrypt("café — 東京") == "gejé — 東京"