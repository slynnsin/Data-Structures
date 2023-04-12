class PracticeStack:
    def __init__(self):
        self._stack = [ ]

    def __len__ (self):
        return len(self._stack)

    def is_empty(self):
        return len(self._stack) == 0

    def push(self, e):
        self._stack.append(e)

    def top(self):
        return self._stack[-1]

    def pop(self):
        return self._stack.pop()

    def __str__(self):
        return str(self._stack)


def transfer(S, T):
    n = len(S)
    i = 0
    while i < n:
        T.push(S.top())
        S.pop()
        i+=1
    return T
    


if __name__ == "__main__":
    S = PracticeStack()
    T = PracticeStack()

    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)

    print(S)

    transfer(S, T)

    print(T)


    
    
