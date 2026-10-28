from cipher_engine import CaesarCipher
def test_round_trip_for_all_26_keys():
    sample="Attack at dawn! 123"
    for key in range(26):
        cipher=CaesarCipher(key)
        assert cipher.decrypt(cipher.encrypt(sample))==sample