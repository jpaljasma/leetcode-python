from typing import List
import math
import unittest
# Write any import statements here


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here

    if M == 0:
        return N // (K + 1)

    S = sorted(S)

    ans = 0
    index = 0
    increment = 0

    for seat in S:
        seat_index = seat - 1 - K
        increment = math.ceil((seat_index - index) / (K + 1))
        ans += increment
        index = seat + K

    ans += math.ceil((N - index) / (K + 1))

    return ans


class TestGetMaxAdditionalDinersCount(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(getMaxAdditionalDinersCount(10, 1, 2, [2, 6]), 3)
        self.assertEqual(getMaxAdditionalDinersCount(15, 2, 3, [11, 6, 14]), 1)
        pass


if __name__ == "__main__":
    unittest.main()
