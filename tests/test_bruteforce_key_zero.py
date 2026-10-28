from cryptanalysis import brute_force_decrypt
def test_key_zero_candidate_preserves_ciphertext():
    assert {"key":0,"plaintext":"HELLO"} in brute_force_decrypt("HELLO")