# Midterm review

# Review all lecture notes

# insertion sort

# binary search

# how to sort data set / list -> binary search for value

# give algorithm for finding max/min value -> evaluate complexity
    # sort first

# complexity analysis- # cells of memory the algorithm needs based on n

# sorted(data)
    #O(nlogn)- best complexity for sorting algorithm








# Textbook exercises

    # Chapter 1
    
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
