from cryptanalysis import verify_round_trip
def test_round_trip_recovers_original():
    result=verify_round_trip("Meet at 9!",8)
    assert result["passed"] is True and result["decrypted"]=="Meet at 9!"