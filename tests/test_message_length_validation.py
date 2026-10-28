from security_analysis import validate_message
def test_message_length_boundary():
    assert validate_message("x"*1000)[0] is True
    assert validate_message("x"*1001)[0] is False