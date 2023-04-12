# COP3410 - Assignment 1
# Chapter 1 - Data Structures and Functions
# Name: Jessica Wan
# Date: 1/22/22


############## R-1.1 ##############
def is_multiple(n, m):
    try:
        if n % m == 0:
            print(m, "divides", n)
            return True
        else:
            print(m, "doesn't divide", n)
            return False
    except ZeroDivisionError:  # m = 0 exception
        print(m, "doesn't divide", n, "(or any non-zero integer)")
        return False


############## R-1.2 ##############
def is_even(k):
    i = k
    while i != 0 and i != 1:
        i = i - 2 if i > 0 else i + 2

    if i == 0:
        print(k, "is even.")
        return True
    if i == 1:
        print(k, "is odd.")
        return False


############## R-1.3 ##############
def minmax(data):
    min = max = data[0]
    for val in data:
        if(val < min): min = val
        if(val > max): max = val

    extremes = min, max
    print("The minimum/maximum values in the list", data, "are", extremes)
    return extremes


############## R-1.4 ##############
def sqsum(n):
    sqs = 0
    for i in range(n):
        sqs += i * i

    print("The sum of squares of all positive integers "
          "smaller than", n, "is", sqs)
    return sqs


############## R-1.5 ##############
def sqsum2(n):
    print("The sum of squares of all positive integers "
          "smaller than", n, "is", sum([k * k for k in range(n)]))


############## R-1.6 ##############
def odd_sqsum(n):
    sum = 0
    for i in [k * k for k in range(n)]:
        if i % 2 == 1:
            sum += i
    print("The sum of squares of all odd positive integers "
          "smaller than", n, "is", sum)
    return sum


############## R-1.7 ##############
def odd_sqsum2(n):
    print("The sum of squares of all odd positive integers "
          "smaller than", n, "is", sum([k * k for k in range(n) if k % 2 == 1]))


############## R-1.9 ##############
def range_tens():
    x = range(50, 90, 10)
    print(list(x))


############## R-1.11 ##############
def pow_2(n):
    print("The powers of 2 up to 2 ^", n, "are:", [2**k for k in range(n + 1)])


############## Function Calls ##############
print("R-1.1: Does m divide n?")
is_multiple(17, 2)  # 1
is_multiple(18, -9)
is_multiple(20, 0)
print()

print("R-1.2: Is n even?")
is_even(160)  # 2
is_even(-169)
print()

print("R-1.3: Find min/max of a list")
values = [1, 0, 9, 3, 16, 2]
minmax(values)  # 3
print()

print("R-1.4: Find sum of squares from 1 - n-1")
sqsum(5)  # 4
sqsum2(6)  # 5
print()

print("R-1.5: Find sum of odd squares from 1 - n-1")
odd_sqsum(11)  # 6
odd_sqsum2(12)  # 7
print()

# R-1.8
# As s[-1] is equivalent to s[n-1],
# s[-2] is equivalent to s[n-2], ... we have s[-i] equals index s[n-i].
# So for -n <= k < 0, s[k] and s[k + n] refer to the same element.
# The equivalent index j would be k + n.

print("R-1.9: Create a range of 50, 60, 70, 80")
range_tens()  # 9
print()

print("R-1.11: Create a range of powers of 2 from 1 to 256")
pow_2(8)  # 11
