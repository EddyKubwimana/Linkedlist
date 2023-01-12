class Node :
    def __init__(self,data):
        self.data = data
        self.next = None


class llist:
    def __init__(self):
        self.head = None

    def insert(self,node):
        ''' this function insert a node at the end of the linked list. it retuns none'''
        new_node = Node(node)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

        

    def __str__(self):
        '''this function print the nodes that are in the linked list'''
        cur_node = self.head
        number = []
        while cur_node:
            number.append(cur_node.data)
            cur_node = cur_node.next
        return f"{number}"

    def insert_head(self,node):
        ''' this function insert the head of the linked list'''
        new_node = Node(node)
        new_node.next = self.head
        self.head = new_node
    def insert_node(self,after, node):
        '''this function insert a node after a specified node in the list'''
        cur_node= self.head
        while cur_node.next:
            if cur_node.data == after:
                new_node = Node(node)
                new_node.next = cur_node.next
                cur_node.next = new_node
            cur_node = cur_node.next

    def delete_node(self,node):
        ''' this function deletes a given node in the linked list'''
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
        '''This function return the length of the linked list'''
        
        if self.head == None:
            print(0)
        cur_node = self.head
        length = 0
        while cur_node:
            length+=1
            cur_node = cur_node.next
        print(length)

    def sort(self):
        '''This function return a sorted linked list'''

        if self.head == None:
            return self.head
        else:
            cur_node = self.head
            x = True
            while x:
                while cur_node.next:
                    x = False
                    if cur_node.data > cur_node.next.data:
                        x  = True
                        temp_var = cur_node.data
                        cur_node.data = cur_node.next.data
                        cur_node.next.data = temp_var
                    cur_node = cur_node.next
            
                cur_node = self.head

    def reverse(self):
        '''This function reverse the linked list'''
        if self.head is None:
            raise IndexError("The list is empty")
        
        prev = None
        cur_node = self.head
        while cur_node is not None:
            next_nodes = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next_nodes
        self.head = prev
            
        
            
            
            
            
    


ls = llist()
ls.insert(10)
ls.insert(20)
ls.insert(30)
ls.insert(40)
ls.insert(100)
print(ls)
ls.reverse()
print(ls)




            
            
            
        
        
                
           
        
            




    
