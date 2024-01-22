class Node(object):
    """
    Binary tree node implementation.
    Single node with no children is also a binary tree

    Path - sequence of nodes connected in a tree
    Parent - a node above another node, connected by it's edge
    Child - a node below a node, connected by it's edge
     - Binary tree has at most 2 children
    Root - a top of the tree, with no parents
    Tree height - the number of edges on the longest downward path between root and leaf

    Balanced binary tree  - a binary tree which the depth of two subtrees of every node never differ by 1
     - Unbalanced - heigh difference more than one
    

        Node
        /  \
    Node   Node
           /  \
        Node  Node
    """

    data = None
    left = None
    right = None

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"Node({self.data})"


if __name__ == "__main__":
    # create root node
    n = Node(4)

    n.left = Node(5)
    n.right = Node(6)

    n.left.left = Node(7)

    """
    Resulting binary tree (None nodes omitted for brevity)
        4
       / \
      5   6
     /
    7
    """
