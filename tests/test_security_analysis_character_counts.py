from security_analysis import analyze_message
def test_analysis_counts_message_characters():
    report=analyze_message("Aa! b",1)
    assert report["message_length"]==5
    assert report["alphabetic_characters"]==3 and report["unique_letters"]==2