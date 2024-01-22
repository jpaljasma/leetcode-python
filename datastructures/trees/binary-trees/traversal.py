from index import Node
# from typing import List


def in_order(node: Node):
    """
    IN-ORDER traversal LEFT > ROOT > RIGHT
    """
    if node is not None:
        # Left
        in_order(node.left)
        # Root
        print(node.data)
        # Right
        in_order(node.right)


def pre_order(node: Node):
    """
    PRE-ORDER traversal ROOT > LEFT > RIGHT
    """
    if node is not None:
        # Root
        print(node.data)
        # Left
        in_order(node.left)
        # Right
        in_order(node.right)


def post_order(node: Node):
    """
    POST-ORDER traversal LEFT > RIGHT > ROOT
    """
    if node is not None:
        # Left
        in_order(node.left)
        # Right
        in_order(node.right)
        # Root
        print(node.data)


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(5)
    root.right = Node(6)
    root.left.left = Node(7)

    #

    # 7 5 4 6
    print("In order traversal")
    in_order(root)

    # 4 7 5 6
    print("Pre order traversal")
    pre_order(root)

    # 7 5 6 4
    print("Post order traversal")
    post_order(root)
