from cryptanalysis import frequency_analysis
def test_frequency_counts_add_up_to_total():
    report=frequency_analysis("Security Lab 2026")
    assert sum(item["count"] for item in report["frequencies"].values())==report["total_letters"]