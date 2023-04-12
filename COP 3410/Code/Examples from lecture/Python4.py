## COP3410- Lecture 4
## Control Structures and Functions
## Date: 1/21/2022


####################################################
grade = int(input("enter your final grade out of 100 >> "))
if 90 <= grade <= 100:
    final = 'A'
elif 80 <= grade :
    final = 'B'
elif 70 <= grade :
    final = 'C'
else:
    final = 'F'
print('final grade: ', final)


## practice the Boolean branching statements ########

door_is_closed =  True

if door_is_closed:
    open_door =  True
    door_is_closed =  False
advance = True

print("door:\n", "Closed?", door_is_closed,"\n", "Open?", open_door,"\n", "advance? ", advance,"\n")


#################### more complicated scenario for  ##############################

door_is_closed =  True
door_is_locked = True
unlock_door = False
advance = False

if door_is_closed:
    if door_is_locked:
        unlock_door = True
    open_door = True
advance = True

print("door:", "closed?", door_is_closed,"locked?", door_is_locked, "now unlocked?", unlock_door, "ready to advance?", advance, sep = '\n')


########################## while loop : Make it more functional, allow capital or lower-case letters ########################################

data = input("enter any string, we're looking for the first apprearance of an X: ")
j = 0

# added another condition so that X could be uppercase or lowercase
while j < len(data) and (data[j] != 'X' or data[j] != 'x'):
    j += 1

# if you have NOT reached the end of the file & found X, print the location found
if j != len(data):
    print('found an X at location ', j+1)

# if you HAVE reached the end of the file & have NOT found X, let the user know
else:
    print('No X!')

########################### function definition #######
def count(data, target):
    n = 0
    for item in data:
        if item == target: # found a match
            n += 1
    return n

########### function call ####################
x = count( range(10), 9)
print( x)



##################### List Comprehension ########################
n = 200
total = sum(k *k for k in range(1, n+1))
print('''Total is computed using list comprehension,
        memory is not wasted,
        only one object is calculated''', total)
	







