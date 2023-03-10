class Node :
    '''
    Node object
    '''
    def __init__(self,data):
        self.data = data
        self.next = None


class llist:
    '''
    Singly linked list
    '''
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,node):
        '''
         This method insert a node at the end of the linked list.
         '''
        new_node = Node(node)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.head = self.tail
            return
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
    

        

    def __str__(self):
        '''
        This method print the nodes that are in the linked list
        '''
        cur_node = self.head
        number = []
        while cur_node:
            number.append(cur_node.data)
            cur_node = cur_node.next
        return f"{number}"

    def prepend(self,node):
        '''
        this function insert the head of the linked list
        '''
        new_node = Node(node)
        new_node.next = self.head
        self.head = new_node
    def insert_node(self,after, node):
        '''
        This method insert a node after a specified node in the list
        '''
        cur_node= self.head
        while cur_node.next:
            if cur_node.data == after:
                new_node = Node(node)
                new_node.next = cur_node.next
                cur_node.next = new_node
            cur_node = cur_node.next

    def delete_node(self,node):
        '''
        This method deletes a given node in the linked list
        '''
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
    @property
    def size(self):
        '''
        This method return the length of the linked list
        '''
        
        if self.head == None:
            return 0
        cur_node = self.head
        length = 0
        while cur_node:
            length+=1
            cur_node = cur_node.next
        return length

    def sort(self, reverse = None):
        '''
        This method return a sorted linked list in ascending order
        '''

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
            if reverse == True:
                self.reverse
                    
    @property
    def reverse(self):
        '''
        This method reverse the linked list
        '''
        if self.head is None:
            raise IndexError("The list is empty")
        
        prev = None
        cur_node = self.head
        while cur_node is not None:
            next_nodes = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next_nodes
        self.tail = self.head
        self.head = prev

            
        
            
            
#Testing the methods and attributes functionalities

ls = llist()
ls.append(10)
ls.append(20)
ls.append(40)
ls.sort(reverse = True)
print(ls.size)
print(ls)




            
            
            
        
        
                
           
        
            




    
