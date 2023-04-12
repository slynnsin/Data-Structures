# COP 3410- Assignment 7
# Sarah Sindeband
# 4/17/22
# Udemy_CitcularList

'''
Taken from the Udemy course: Python for Data Structures, Algorithms and Interviews
Problem: Given a singly linked list, write a function that takes a node for the linked list and determines if the linked list is cyclic
The fucntion returns a boolean value

'''


# Implement a function that counts the number of nodes in a circularly linked list.
# Test your functions by using the driver in the same file. Create a larger circular linked list and test again.

# creating a stack for the nodes in order to indicate which would be the "head" for counting
# inspitation from the StackUsingLinkedList file from the letcure
class NodeStack:
    # turned the node class into a nested node like the LinkedStack class
    class Node(object):
        def __init__(self,value):
            """create empty node"""
            self.value = value
            self.nextnode = None

# stack methods
    def __init__ (self):
        """constructor for empty stack"""
        self.head = None # head none
        self.size = 0

    def len (self):
        """returns the number of elements in the stack"""
        return self.size

    def is_empty(self):
        """returns true if the stack is empty"""
        return self.size == 0

    def push(self, e):
        '''Add element e to the top of the stack.'''
        self.head = self.Node(e, self.head) # create and link a new node, put e in node, make head
        self.size += 1

    def top(self):
        '''Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        '''
        if self.is_empty( ):
            raise Empty( 'Stack is empty' )
        return self.head.element # top of stack is at head of list

    def pop(self):
        '''Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        '''
        if self.is_empty( ):
            raise Empty( 'Stack is empty' )
        answer = self.head.element
        self.head = self.head.next # bypass the former top node
        self.size -= 1
        return answer
        

# Implement a function that counts the number of nodes in a circularly linked list.
def node_count(node):
    while node.nextnode != head and node.cycle_check == True:
        return len(noed)
    print(count)


def cycle_check(node):

    # Begin both markers at the first node
    marker1 = node
    marker2 = node

    # Go until end of list
    while marker2 != None and marker2.nextnode != None:
        
        # Note
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        # Check if the markers have matched
        if marker2 == marker1:
            return True

    # Case where marker ahead reaches the end of the list
    return False


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
if __name__ == "__main__":

    # CREATE CYCLE LIST

    L = NodeStack()
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = a # Cycle Here!


    # CREATE NON CYCLE LIST
    x = Node(1)
    y = Node(2)
    z = Node(3)

    x.nextnode = y
    y.nextnode = z

    #RUN A CYCLE CHECK
    print(cycle_check(a))
    print(cycle_check(x))

    print(node_count(x))
    
    

    

    

