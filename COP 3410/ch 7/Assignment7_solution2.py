# COP3410 - Assignment 7
# Chapter 7 - Linked Lists
# Name: Jessica Wan
# Date: 4/16/22

'''
Taken from the Udemy course: Python for Data Structures, Algorithms and Interviews
Problem: Given a singly linked list, write a function that takes a node for the linked list and determines if the linked list is cyclic
The fucntion returns a boolean value

'''


class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


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


###################################################################
# # ***************** Beginning of assignment ***************** # #
###################################################################


def cycle_length(node):
    # Function to find length of cyclic list

    if not cycle_check(node):     # if list is not cyclic, return -1
        return -1

    marker = node
    marker2 = node.nextnode     # marker to trace the cycle
    length = 1                  # length starts with only the first node

    while marker2 != marker:
        length += 1                 # increment length by 1
        marker2 = marker2.nextnode  # then continue to the next node

    # as the list is cyclic, marker2 must reach the original node
    # after traversing the whole cycle once.

    # so, length now equals the length of the cycle,
    # as each unique node increments it by one.

    return length


if __name__ == "__main__":

    # # # TESTING CYCLE CHECK AND LENGTH # # #

    # Create a circular list
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = a  # Cycle Here! List: a - b - c - a...

    # Create non-circular list
    x = Node(1)
    y = Node(2)
    z = Node(3)

    x.nextnode = y
    y.nextnode = z  # List: x - y - z - None

    # Run a cycle check
    print("******* Circular list check *******")
    print("Cycle check for node a:", cycle_check(a))
    print("Length of cycle:", cycle_length(a))
    print()

    print("******* Non-circular list check *******")
    print("Cycle check for node x:", cycle_check(x))
    print("Length of cycle:", cycle_length(x))
    print("\n")

    # Other cyclic lists

    a.nextnode = a  # List: a - a... length 1
    print("******* Circular list with single element *******")
    print("Cycle check for node a:", cycle_check(a))
    print("Length of cycle:", cycle_length(a))
    print()

    d = Node(1)
    e = Node(5)
    f = Node(6)
    g = Node(7)

    a.nextnode = b
    c.nextnode = d
    d.nextnode = e
    e.nextnode = f
    f.nextnode = g
    g.nextnode = a  # List: a - b - c - d - e - f - g - a... length 7

    print("******* Larger circular list *******")
    print("Cycle check for node a:", cycle_check(a))
    print("Length of cycle:", cycle_length(a))
    print("Cycle check for node g:", cycle_check(g))
    print("Length of cycle:", cycle_length(g))
    print()
