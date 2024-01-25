from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return f"ListNode(val = {self.val}, next = {self.next})"


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        # floyd cycle detection algorithm

        # tortoise
        turtle = head
        # hare, jumps 2 steps
        hare = head

        # when we deal with the loop, then at one point tortoise and hare are guaranteed to meet
        while hare and hare.next:
            # leap
            hare = hare.next.next
            turtle = turtle.next
            if turtle == hare:
                return True

        return False

        # naive "I've seen you" approach
        head.seen = True
        node = head.next
        i = 0
        while i < 10**4 and node is not None:
            if hasattr(node, "seen"):
                return True
            node.seen = True
            node = node.next
            i += 1

        return False


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
    s = Solution()

    rec = ListNode(9)
    mylist = rec
    mylist.next = la
    mylist = mylist.next
    mylist.next = rec
    mylist = mylist.next

    # don't do it - throws RecursionError
    # print(mylist)

    print(s.hasCycle(mylist))
