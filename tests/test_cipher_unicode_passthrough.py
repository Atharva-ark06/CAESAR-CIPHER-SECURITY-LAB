from cipher_engine import CaesarCipher
def test_non_ascii_text_is_preserved_by_ascii_shift_logic():
    result=CaesarCipher(4).encrypt("café — 東京")
    assert " — 東京" in result