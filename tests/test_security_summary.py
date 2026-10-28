from security_analysis import analyze_message
def test_report_explains_tiny_key_space():
    report=analyze_message("abc",29)
    assert report["key"]==3 and report["key_space"]==26
    assert report["brute_force_attempts"]==26 and report["security_level"]=="Educational / Weak"