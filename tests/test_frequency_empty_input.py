from cryptanalysis import frequency_analysis
def test_no_letters_returns_empty_summary():
    result=frequency_analysis("123 !!!")
    assert result["total_letters"]==0 and result["frequencies"]=={} and result["most_frequent"] is None