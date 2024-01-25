from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode(val = {self.val}, next = {self.next})"


class Solution:
    def merge_two_lists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # create new list head node
        cur = ListNode(0)
        ans = cur

        # merge order two lists
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next

        # add remainders
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next

        return ans.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        # the idea is to merge two lists at the same time using two pointers i and j as the edge
        last = len(lists) - 1
        j = last

        while last > 0:
            i = 0
            j = last
            while j > i:
                lists[i] = self.merge_two_lists(lists[i], lists[j])
                lists[j] = None

                i += 1
                j -= 1
                last = j

        return lists[0]


if __name__ == "__main__":

    def build_list(arr: List[int]) -> ListNode:
        """
        Helper method to build ListNode from List
        """
        head = ListNode(None)
        cur = head

        for n in arr:
            cur.next = ListNode(n)
            cur = cur.next
        return head.next

    la = build_list([1, 2, 3])
    lb = build_list([1, 1, 5, 6])
    lc = build_list([5, 6, 7])
    ld = build_list([1, 2, 3])

    s = Solution()

    print(s.mergeKLists([la, lb, lc, ld]))
