# interview quesetion
# create stack that behaves like queue ---> must connect to another stack
# first in first out


class Queue2Stacks(object):

    def __init__(self):

        # Two Stacks
        self.instack = []
        self.outstack = []

    def enque(self, element):
        # Add an enqueue with an 'in' stack
        self.instack.append(element)                                 # use append for this class and interview, not real life

    def dequeue(self):

        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())            # instack removal gets appended to outstack

        return self.outstack.pop()


if __name__ == "__main__":

    S1 = []
    S2 = []
    Q2 = Queue2Stacks()


    for i in range(5):
        Q2.enqueue(i)


    for i in range(5):
        print(Q2.dequeue())
