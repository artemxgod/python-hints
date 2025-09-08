# list of variables with differrent types, can also put list into another list
listA = [2023, "Python", 3.11, 5+6j, 1.23E-4]
print(type(listA), type(listA[0]), type(listA[1]), type(listA[2]), type(listA[3]), type(listA[4]))

# tuple is literally a list but immutable
tupleA = (2023, "Python", 3.11, 5+6j, 1.23E-4)
print(type(tupleA), type(tupleA[0]), type(tupleA[1]), type(tupleA[2]), type(tupleA[3]), type(tupleA[4]))



# string methods

str = 'Hello Python!'

# H e Python n Python!Python! # [x:y] includes x but not y
print(str[0], str[1:2], str[6:], str[-2], str[6:]*2)


# range is immutable sequence of numbers
for i in range(5):
    print (i)
print('\n')

for i in range(1, 5, 2):
    print(i)

# bytes

# immutable
b1 = bytes([65, 66, 67, 68, 69])  
print(b1)

b2 = b'Python'
print(b2)

# mutable
b3 = bytearray([72, 101, 108, 108, 111])  
print(b3)

b4 = bytearray("Python", "utf-8")
print(b4)

# memoryview is a build-in object that provides a view into the memory of the original object
view = memoryview(b4)
print(view)

import array

arr = array.array('i', [1,3,2])
view1 = memoryview(arr) 
view2 = memoryview(arr[2:])
print(view1, view2)

# dictionary: key-value pairs
dict = {}
dict['one'] = 'biba'
dict[2] = 'boba'
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

# set (math set) unorgonized collection of unique values
set = {1, 2, 3, 4+2j, 5E-4}
print(set)

# frozenset immutable set
fset = frozenset({1, 2, 3, 4+2j, 5E-4})
print(fset)

# nulltype 
x = None

# Printing its value and type
print("x = ", x)
print("type of x = ", type(x))

# type conversion
print("Conversion to integer data type")
a = int(1)     # a will be 1
c = int("3")   # c will be 3

print (a)
print (c)

print("Conversion to floating point number")
a = float(1)     # a will be 1.0
c = float("3.3") # c will be 3.3

print (a)
print (c)

