from typing import List


class Node(object):

    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data

    # def __str__(self):
    #     return str(self.data)

    def __repr__(self):
        return "Node(val=" + str(self.data) + ", next={" + str(self.next) + "})"
    
class LinkedList(object):

    def __init__(self) -> None:
        self.dummy_head = Node()
        pass

    def prepend(self, data) -> Node:
        if data is None:
            return None
        
        node = Node(data)
        if None == self.dummy_head.next:
            self.dummy_head.next = node
        else:
            next = self.dummy_head.next
            self.dummy_head.next = node
            node.next = next
        
        return node
        
    def append(self, data) -> Node:
        if data is None:
            return None
        
        node = Node(data)

        curr_node = self.dummy_head
        while curr_node.next:
            curr_node = curr_node.next
        
        curr_node.next = node
        return node

    def find(self, data) -> Node:
        if None == data:
            return None
        
        node = self.dummy_head.next
        while node:
            if data == node.data:
                return node
            node = node.next

    def delete(self, data) -> bool:
        if None == data:
            return False
        
        prev_node = self.dummy_head
        curr_node = self.dummy_head.next

        if None == curr_node:
            return False
        
        while curr_node:
            if data == curr_node.data:
                prev_node.next = curr_node.next
                return True
            prev_node = curr_node
            curr_node = curr_node.next

        return False

    def get_all_data(self):
        data = []
        node = self.dummy_head.next
        while node:
            data.append(node.data)
            node = node.next
        return data
    
    def __len__(self):
        counter = 0
        node = self.dummy_head.next
        while node:
            counter += 1
            node = node.next
        return counter

    def __repr__(self):
        return "LinkedList(" + str(self.dummy_head.next) + ")"

if __name__ == '__main__':

    l = LinkedList()
    l.prepend(10)
    l.prepend(3)
    l.append(8)
    l.append(None)
    l.append(-1)

    print(l.find(None))
    print(l.find(8))
    print(l.delete(None))
    print(l.delete(-1))
    l.append(0)

    print(l.get_all_data())