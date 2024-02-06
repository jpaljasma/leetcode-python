from typing import List
import unittest


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = []
        if len(candies) == 0:
            return []

        maximum = max(candies)
        for i in range(len(candies)):
            candy_extra = candies[i] + extraCandies
            out.append(candy_extra >= maximum)
        return out


class TestKidsWithCandies(unittest.TestCase):
    solution = None

    def setUp(self) -> None:
        self.solution = Solution()
        return super().setUp()

    def tearDown(self) -> None:
        self.solution = None
        return super().tearDown()

    def test_standard_cases(self):
        self.assertEqual(
            self.solution.kidsWithCandies([2, 3, 5, 1, 3], 3),
            [True, True, True, False, True],
        )

        self.assertEqual(
            self.solution.kidsWithCandies([12, 1, 12], 10),
            [True, False, True],
        )

        self.assertEqual(
            self.solution.kidsWithCandies([], 10),
            [],
        )
        self.assertEqual(
            self.solution.kidsWithCandies([1, 2, 3, 4, 5], 0),
            [False, False, False, False, True],
        )
        self.assertEqual(
            self.solution.kidsWithCandies([1, 2, 3, 4, 5], 3),
            [False, True, True, True, True],
        )


if __name__ == "__main__":
    unittest.main()
