from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""


class Solution:
    def __init__(self) -> None:
        self.res = None
        self.k = None

    def solution(self, node: Optional[TreeNode]):
        if not node:
            return

        self.solution(node.left)

        self.k -= 1

        if 0 == self.k:
            self.res = node.val

        self.solution(node.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.solution(root)
        return self.res


if __name__ == "__main__":
    s = Solution()
    print(s.kthSmallest(TreeNode(10), 1))
