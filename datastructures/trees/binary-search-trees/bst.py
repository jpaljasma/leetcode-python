import random


class Node:
    left = None
    right = None
    data = None

    def __init__(self, value: int):
        self.data = value
        self.count = 1
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"Node(data={self.data}, count={self.count}, left={self.left}, right={self.right})"


class bst(object):
    """
    Binary Search Tree (or BST)

    LEFT subtree has values LOWER OR EQUAL to the node
    RIGHT subtree has valuse LARGER than the node

    left < node >= right

    INSERTING
    Keep the BST properties
    - always add the new node as a leaf
    - find a node larger than N, and insert left (as smaller)
    -- i.e. N=14, traverse tree until you find 15, and add 14 as a node(15).left

    DELETE

    Deletion of a leaf = just delete a node
    If deleting node with one child: delete node, and connect it's parent to its child
    When deleting two nodes, find smallest element M that is bigger than (N) - it's on the right side.
    - then move it's LEFT node L as a parent of the M, so that L.left = M.left and M.right = N.right
    """

    def __init__(self) -> None:
        pass

    def insert(self, root=None, nod=None):
        if root is None:
            root = nod
            return
        if nod is None:
            return

        if root.data == nod.data:
            # duplicate, increase counter
            root.count += 1
            print(root)
        elif root.data < nod.data:
            if root.right is None:
                root.right = nod
            else:
                self.insert(root.right, nod)
        else:
            if root.left is None:
                root.left = nod
            else:
                self.insert(root.left, nod)

    def preorder(self, at_node):
        if at_node is not None:
            self.preorder(at_node.left)
            self.preorder(at_node.right)

    def search(self, node: Node, key: int) -> Node:
        """
        node: We start searching from the root first
        key: the number we're searching for
        """
        if node is None:
            return None

        print("Current node value is %0d" % node.data)

        if node.data == key:
            print("Match!")
            return node
        elif node.data < key and node.right is not None:
            print("Going right")
            node = node.right
            return self.search(node, key)
        elif node.left is not None:
            print("Going left ...")
            node = node.left
            return self.search(node, key)

        return None

    def delete(self, node: Node, key: int) -> bool:
        """ """
        if node is None:
            return False

        print("[DEL]\tCurrent node value is %0d" % node.data)

        if node.data == key:
            print(f"[DEL]\tFound match! Deleting {node}")
            return True
        
        if key < node.data:
            # check the left branch
            if node.left is not None:
                print("[DEL]\tSeeking left ...")
                return self.delete(node.left, key)

        if node.right is not None:
            # now check right
            print("[DEL]\tSeeking right ...")
            return self.delete(node.right, key)

        
        return False


if __name__ == "__main__":
    tree = bst()
    root = Node(9)

    nums = [9]

    for i in range(23):
        rnd = random.randint(1, 99)
        nod = Node(rnd)
        nums.append(rnd)

        tree.insert(root, nod)
        print(nod)

    print(tree.preorder(root))
    print(tree.search(root, 3))
    print(tree.search(root, 27))
    print(tree.search(root, 12))

    for i in range(5):
        rnd = random.randint(0, len(nums) - 1)
        print("Delete %d" % nums[rnd])
        print(tree.delete(root, nums[rnd]))
