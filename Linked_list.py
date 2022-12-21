class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
