from security_analysis import validate_message
def test_whitespace_only_message_is_rejected():
    valid,reason=validate_message("  \n  ")
    assert valid is False and "empty" in reason.lower()