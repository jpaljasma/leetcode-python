from typing import List, Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        def sumNode(n: ListNode) -> int:
            tot = 0
            power = 0
            while n is not None:
                nums.append(n.val)
                tot += n.val * pow(10,power)
                power += 1
                n = n.next
            return tot
            
        # sum nodes
        res = sumNode(l1) + sumNode(l2)

        if 0 == res:
            return ListNode(0)

        dummyHead = ListNode(0)
        tail = dummyHead

        while res > 0:
            rem = res % 10
            nums.append(rem)
            res = res // 10

            # add new node and move tail
            newnode = ListNode(rem)
            tail.next = newnode
            tail = tail.next
            
        result = dummyHead.next
        
        return result
    

def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))

def LL_to_list(root: ListNode) -> list:
    _tmp = []
    while root:
        _tmp.append(root.val)
        root = root.next
    return _tmp

test = Solution()

a1 = [2,4,3]
a2 = [5,6,4]
result = [7,0,8]

print(LL_to_list(test.addTwoNumbers(list_to_LL(a1), list_to_LL(a2))))

