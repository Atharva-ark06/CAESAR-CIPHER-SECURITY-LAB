from security_analysis import normalize_key
def test_key_normalization_boundaries():
    assert normalize_key(26)==0 and normalize_key(27)==1 and normalize_key(-1)==25