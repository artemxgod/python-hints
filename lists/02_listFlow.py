# loop
listA = [1,2,3]

for item in listA:
    print(item, end=" ")
print()

index = 0
while index < len(listA):
    print(listA[len(listA) - 1 - index], end=" ") # reverse
    index += 1
print()

indices = range(len(listA))
for index in indices:
    print(listA[index], end=" ")
print()

# comprehension new_list = [expression for item in iterable if condition]
squired = [num ** 2 for num in listA]
print(squired)
listb = ['a', 'b', 'c']
upper = [char.upper() for char in listb if char.isalpha()]
print(upper)

# enumerate
for index, item in enumerate(listA):
    print(index, "--", item)
print()

# sort
list1 = ['physics', 'Biology', 'chemistry', 'maths']
print ("list before sort:", list1)
list1.sort()
print ("list after sort : ", list1)

listA.sort(reverse=True)
print(listA)

# key is a function that defines how to sort 
list1.sort(key=str.lower)
print(list1)

def myfunction(x):
   return x%10
list1 = [17, 23, 46, 51, 90]
print ("list before sort", list1)
list1.sort(key=myfunction)
print ("list after sort : ", list1)



