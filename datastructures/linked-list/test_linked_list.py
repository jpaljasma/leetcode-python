import unittest
from linked_list import LinkedList, Node


class TestLinkedList(unittest.TestCase):

    def test_prepend(self):
        linked_list = LinkedList()
        linked_list.prepend(10)
        linked_list.prepend(3)
        linked_list.prepend(2)
        self.assertEqual(linked_list.get_all_data(), [2, 3, 10])

    def test_append(self):
        pass

    def test_find(self):
        ll = LinkedList()

        self.assertIsNone(ll.find(3))
        self.assertIsNone(ll.find(None))

        ll.append("fish")
        ll.append(9)

        fish = ll.find("fish")
        self.assertIsInstance(fish, Node)
        self.assertEqual(fish.data, "fish")

        self.assertIsNotNone(ll.find(9))

        pass

    def test_delete(self):
        ll = LinkedList()
        ll.append(2)
        ll.prepend(3)
        ll.append("fish")
        ll.prepend(9)
        self.assertEqual(4, len(ll))

        self.assertTrue(ll.delete(3))
        self.assertEqual(ll.get_all_data(), [9, 2, 'fish'])

        self.assertFalse(ll.delete(3))

    # @unittest.skip("skipping len tests")
    def test_len(self):
        ll = LinkedList()
        ll.append(2)
        ll.append(None)
        ll.prepend(3)
        ll.prepend(9)

        self.assertEqual(3, len(ll))
        # test validity
        self.assertEqual(ll.get_all_data(), [9, 3, 2])
        pass


if __name__ == '__main__':
    unittest.main()
