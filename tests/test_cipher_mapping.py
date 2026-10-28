from cipher_engine import CaesarCipher
def test_mapping_has_all_letters_and_wraps():
    mapping=CaesarCipher(3).get_mapping()
    assert len(mapping)==26 and mapping["A"]=="D" and mapping["Z"]=="C"