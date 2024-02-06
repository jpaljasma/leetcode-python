from typing import List
import unittest


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # edge case - [0]
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True

        # left edge [0,0 ...]
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1

        for i in range(1, len(flowerbed) - 1):
            if n < 1:
                break
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

        # right edge [... 0,0]
        if (
            n > 0
            and flowerbed[len(flowerbed) - 1] == 0
            and flowerbed[len(flowerbed) - 2] == 0
        ):
            flowerbed[len(flowerbed) - 1] = 1
            n -= 1

        return n < 1


class TestCanPlaceFlowers(unittest.TestCase):
    def test_place_flowers_true(self):
        s = Solution()
        self.assertTrue(s.canPlaceFlowers([1, 0, 0, 0, 1], 1))
        self.assertTrue(s.canPlaceFlowers([0, 0, 1, 0, 1], 1))
        self.assertTrue(s.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))
        self.assertTrue(s.canPlaceFlowers([0], 1))
        self.assertTrue(s.canPlaceFlowers([0, 0, 0, 0, 1], 2))

    def test_place_flowers_false(self):
        s = Solution()
        self.assertFalse(s.canPlaceFlowers([1, 0, 0, 0, 1], 2))
        self.assertFalse(s.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))


if __name__ == "__main__":
    unittest.main()
