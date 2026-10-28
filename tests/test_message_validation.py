from security_analysis import validate_message
def test_valid_and_non_string_messages():
    assert validate_message("hello")[0] is True
    assert validate_message(None)[0] is False