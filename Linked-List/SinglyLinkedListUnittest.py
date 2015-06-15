import unittest
from LinkedList import LinkedList, Node

class NodeFunctionsTest(unittest.TestCase):

    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n3.next = self.n2

    def test_get_data(self):
        self.assertEqual(self.n1.get_data(), 1)
        self.assertEqual(self.n3.get_data(), 3)

    def test_get_next(self):
        self.assertEqual(self.n1.get_next(), None)
        self.assertEqual(self.n3.get_next(), self.n2)

    def test_set_data(self):
        self.n1.set_data(11)
        self.assertEqual(self.n1.data, 11)
    
    def test_set_next(self):
        self.n2.set_next(self.n1)
        self.assertEqual(self.n2.next, self.n1)

class ListFunctionsTest(unittest.TestCase):

    def setUp(self):
        self.l1 = LinkedList()
        self.l2 = LinkedList(2)
        self.l3 = LinkedList(3)

    def test_is_empty(self):
        self.assertEqual(self.l1.head, None)
        self.assertFalse(self.l2.head == None)

    def test_insert_beginning(self):
        self.l1.insert_beginning(1)
        self.assertEqual(self.l1.head.data, 1)
        self.assertEqual(self.l1.head.next, None)

        self.l2.insert_beginning(1)
        self.assertEqual(self.l2.head.data, 1)
        self.assertEqual(self.l2.head.next.data, 2)

    def test_size(self):
        self.assertEqual(self.l1.size(), 0)
        self.assertEqual(self.l2.size(), 1)

    def test_search(self):
        self.assertFalse(self.l1.search(1))
        self.assertTrue(self.l2.search(2))

    def test_remove(self):
        self.l2.remove(2)
        self.assertEqual(self.l2.head, None)

        self.assertFalse(self.l1.remove(1))

        self.l3.insert_beginning(2)
        self.l3.insert_beginning(1)
        self.l3.remove(2)

    def test_index_of(self):
        self.myList = LinkedList()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        self.myList.head = node1
        node1.next = node2
        node2.next = node3
        
        self.assertEqual(self.myList.index_of(1), 0)
        self.assertEqual(self.myList.index_of(2), 1)
        self.assertEqual(self.myList.index_of(3), 2)

        self.assertFalse(self.l1.index_of(1))
        self.assertFalse(self.l2.index_of(1))
        self.assertEqual(self.l3.index_of(1), 0)



if __name__ == '__main__':
    unittest.main()
