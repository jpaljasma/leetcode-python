# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if root is None:
            return "null,"

        left_ser = self.serialize(root.left)
        rigth_ser = self.serialize(root.right)

        return str(root.val) + "," + left_ser + rigth_ser

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs():
            nonlocal data
            val = next(data)
            if "null" == val:
                return None

            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()

            return node

        data = iter(data.split(","))

        return dfs()


if __name__ == "__main__":
    # Your Codec object will be instantiated and called as such:
    ser = Codec()
    deser = Codec()

    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.right.left = TreeNode(4)
    t.right.right = TreeNode(5)

    print(ser.serialize(t))
    print(ser.serialize(t) == ser.serialize(deser.deserialize(ser.serialize(t))))
