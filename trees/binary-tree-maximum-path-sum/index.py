from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


class Solution:
    ans = -float("inf")

    def solve(self, node: TreeNode):
        if node is None:
            return 0

        left = self.solve(node.left)
        right = self.solve(node.right)

        max_side = max(node.val, node.val + max(left, right))
        max_current = max(max_side, node.val + left + right)

        self.ans = max(self.ans, max_current)

        return max_side

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -float("inf")
        self.solve(root)

        return self.ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxPathSum(TreeNode(69)))
