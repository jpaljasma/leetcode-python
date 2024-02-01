from typing import List
from abc import abstractmethod

"""
    Code to sort the pros for display
    The algorithm is that there are multiple types of rankers (in this case, Quality and New)
    There is a window that contains a list of rankers, like ['Quality', 'New', 'Quality']
    We want to go through that list such that we choose the first pro from 'Quality', then the first from 'New', then second from 'Quality', and continuing to loop
    until we run out of pros for the list.
"""


class SlidingWindowRanker:
    def __init__(self, window: List[str], rankers: dict):
        self.window = window
        self.rankers = rankers

    def rank(self, pros: List[int]) -> List[int]:
        win_len = len(self.window)
        i = 0
        res = []
        while len(pros):
            algo_name = self.window[i % win_len]
            ranker = self.rankers[algo_name]

            pros = ranker.rank(pros)
            res.append(pros.pop(0))

            i += 1
        return res

    # def rank(self, pros):
    #     r = []
    #     seen = []
    #     finished = []
    #     i = 0
    #     while True:
    #         ranker = self.rankers[self.window[i % len(self.window)]]
    #         values = ranker.rank(pros)
    #         j = 0
    #         while j < len(values):
    #             if values[j] not in seen:
    #                 seen.append(values[j])
    #                 r.append(values[j])
    #                 break
    #             elif (
    #                 j == len(values) - 1
    #                 and self.window[i % len(self.window)] not in finished
    #             ):
    #                 finished.append(self.window[i % len(self.window)])
    #             j += 1
    #         if len(finished) == len(self.rankers):
    #             break
    #         i += 1
    #     return r


class AbstractRanker:
    @abstractmethod
    def rank(self, lst: List[int]) -> List[int]:
        raise NotImplementedError


class QualityRanker(AbstractRanker):
    def rank(self, lst: List[int]) -> List[int]:
        return sorted(lst, reverse=True)


class NewRanker(AbstractRanker):
    def rank(self, lst: List[int]) -> List[int]:
        return sorted(lst)


class SlidingWindowRankerTest:
    def test_ranker(self):
        win = ["Quality", "New", "Quality"]
        rankers = {"Quality": QualityRanker(), "New": NewRanker()}
        res = SlidingWindowRanker(win, rankers).rank([1, 2, 4, 5, 6, 7, 8])
        return res == [8, 1, 7, 6, 2, 5, 4]


print(QualityRanker().rank([1, 3, 2]))
print(NewRanker().rank([1, 3, 2]))

print("TEST 1: ", SlidingWindowRankerTest().test_ranker())
