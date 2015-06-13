import unittest
from LinkedList import LinkedList, Node

class NodeFunctionsTest(unittest.TestCase):

    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3, self.n2)

    def test_get_data(self):
        self.assertEqual(self.n1.__str__(), "1")
        self.assertEqual(self.n3.__str__(), "32")

    def test_get_next(self):
        self.assertEqual(self.n1.get_next(), None)
        self.assertEqual(self.n3.get_next(), self.n2)

    def test_set_data(self):
        self.n1.set_data(11)
        self.assertEqual(self.n1.get_data(), 11)
    
    def test_set_next(self):
        self.n2.set_next(self.n1)
        self.assertEqual(self.n2.get_next(), self.n1)

class ListFunctionsTest(unittest.TestCase):

    def setUp(self):
        self.l0 = LinkedList()
        
        self.l1 = LinkedList()
        
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.l2 = LinkedList(self.n1)

    def test_is_empty(self):
        self.assertTrue(self.l1.is_empty())
        self.assertFalse(self.l2.is_empty())

    def test_insert_beginning(self):
        self.l1.insert_beginning(self.n1)
        self.assertEqual(self.l1.__str__(), "1")

    def test_size(self):
        self.assertEqual(self.l0.size(), 0)

        self.l1.insert_beginning(self.n1)
        self.assertEqual(self.l1.size(), 1)
        
        self.assertEqual(self.l2.size(), 1)

    def test_search(self):
        self.assertFalse(self.l0.search(1))
        self.assertFalse(self.l1.search(2))
        self.assertTrue(self.l2.search(1))

if __name__ == '__main__':
    unittest.main()
