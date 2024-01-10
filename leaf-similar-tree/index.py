from typing import List, Optional

"""
https://leetcode.com/problems/leaf-similar-trees/

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def last_leaf(node: TreeNode) -> list:
            """
            Recursive function to find the last tree nodes
            """
            vals = []
            if not node.left and not node.right:
                vals.append(node.val)
            else:
                if node.left:
                    vals += last_leaf(node.left)
                if node.right:
                    vals += last_leaf(node.right)
            return vals

        # simply compare lists
        return last_leaf(root1) == last_leaf(root2)
        