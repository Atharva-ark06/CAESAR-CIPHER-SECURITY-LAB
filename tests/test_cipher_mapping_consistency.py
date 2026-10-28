from cipher_engine import CaesarCipher
def test_mapping_agrees_with_encrypt_method():
    cipher=CaesarCipher(11)
    for source,target in cipher.get_mapping().items():
        assert cipher.encrypt(source)==target