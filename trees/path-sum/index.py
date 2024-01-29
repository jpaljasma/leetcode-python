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

    @property
    def is_leaf(self) -> bool:
        return self.left is None and self.right is None


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum

        def has_sum(node: TreeNode, target: int, current: int) -> bool:
            current += node.val

            if current == target and node.left is None and node.right is None:
                return True

            if node.left is not None:
                if has_sum(node.left, target, current):
                    return True

            if node.right is not None:
                if has_sum(node.right, target, current):
                    return True

            return False

        return has_sum(root, targetSum, 0)


if __name__ == "__main__":
    s = Solution()
    t = TreeNode(8)
    t.left = TreeNode(7)
    t.right = TreeNode(11)

    print(s.hasPathSum(t, 15))
