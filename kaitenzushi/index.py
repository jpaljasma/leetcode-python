from typing import List
from collections import deque
import unittest

"""
Passes 32/33 FB Kaitenzushi tests (time limit exceeded on the last one).
Interestingly enoguh, using deque is even slower, 31/33 passed.
I'll leave the deque usage coded in
"""


def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    ret = 0
    m = []
    for i in D:
        if i not in m[-K:]:
            ret += 1
            m.append(i)
    return ret


def getMaximumEatenDishCountDeque(N: int, D: List[int], K: int) -> int:
    queue = deque()
    ret = 0
    for i in D:
        if i not in queue:
            ret += 1
            queue.append(i)
        if len(queue) > K:
            queue.popleft()
    return ret


class TestKaitenzushi(unittest.TestCase):
    tests = [
        [6, [1, 2, 3, 3, 2, 1], 1, 5],
        [6, [1, 2, 3, 3, 2, 1], 2, 4],
        [7, [1, 2, 1, 2, 1, 2, 1], 2, 2],
    ]

    def test_maximum_eaten_dish_count(self):
        for test in self.tests:
            self.assertEqual(
                getMaximumEatenDishCount(test[0], test[1], test[2]), test[3]
            )

    def test_deque_vs_list(self):
        for test in self.tests:
            self.assertEqual(
                getMaximumEatenDishCount(test[0], test[1], test[2]),
                getMaximumEatenDishCountDeque(test[0], test[1], test[2]),
            )


if __name__ == "__main__":
    unittest.main()
