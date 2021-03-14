# sequences.py

myList = [10,20,30,"hello", True, 7.34,"TheEnd"]
print(myList)
print(myList[3])

print(myList[:3])
print(myList[4:])
print(myList[1:3])
print(myList[-1])

myList[3] = "HelloWorld"
print(myList)

# iterate over list
for x in myList:
    print(x, end="\n")


print([i for i in myList])

x = [1,2,3,4]
y = [5,6,7,8]
print(x + y)

print(len(x))
print(max(x))
print(min(x))


# list methods
z = [1,2,3]
z.append(4)		# append to end of list
print(z)
z.insert(0,44)  # index and value
print(z)
z.remove(44)	# remove element 44
print(z)
z.pop(0)		# remove element with index 0
print(z)
print(z.index(2))	# get index of this element

# sort a list
unsortedList = [7,1,5,8,9,2,4,3]
unsortedList.sort()	# have to sort before print
print(unsortedList)

list = [4,6,1,2,9,0]
print(sorted(list))  # print the list sorted, but do not change the list
print(list)

# tuple. Can not be changed
myTuple = (1,2,3)
print(len(myTuple))
print(myTuple[1])