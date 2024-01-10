"""Typings for List"""
from typing import List


def binary_search(arr: List[int], q: int) -> int:
    """
    Performs a binary search of q against SORTED list
    """
    left = 0
    right = len(arr) - 1

    if right == 0:
        return False

    while left <= right:
        _midp = (left + right) // 2

        # if Q is present, return the index
        if arr[_midp] == q:
            return _midp

        if arr[_midp] < q:
            # ignore left half
            left = _midp + 1
        else:
            # ignore right half
            right = _midp - 1

    return -1


if __name__ == "__main__":
    t = [1, 2, 3, 4, 5, 6]
    query = 6
    print(binary_search(t, query))
