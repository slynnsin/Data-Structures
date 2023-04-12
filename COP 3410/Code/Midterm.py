# Midterm review


    # Review all lecture notes

    # binary search- ch 4

    # sort function

    # insertion sort

    # how to sort data set / list -> binary search for value

    # complexity analysis- # cells of memory the algorithm needs based on n

    # sorted(data)
        #O(nlogn)- best complexity for sorting algorithm

    # give algorithm for finding max/min value -> evaluate complexity
        # sort first










    # Chapter 1

# Notes
    create_list = [0, 1, 2, 3]                          # faster ch 5
    create_tuple= (0, 1, 2, 3) # cannot be changed
    data_tuple = 2, 4, 6, 8 # automatic packing
    a, b, c, d = range (7, 11) # unpack sequence
    # import modules 1/22


    # give algorithm for finding max/min value -> evaluate complexity
    # 2/2
    # chapter 3 counting primitive operations- 2/2
    # 2/11/22/2 analysis
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val

    # list comprehension
    [ k*k for k in range(1, n+1) ] # [1, 4, 9 ,16]

    factors = [k for k in range(1,n+1) if n % k == 0 # has condition- ir % = 9 (whole numbers)
            
        


# Exercises
    
# R 1.1 Write a short Python function, is multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some
    # integer i, and False otherwise.
def is_multiple(n, m):
    leftover = m % n
    if leftover == 0:
        print(n, "is a multiple of", m)
        return True
    else:
        print(n, "is not a multiple of", m)
        return False

# R 1.2 Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function
    # cannot use the multiplication, modulo, or division operators.
def is_even(k):
    if k % 2 == 0:
        print(k, "is an even number")
        return True
    else:
        print(k, "is not an even number")
        return False
    
# R 1.3 Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the
    # form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.
def minmax():
    data = [2, 1, 9, 5, 7, 6]
    min = max = data[0]
    for j in data:
        if j > max:
            max = j
        elif j < min:
            min = j
    print("The minimum is", min, "and the maximum is", max)
    return min, max

# R 1.4 Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.
def fun(num):
    sum_squares = 0
    count = num
    while (num > 0) and (count > 0):
        squares = (count - 1)**2
        sum_squares += squares
        count -=1
    print("The sum of squares for the numbers less than", num, "is", sum_squares)
    return sum_squares

# R 1.5 Give a single command that computes the sum from Exercise R-1.4, relying on Python’s comprehension syntax and the built-in sum function.
def built_in_fun(built):
    print(sum([i**2 for i in range(built)]))

# R 1.6 Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.
def odds_only(num2):
    sum_squares2 = 0
    if num2 % 2 == 0:
        num2 +=1
    count2 = num2
    built2 = num2 - 2
    while (num2 > 1):
        squares2 = (num2 - 2)**2
        sum_squares2 += squares2
        num2 -=2
    print("The sum of squares of the odd numbers less than", built2, "is", sum_squares2)
    return sum_squares2

# R 1.7 Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the built-in sum function.
def built_in_fun2(built2):
    print(sum([i**2 for i in range(1, built2, 2)]))

# R 1.8 Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n, and expression s[k] is used for
    # index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the same element?

    # n = [1, 2, 3, 4, 5]
    # k = -2
    # print('n[k]: ', n[k])
    # j = k + len(n) # should return 3
    # print('n[j]: ', n[j]) #should print same value as n[k]

# R 1.9 What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80?
def range_skip_10():
    val = range(50, 90, 10) # start, stop non-inclusive, step
    print(list(val))

# R 1.10 What parameters should be sent to the range constructor, to produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
def range_skip_odd():
    val2 = range(-8, 10, 2)
    print(list(val2))

# R 1.11 Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
def list_fun():
    new_list = [2**k for k in range(0,9)]
    print("\n", new_list)
    

# define main function
def main():
    # Exercise 1.1
    print("\nReinforcement Exercise 1.1")
    #n = int(input("Please enter an integer: "))
    #m = int(input("Please enter another integer: "))
    n = 4
    m = 2
    is_multiple(n, m)
    
    # Exercise 1.2
    print("\nReinforcement Exercise 1.2")
    #k = int(input("Please enter an integer: "))
    k = 7
    is_even(k)

    # Exercise 1.3
    print("\nReinforcement Exercise 1.3")
    minmax() 

# Exercide 1.4
    print("\nReinforcement Exercise 1.4")
    #num = int(input("Enter a number: "))
    num = 8
    built = num
    fun(num)

# Exercise 1.5
    print("\nReinforcement Exercise 1.5")
    built_in_fun(built)

# Exercise 1.6
    print("\nReinforcement Exercise 1.6")
    #num2 = int(input("Enter another number: "))
    num2 = 9
    built2 = num2
    odds_only(num2)

# Exercise 1.7
    print("\nReinforcement Exercise 1.7")
    built_in_fun2(built2)

# Exercise 1.9
    range_skip_10()

# Exercise 1.10
    range_skip_odd()

# Exercise 1.11
    list_fun()


main()







    # Chapter 2- Object oriented programming

# Notes
    # assume variables are private- get()
    # 1/28 Vectors
    # Classes
        class Employee:
            def __init__(self, name):
                self.name = name

        john = Employee('John')
        print(john) # John


    # Chapter 3- Algorithm Analysis 2/2

# Notes
    # log n- sorted set & binary search
    # growth graph 2/9
    # log math 2/9
    # big oh- worst case
    # big omega- best case
    # big theta- behave the same- 2/11



    # Chapter 4- Recursion- 2/16
# Notes
    # recursion- if/else
    # factorial 2/16    # linear recursion- 2/18
    # reversing array- 2/18, 2/23
    # reverse order / swap 2/18/22/2
    # binary recursion- binary sum pg 174

    
    

    # Binary Search- O(logn)
def binary_search(data, target, low, high):         # 2/16, &2 for pseudocode, 2/18
    if low > high:
        return False
    else:                           # base case
        mid = (low + high) // 2
        if target == data[mid]:
            return True             # can also return location
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)



    # Chapter 5
# Notes
    # 2/23_2 compact arrays
    # 2/23_3 def power
    # 3/2 array-based sequences
        # import array
    # append= O(n)

    # 3/2 list comprehension- faster\\
    # 3/2_2 append / extend / operations
    # insertion sort 3/4_2- code, 3/4 pseudocode / code
        # O(n^2)
    


def insertion_sort(A):
    # sort by ascending order

    for i in range(1, len(A)):
        for j in range(I, 0, -1):    # -1 b/c backwards
            if A[j] < A[j-1]:
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
    return A
            # nested loops O(n^2) worst case
            # best case O(n)
            # space complexity- O(n) b/c can move around inside array- don't need extra space


# Matrix
    data = [[0] * c for j in range(r)]


















    
