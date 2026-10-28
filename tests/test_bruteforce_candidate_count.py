from cryptanalysis import brute_force_decrypt
def test_brute_force_returns_26_candidates():
    assert len(brute_force_decrypt("KHOOR"))==26