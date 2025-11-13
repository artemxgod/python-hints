# concat
listA = [1,2,3]
listB = [4,5,6]

print(listA + listB) # [1, 2, 3, 4, 5, 6]

# repetition
print(listA * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# membership 
print(3 in listA) # True

# sublist # [start:stop] (start inclusive, stop exclusive)
print(listA[1:3]) # [2, 3]

# change range of items
listA[:2] = [10, 20]
print(listA) # [10, 20, 3]
listA[1:] = [100] # 100 will replace both 20 and 3
print(listA) # [10, 100]

# add items
listA.append(999) # last
print(listA) # [10, 100, 999]

listA.insert(1, 1000) # index
print(listA) # [10, 1000, 100, 999]

listA.extend([1001, 1002]) # multiple
print(listA) # [10, 1000, 100, 999, 1001, 1002]


# remove items
listA.remove(1000)
print(listA) # [10, 100, 999, 1001, 1002]

listA.pop(1) # index
print(listA) # [10, 999, 1001, 1002]

listA.clear() # clears the list
print(listA) # []

del listB[1]
print(listB) # [4, 6]
del listB[:2]
print(listB) # []
