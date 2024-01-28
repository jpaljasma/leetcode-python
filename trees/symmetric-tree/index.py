from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


"""
https://leetcode.com/problems/symmetric-tree/description/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Same shape, but also same value in a mirror.
"""


class Solution:
    def _isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        return (
            left.val == right.val
            and self._isMirror(left.left, right.right)
            and self._isMirror(left.right, right.left)
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self._isMirror(root.left, root.right)


if __name__ == "__main__":
    s = Solution()
    print(s.isSymmetric(TreeNode(10)))
