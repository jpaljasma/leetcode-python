from typing import List


class Node:

    """
    https://leetcode.com/problems/construct-quad-tree/description/
    Watch this https://www.youtube.com/watch?v=UQ-1sBMV0v4

    ROOT node can be considered as the entire grid
    Quadrant: Width = n/2 and Height = n/2
    Idea is to break the quadrant apart until we have individual cells
    If all values in the quadrant are the same, we don't need to break it apart
     - we don't need children (hence we can PRUNE it)
     - it will become a LEAF node

    Define origin of each quadrants based on their top-left position.
    """

    val = 0
    is_leaf = False
    top_left = None
    top_right = None
    bottom_left = None
    bottom_right = None

    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight) -> None:
        # val is true if the node represents a grid of 1, or False if it's a grid of 0s
        self.val = val

        # is_leaf is True when the node is leaf node on the tree, or False if the node has four children
        self.is_leaf = isLeaf

        self.top_left = topLeft
        self.top_right = topRight
        self.bottom_left = bottomLeft
        self.bottom_right = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def dfs(n, r, c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        allSame = False
                        break

            if allSame is True:
                # base case - no children, it's a LEAF!
                return Node(grid[r][c], True)

            # split the grid in half
            n //= 2
            # pick new top-left coords based on the split
            top_left = dfs(n, r, c)
            top_right = dfs(n, r, c + n)
            bottom_left = dfs(n, r + n, c)
            bottom_right = dfs(n, r + n, c + n)

            return Node(None, False, top_left, top_right, bottom_left, bottom_right)

        return dfs(len(grid), 0, 0)
