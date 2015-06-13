class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        current = self.head
        if current:
            return current.__str__()
        return "[]"


    def is_empty(self):
        return self.head == None

    def insert_beginning(self, node):
        node.set_next(self.head)
        self.head = node

    def size(self):
        current = self.head
        size = 0
        if current:
            while current:
                size += 1
                current = current.get_next() 

        return size

    def search(self, item):
        current = self.head
        if current:
            while current.get_data() != item:
                if current.get_next():
                    current = current.get_next()
                else:
                    return False
        else:
            return False
        return True

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        node = self
        if node.next:
            node = node.next
            return str(self.data) + node.__str__() 
        return str(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, next_node):
        self.next = next_node
