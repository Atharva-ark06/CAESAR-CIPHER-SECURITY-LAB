from cryptanalysis import frequency_analysis
def test_simple_frequency_percentages():
    result=frequency_analysis("AABB")["frequencies"]
    assert result["A"]["percentage"]==50.0 and result["B"]["percentage"]==50.0