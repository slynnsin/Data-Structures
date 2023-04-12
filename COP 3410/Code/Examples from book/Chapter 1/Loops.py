

# executes once for each element of the data sequence
# val = identifier
total = 0
for val in data:
    total += val


# find the maximum value in a list
# can also use built in max function
biggest = data[0]
for val in data:
    if val > biggest:
        biggest = val


# indexed for loop
# use when you want to find where in the series it is
big_index = 0
# j = counter
for j in range(len(data)):              # range(n) = 0 to n-1, counts over range of indices
    if data[j] > data[big_index]:
        big_index = j
