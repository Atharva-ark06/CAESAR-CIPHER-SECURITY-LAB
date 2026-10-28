from cryptanalysis import brute_force_decrypt
def test_candidates_are_returned_in_key_order():
    assert [row["key"] for row in brute_force_decrypt("ABC")]==list(range(26))