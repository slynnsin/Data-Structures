''''
Single Linked List Implementation
COP3410 - Spring 2022
Sareh Taebi
'''
class Node:
    '''Lightweight class for storing a singly linked node.'''

    def __init__(self, element,next):     # initialize node’s field
       self.element = element             # reference to user’s element
       self.next = next                   # reference to next node
  
    def getElement(self):                     # Accessor methods
        return  self.element
    
    def getNext(self):                       # Accessor methods
        return  self.next
    
    def setElement(self,new):                 # Modifier methods
        self.element  =  new
         
    def setNext(self,newNext): 
         self.next  =  newNext

        
if __name__ == "__main__":

    # Node Creation
    A = Node(2,None)
    B = Node(3, None)                       #CONNECT NODES
    C = Node(4, None)

    # connect nodes here
    A.next = B
    B.next = C
    C.next = None

    # debugging but better to use methods
    print(A.next, B.next, C.next)
    print(A.element, B.element, C.element)
    A.next.element
    
    #Using methods
    A.getElement()
    B.setElement('new')
    B.setNext(None)
    
