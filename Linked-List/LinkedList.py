class LinkedList:
    '''
    A singly linked list.
    '''
    def __init__(self, head=None):
        if head:
            self.head = Node(head)
        else:
            self.head = head

    def __str__(self):
        current = self.head
        result = "["
        if current:
            result += current.__str__()
        return result + "]"


    def is_empty(self):
        '''
        Check if the linked list is empty.
        '''
        return self.head == None

    def insert_beginning(self, item):
        '''
        Inserts a Node to the beginning of the list.
        '''
        node = Node(item)
        node.set_next(self.head)
        self.head = node

    def size(self):
        '''
        Get the size of the linked list.
        '''
        current = self.head
        size = 0
        if current:
            while current:
                size += 1
                current = current.get_next() 

        return size

    def search(self, item):
        '''
        Searches the list for a Node which has data matching 'item'.
        '''
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        '''
        Removes the node in item whose data is equal to 'item'. Return nothing if node does not
        exist.
        '''
        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.get_data() == item:
                found = True
                if prev:
                    prev.set_next(current.get_next())
                else:
                    self.head = current.get_next()
            else:
                prev = current
                current = current.get_next()
        
        return found
        
        if prev:
            prev.set_next(current.get_next())

        else: # self.head is the node we want to remove
            self.head = current.get_next()

    def index_of(self, item):
        '''
        Checks if a node exists whose data is equal to item. If it does exist, return the
        index of that node (index starts at 0, meaning that the first item on the list has
        an index of 0). If it does not exist, return false.
        '''
        current = self.head
        found = False
        index = 0

        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                index += 1
                current = current.get_next()

        if found:
            return index

        return False
                

        
class Node:
    '''
    Node for a singly linked list.
    '''
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        node = self
        result = ""
        if node.next:
            node = node.next
            return str(self.data) + ", " + node.__str__()
        return str(self.data)

    def get_data(self):
        '''
        Get the data of a node.
        '''
        return self.data

    def get_next(self):
        '''
        Get the next item which the given node links to (could be another node or could
        be None - None if the given node is the tail of the linked list).
        '''
        return self.next

    def set_data(self, new_data):
        '''
        Set the data of the given node.
        '''
        self.data = new_data

    def set_next(self, next_node):
        '''
        Set the next item of a given node.
        '''
        self.next = next_node
