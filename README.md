# Singly Linked list

A singly linked list is a linear data structure in which each element, called a node, contains a reference to the next element in the list. The first element of the list is called the head, and the last element is called the tail. Here is a basic documentation for a singly linked list:

# Properties

Each node contains a value and a reference to the next node
The last node points to None
A head and tail pointer to the first and last element respectively.

# Operations

# Insert at the head

Time Complexity: O(1) as it only requires the modification of the head pointer.
Space Complexity: O(1) as it only requires the creation of a new node.

# Insert at the tail

Time Complexity: O(1) as it requires one to change the tail of the list .
Space Complexity: O(1) as it only requires the creation of a new node.

# Delete a node that is not a head or tail

Time Complexity: O(n) as it requires traversing the entire list to find the node to delete
Space Complexity: O(1) as it only requires modification of the pointers of the previous and next node to the deleted node.
Inserting in the middle

Time Complexity: O(n) as it requires traversing the entire list to find the node to insert after.
Space Complexity: O(1) as it only requires the creation of a new node and modification of the pointers of the previous and next node to the inserted node.
