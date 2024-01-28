from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if not root.left and not root.right:
            return 1

        def find_depth(node: TreeNode, c: int = 0):
            if node is None:
                return c
            c += 1
            da = c
            db = c
            if node.left:
                da = find_depth(node.left, c)
            if node.right:
                db = find_depth(node.right, c)
            return da if da > db else db

        return find_depth(root)


if __name__ == "__main__":
    s = Solution()
    print(s.maxDepth(TreeNode()))
