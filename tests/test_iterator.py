from merge_sorted_files.iterator import MergeSortedIterators


def test_concat():
    it1 = range(10)
    it2 = range(10, 30)
    it3 = range(30, 35)

    result = list(MergeSortedIterators([it3, it1, it2]))
    assert result == list(range(35))


def test_one_empty_iterable():
    it1 = []
    it2 = [2, 56, 101]
    it3 = [3, 60]

    result = list(MergeSortedIterators([it1, it2, it3]))
    assert result == [2, 3, 56, 60, 101]


def test_all_empty_iterables():
    it1 = range(1, -9000)
    it2 = range(666, 101)

    result = list(MergeSortedIterators([it1, it2]))
    assert not result
