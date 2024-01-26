from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode(val = {self.val}, next = {self.next})"

    # makes ListNode iterable
    def __iter__(self):
        current = self
        while current is not None:
            yield current.val
            current = current.next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length
        nl = 0
        node = head
        while node:
            nl += 1
            node = node.next

        n = nl - n
        if n == 0:
            return head.next

        c = 1
        prev = head
        node = head.next

        while node:
            if c == n:
                if node == prev and not node.next:
                    prev = None
                else:
                    prev.next = node.next
                break
            c += 1
            prev = node
            node = node.next

        return head


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

    s = Solution()
    print(list(s.removeNthFromEnd(build_list([1, 2, 3, 4]), 3)))
