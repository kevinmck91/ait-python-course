# A00279670

from python_assignment_part_3.utilities import stats_utils

def test_get_mean():
    assert stats_utils.get_mean([1]) == 1
    assert stats_utils.get_mean([10]) == 10
    assert stats_utils.get_mean([0]) == 0
    assert stats_utils.get_mean([]) == "null"
    assert stats_utils.get_mean([9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]) == 16.75
    assert stats_utils.get_mean([-25, -24, -22, -18, -15, -13, -13, -12, -6, 9, 10, 13, 15, 16, 23, 24]) == -2.375

def test_get_median():
    assert stats_utils.get_median([9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]) == 15.5
    assert stats_utils.get_median([-25, -24, -22, -18, -15, -13, -13, -12, -6, 9, 10, 13, 15, 16, 23, 24]) == -9
    assert stats_utils.get_median([1]) == 1
    assert stats_utils.get_median([10]) == 10
    assert stats_utils.get_median([0]) == 0
    assert stats_utils.get_median([]) == "null"

def test_get_mode():
    assert stats_utils.get_mode([9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]) == 13
    assert stats_utils.get_mode([-25, -24, -22, -18, -15, -13, -13, -12, -6, 9, 10, 13, 15, 16, 23, 24]) == -13
    assert stats_utils.get_mode([1]) == 1
    assert stats_utils.get_mode([10]) == 10
    assert stats_utils.get_mode([0]) == 0
    assert stats_utils.get_mode([]) == "null"

def test_get_standard_deviation():
    assert round(stats_utils.get_standard_deviation([9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]),0) == 5
    assert round(stats_utils.get_standard_deviation([-25, -24, -22, -18, -15, -13, -13, -12, -6, 9, 10, 13, 15, 16, 23, 24])) == 17
    assert round(stats_utils.get_standard_deviation([1, 2, 3, 4, 5, 6, 7, 8, 9])) == 2
    assert stats_utils.get_mode([1]) == 1
    assert stats_utils.get_mode([10]) == 10
    assert stats_utils.get_mode([0]) == 0
    assert stats_utils.get_mode([]) == "null"

def test_get_correlation():

    list_1 = [9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]
    list_2 = [-25, -24, -22, -18, -15, -13, -13, -12, -6, 9, 10, 13, 15, 16, 23, 24]
    list_3 = [-5, -4, 22, -8, 15, -3, -3, 12, -8, 9, 10, 3, 15, 1, 23, 24]

    assert round(stats_utils.get_correlation(list_1 , list_2), 4) == 0.9579
    assert round(stats_utils.get_correlation(list_1 , list_3), 4) == 0.4752
    assert round(stats_utils.get_correlation(list_2 , list_3), 4) == 0.4904
