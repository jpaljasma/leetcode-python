class Node:
    key = ""
    value = ""
    count = 0
    next = None
    prev = None

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.count = 1
        self.next = None
        self.prev = None

    # def __str__(self) -> str:
    #     return f"{self.key}={self.value} ({self.count})"


class DoublyLinkedList:
    size = 0
    tail = None
    dummy_head = None

    def __init__(self) -> None:
        self.dummy_head = Node(None, None)
        self.tail = self.dummy_head
        self.size = 0
        pass

    def insert(self, node: Node):
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.size += 1

    def remove(self, node: Node = None) -> Node:
        if 0 == self.size:
            return None

        if not node:
            node = self.dummy_head.next

        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # update tail in case node is tail
        if node == self.tail:
            self.tail = self.tail.prev

        self.size -= 1
        return node

    def __len__(self) -> int:
        return self.size


class LRUCache:

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.node_map = {}
        self.node_list = DoublyLinkedList()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        pass

    def get(self, key: str) -> any:
        if key in self.node_map:
            node = self.node_map[key]
            # move most used node to the top and increase usage counter
            node.count += 1
            self.node_list.remove(node)
            self.node_list.insert(node)
            return node.value
        return None

    def _manage_capacity(self):
        # limit capacity by removing the least recently used
        while (len(self.node_list) > self.capacity):
            # least recently used is at the top
            node = self.node_list.dummy_head.next

            print("Removing node", vars(node))
            self.node_list.remove(node)
            del self.node_map[node.key]

    def put(self, key: str, value):
        if key in self.node_map:
            node = self.node_map[key]
            self.node_list.remove(node)
            self.node_list.insert(node)
        else:
            node = Node(key, value)
            self.node_list.insert(node)
            self.node_map[key] = node

        self._manage_capacity()


cache = LRUCache(2)

cache.put("a", {"x": "y"})
cache.put("fish", "bowl")
for n in range(10):
    cache.get("a")
cache.put("cat", "meow")

print("NODES", cache.node_map.keys())

print(vars(cache))
