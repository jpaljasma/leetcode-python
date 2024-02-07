import unittest


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    def runfunc(begin: str, middle: str, end: str) -> int:
        ret = 0
        w = list(C)

        for i in range(N - X):
            c = w[i]
            if c == begin:
                for j in range(i + X, min(i + 1 + Y, N)):
                    a = w[j]
                    if a == middle:
                        for k in range(min(j + X, N), min(j + 1 + Y, N)):
                            b = w[k]
                            if b == end:
                                ret += 1
        return ret

    ret = 0

    ret += runfunc("P", "A", "B")
    ret += runfunc("B", "A", "P")

    return ret


class TestArtisticPhotograpCount(unittest.TestCase):
    def test_classic(self):
        self.assertEqual(getArtisticPhotographCount(5, "APABA", 1, 2), 1)
        self.assertEqual(getArtisticPhotographCount(5, "APABA", 2, 3), 0)
        self.assertEqual(getArtisticPhotographCount(8, ".PBAAP.B", 1, 3), 3)


if __name__ == "__main__":
    unittest.main()
