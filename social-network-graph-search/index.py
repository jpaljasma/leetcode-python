from typing import List
from collections import deque


class PersonNode:
    """ Each Vertex is represented by a PersonNode which maintains a dictionary of friends """

    def __init__(self, node_id: int, name: str) -> None:
        self.friends = {}
        self.id = node_id
        self.name = name
        self.previous_node = None

    def __str__(self) -> str:
        return f"({self.id}){self.name}"

    def friendWith(self, who: 'PersonNode'):
        self.friends[who.id] = who
        who.friends[self.id] = self


def bidireaction_search(left_node_start: PersonNode, right_node_start: PersonNode, max_depth: int = 2):
    if left_node_start == right_node_start:
        """ We found the match - its yourself """
        return left_node_start

    # use python's collection.deque
    left_queue, right_queue = deque(), deque()
    left_visited, right_visited = set(), set()

    left_queue.append(left_node_start)
    right_queue.append(right_node_start)

    left_visited.add(left_node_start)
    right_visited.add(right_node_start)

    depth = 0

    # iterate on one level of the graph on both the forward and backward searches
    while depth < max_depth:

        left_node, right_node = check_neighbors(
            left_queue, left_visited, right_visited)
        if left_node:
            return construct_shortest_path(left_node, right_node)

        right_node, left_node = check_neighbors(
            right_queue, right_visited, left_visited)
        if left_node:
            return construct_shortest_path(left_node, right_node)

        depth += 1

    return None


def check_neighbors(neighbors_queue: deque, visited: set, visited_opposite: set):
    num_neighbors_in_level = len(neighbors_queue)

    for _ in range(num_neighbors_in_level):
        node = neighbors_queue.popleft()
        for neighbor_node in node.friends.values():

            if neighbor_node in visited_opposite:
                return node, neighbor_node

            if neighbor_node not in visited:
                neighbor_node.previous_node = node
                visited.add(neighbor_node)
                neighbors_queue.append(neighbor_node)

    return None, None


def build_list(node: PersonNode):
    new_list = []
    while node:
        new_list.append(node)
        node = node.previous_node
    return new_list


def construct_shortest_path(left_node: PersonNode, right_node: PersonNode):
    a_list = build_list(left_node)
    a_list.reverse()

    b_list = build_list(right_node)

    return a_list + b_list


aNode = PersonNode(1, "John")
bNode = PersonNode(2, "Jane")
cNode = PersonNode(3, "Matt")
dNode = PersonNode(4, "Renee")
eNode = PersonNode(5, "Leah")
fNode = PersonNode(6, "Richard")

# John is a friend with Jane
aNode.friendWith(bNode)
dNode.friendWith(eNode)
dNode.friendWith(bNode)
eNode.friendWith(fNode)
cNode.friendWith(bNode)

search_a = aNode
search_b = fNode

search_result = bidireaction_search(search_a, search_b, 2)
if None == search_result:
    print(search_a, "and", search_b, "are not friends")
else:
    s = list(map(lambda x: str(x), search_result))
    print("FRIENDS:", " -> ".join(s))
