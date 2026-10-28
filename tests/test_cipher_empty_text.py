from cipher_engine import CaesarCipher
def test_empty_text_round_trip():
    cipher=CaesarCipher(17)
    assert cipher.decrypt(cipher.encrypt(""))==""