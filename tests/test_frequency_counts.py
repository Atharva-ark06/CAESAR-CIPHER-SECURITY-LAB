from cryptanalysis import frequency_analysis
def test_counts_are_case_insensitive():
    result=frequency_analysis("AaBbA")
    assert result["total_letters"]==5
    assert result["frequencies"]["A"]["count"]==3
    assert result["frequencies"]["B"]["count"]==2