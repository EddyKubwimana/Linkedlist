class Node :
    def __init__(self,data):
        self.data = data
        self.next = None


class llist:
    def __init__(self):
        self.head = None

    def insert(self,node):
        new_node = Node(node)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

        

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def insert_head(self,node):
        new_node = Node(node)
        new_node.next = self.head
        self.head = new_node
    def insert_node(self,after, node):
        cur_node= self.head
        while cur_node.next:
            if cur_node.data == after:
                new_node = Node(node)
                new_node.next = cur_node.next
                cur_node.next = new_node
            cur_node = cur_node.next
        return "the node doesn't exist"

    def delete_node(self,node):
        cur_node = self.head
        if self.head.data==node:
            second_part= self.head.next
            self.head = second_part
        elif cur_node.next:
            try:
                while cur_node.next:
                    if cur_node.next.data == node:
                        second_part = cur_node.next.next
                        cur_node.next = None
                        cur_node.next = second_part
                    cur_node = cur_node.next
            except AttributeError:
                cur_node = None

                
               

            
        else:
            return None

    def size(self):
        if self.head == None:
            print(0)
        cur_node = self.head
        length = 0
        while cur_node:
            length+=1
            cur_node = cur_node.next
        print(length)
            
        
        
                
           
        
            

l = llist()
l.insert(10)
l.insert(20)
l.insert(40)
l.insert(70)
l.insert_head(80)
l.print_list()
print()
l.insert_node(10,300)
l.insert_node(10,500)
l.print_list()
l.delete_node(500)
l.delete_node(70)
print()
l.print_list()

print()
l.print_list()
l.size()

    
