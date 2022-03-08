
from unittest import expectedFailure
from array_binary_search.binarySearch import BinarySearch
def test_Bianry():
    actual = BinarySearch([1,2,3,4,5],5)
    expected = 4
    assert actual == expected

