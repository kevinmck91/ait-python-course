from assignment.utilities import stats_utils

def test_get_mean() :
    assert stats_utils.get_mean([1]) == 1
    assert stats_utils.get_mean([10]) == 10
    assert stats_utils.get_mean([0]) == 0
    assert stats_utils.get_mean([]) == "null"
    assert stats_utils.get_mean([9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]) == 16.75
    assert stats_utils.get_mean([-25, -24, -22, -18, -15, -13, -13, -12, -6, 9, 10, 13, 15, 16, 23, 24]) == -2.375

