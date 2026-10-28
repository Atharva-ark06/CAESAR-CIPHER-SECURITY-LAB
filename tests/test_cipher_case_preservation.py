from cipher_engine import CaesarCipher

def test_upper_and_lower_case_are_preserved():
    assert CaesarCipher(1).encrypt("Az") == "Ba"