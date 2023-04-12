# COP3410 - Assignment 7
# Chapter 7 - Linked Lists
# Name: Jessica Wan
# Date: 4/17/22

'''
Doubly Linked List Base and Deque Implementation
Date: 04/07/2022
'''


class DoublyLinkedBase:
    '''A base class providing a doubly linked list representation. This class should not be used publicly'''

    class Node:
        '''Lightweight, nonpublic class for storing a doubly linked node.'''

        def __init__(self, element, prev, next): # initialize node’s field

            self.element = element   # user’s element
            self.prev = prev         # previous node reference
            self.next = next         # next node reference

    def __init__ (self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer # trailer is after header
        self.trailer.prev = self.header # header is before trailer
        self.size = 0 # number of elements]

    def len (self):
        '''Return the number of elements in the list.'''
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_between(self, e, predecessor, successor):
        '''Add element e between two existing nodes and return new node.'''
        newest = self.Node(e, predecessor, successor) # linked to neighbors
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest

    def delete_node(self, node):
        '''Delete nonsentinel node from the list and return its element.'''
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.element      # record deleted element
        node.prev = node.next = node.element = None   # deprecate node
        return element


class Empty(Exception):
    '''Error attempting to access an element from an empty container.

       ************
        (I moved this class outside of the LinkedDeque class, as I think
       the class definition wasn't being compiled previously.)
    '''
    pass

# USING THE DOUBLY LINK BASE CLASS FOR IMPLEMENTAION OF DEQUES


class LinkedDeque(DoublyLinkedBase):  # note the use of inheritance
    '''Double-ended queue implementation based on a doubly linked list.'''
    
    def first(self):
        '''Return (but do not remove) the element at the front of the deque.'''
        if self.is_empty( ):
            raise Empty('Deque is empty')

        return self.header.next.element  # real item just after header
    
    def last(self):
        '''Return (but do not remove) the element at the back of the deque.'''
        # return self.trailer.prev.element if not self.is_empty() else None

        if self.is_empty():
            raise Empty("Deque is empty")

        return self.trailer.prev.element  # real item just before trailer
   
    def insert_first(self, e):
        '''Add an element to the front of the deque.'''
        self.insert_between(e, self.header, self.header.next)  # after header
        
    def insert_last(self, e):
        '''Add an element to the back of the deque.'''
        self.insert_between(e, self.trailer.prev, self.trailer)  # before trailer

    def delete_first(self):
        '''Remove and return the element from the front of the deque.
    
        Raise Empty exception if the deque is empty.
        '''
        if self.is_empty():
            raise Empty("Deque is empty")

        return self.delete_node(self.header.next)  # use inherited method
 
    def delete_last(self):
        '''Remove and return the element from the back of the deque.
        Raise Empty exception if the deque is empty.
        '''
        if self.is_empty():
            raise Empty("Deque is empty")

        return self.delete_node(self.trailer.prev)  # use inherited method


###################################################################
# # ***************** Beginning of assignment ***************** # #
###################################################################


if __name__ == "__main__":
    # # # TESTING DEQUE - INITIALIZATION, INSERTIONS, SIZE/IS_EMPTY # # #

    print("Creating Deque 'cards'.")
    cards = LinkedDeque()  # deque with only header/trailer
    print("Is 'cards' empty:", cards.is_empty())
    print()

    print("************ TESTING INSERTIONS ************\n")
    print("Inserting 'heart' at bottom:")
    cards.insert_last("heart")
    print("Current first card:", cards.first())
    print("Current last card:", cards.last())
    print("Size of cards:", cards.size)
    print()  # Deque: HEADER - heart - TRAILER

    print("Inserting 'clover' at top:")
    cards.insert_first("clover")
    print("Current first card:", cards.first())
    print("Current last card:", cards.last())
    print("Size of cards:", cards.size)
    print()  # Deque: HEADER - clover - heart - TRAILER

    print("Inserting 'spade' at top:")
    cards.insert_first("spade")
    print("Current first card:", cards.first())
    print("Current last card:", cards.last())
    print("Size of cards:", cards.size)
    print()  # Deque: HEADER - spade - clover - heart - TRAILER

    print("Inserting 'diamond' at bottom:")
    cards.insert_last("diamond")
    print("Current first card:", cards.first())
    print("Current last card:", cards.last())
    print("Size of cards:", cards.size)
    print()  # Deque: HEADER - spade - clover - heart - diamond - TRAILER

    # # # CURRENT CARDS: (head to tail) [spade, clover, heart, diamonds] # # #

    # # # TESTING DELETIONS AND ERROR CATCHING # # #

    print("Deque currently has", cards.size, "elements.")
    print("Is 'cards' empty:", cards.is_empty())
    print()

    print("************ TESTING DELETIONS ************\n")
    print("Taking first card:", cards.delete_first())
    print("Current first card:", cards.first())
    print("Current last card:", cards.last())
    print("Size of cards:", cards.size)
    print()  # Deque: HEADER - clover - heart - diamond - TRAILER

    print("Taking last card:", cards.delete_last())
    print("Current first card:", cards.first())
    print("Current last card:", cards.last())
    print("Size of cards:", cards.size)
    print()  # Deque: HEADER - clover - heart - TRAILER

    print("Taking last card:", cards.delete_last())
    print("Current first card:", cards.first())
    print("Current last card:", cards.last())
    print("Size of cards:", cards.size)
    print()  # Deque: HEADER - clover - TRAILER

    print("Taking first card:", cards.delete_first())
    print("Is 'cards' empty:", cards.is_empty())
    print()  # Deque: HEADER - TRAILER

    # # # TESTING Empty ERROR CATCHING # # #

    # print("First card:", cards.first())
    # print("Last card:", cards.last())
    # print("Deleting first card:")
    # cards.delete_first()
    # print()
