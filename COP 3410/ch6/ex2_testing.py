## Chapter 6: Stacks
## 3/23/2022

# COP3410 - Assignment 6
# Chapter 6 - Stacks
# Name: Jessica Wan (& Dr. Taebi)
# Date: 4/1/22


class ArrayStack:
    '''LIFO Stack implementation using a Python list as underlying storage.'''

    def __init__ (self):
        '''Create an empty stack.'''
        self._data = [] # nonpublic list instance

    def __len__ (self):
         '''Return the number of elements in the stack.'''
         return len(self._data)

    def is_empty(self):
         '''Return True if the stack is empty.'''
         return len(self._data) == 0

    def push(self, e):
         '''Add element e to the top of the stack.'''
         self._data.append(e)  # new item added at end of list

    def top(self):
         '''Return (but do not remove) the element at the top of the stack.
         Raise Empty exception if the stack is empty.
         '''
         if self.is_empty( ):
             raise Empty( 'Stack is empty' )
         return self._data[-1]  # last item of list

    def pop(self):
        '''Remove and return the element from the top of the stack (i.e., LIFO).

         Raise Empty exception if the stack is empty.
        '''
        if self.is_empty():
          raise Empty( 'Stack is empty' )
        return self._data.pop()  # remove last item from list

    def __str__(self):
        '''Print the elements of a stack in bottom to top order'''

        temp = ArrayStack()
        while not self.is_empty():
            temp.push(self.pop())

        strRep = "["
        while len(temp) >= 2:
            val = temp.pop()       # pop elements from temp in order
            strRep = strRep + str(val) + ", "
            self.push(val)            # push back into S in original order

        if len(temp) == 1:
            val = temp.pop()       # pop last element and print (unless temp was empty)
            strRep = strRep + str(val)
            self.push(val)

        strRep = strRep + "]"
        return strRep


class Empty(Exception):
    '''Error attempting to access an element from an empty container.'''
    pass


def transfer(S, T):
    '''Transfer all elements of stack S onto stack T, in reverse order.
        Exercise R-6.3
    '''
    try:
        while not S.is_empty():
            T.push(S.pop())
    except TypeError:
        print("S and T must be stacks.")


# def reverse_file(filename):
#     '''Overwrite given file with its contents line-by-line reversed.'''
#     print("reversefile executing")
#     S = ArrayStack()
#     original = open(filename)
#     for line in original:
#         S.push(line.rstrip( '\n' )) # we will re-insert newlines when writing
#     original.close( )
#     # now we overwrite with contents in LIFO order
#     output = open(filename, 'w' ) # reopening file overwrites original
#     while not S.is_empty( ):
#         output.write(S.pop( ) + '\n' ) # re-insert newline characters
#     output.close( )
# reverse_file("ReverseFile.txt")

if __name__ == "__main__":
    S = ArrayStack()
    S.push(5)
    S.push(3)
    S.push(9)
    S.push(10)  # contents: [5, 3, 9, 10]

    T = ArrayStack()
    T.push(11)
    T.push(1)
    T.push(8)
    T.push(5)  # contents: [11, 1, 8, 5]

    print("Stack S:", S)  # [5,3,9,10]
    print("Stack T:", T)  # [11,1,8,5]
    print()
    print("Transferring S to T.")
    transfer(S, T)
    print("Stack S:", S)  # [] - empty
    print("Stack T:", T)  # [11,1,8,5,10,9,3,5] - original elements of T with S in reverse order

    print("Transferring T to S.")
    transfer(T, S)
    print("Stack S:", S)  # [5,3,9,10,5,8,1,11]
    print("Stack T:", T)  # [] - empty

    print("Transferring T to S.")
    transfer(T, S)        # No change
    print("Stack S:", S)
    print("Stack T:", T)
