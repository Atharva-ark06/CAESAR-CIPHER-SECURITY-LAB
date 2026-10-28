from cryptanalysis import verify_round_trip
def test_round_trip_reports_normalized_key():
    result=verify_round_trip("ABC",29)
    assert result["key"]==3 and result["passed"] is True