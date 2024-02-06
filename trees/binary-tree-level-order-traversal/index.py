from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = {}

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def solve(node: TreeNode, level: int):
            if node is None:
                return
            if self.ans.get(level) is None:
                self.ans[level] = []
            self.ans.get(level).append(node.val)
            solve(node.left, level + 1)
            solve(node.right, level + 1)

        solve(root, 0)
        return list(self.ans.values())


if __name__ == "__main__":
    s = Solution()
    print(
        s.levelOrder(
            TreeNode(
                1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3, right=TreeNode(5, right=TreeNode(6))),
            )
        )
    )
