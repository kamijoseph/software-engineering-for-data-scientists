from chap_7 import fit_trendline
from chap_7 import weighted_mean

# test for the weighted sum function
def test_weighted_mean():

    list_a = [1, 2, 4]
    list_b = [1, 2, 4]

    result = weighted_mean(list_a, list_b)
    assert result == 3

# test for an unexpected input
def test_weighted_means():
    
    result = weighted_mean([1, 2, 4], [1, 2, 4])
    assert result == 3

    empty_list_result = weighted_mean([], [])
    assert not empty_list_result

# test for the fit trendline function
def test_fit_trendline():

    data = [1, 2, 3]
    timestamps = [2020, 2021, 2022]

    slope, r_squared = fit_trendline(timestamps, data)

    assert slope == 1
    assert r_squared == 1