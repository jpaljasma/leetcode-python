from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode(val = {self.val}, next = {self.next})"


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur = ListNode(None)
        head = cur

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        while list1:
            cur.next = list1
            cur = cur.next
            list1 = list1.next
        while list2:
            cur.next = list2
            cur = cur.next
            list2 = list2.next

        return head.next


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
    s = Solution()

    print(s.mergeTwoLists(la, lb))
