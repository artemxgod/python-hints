# set is an unordered collection of unique elements

# creating set 
my_set = {1, 2, 3, 4, 5}
print (my_set)

my_set = set([1,2,3,4,5])
print(my_set)

my_set = {1, 2, 2, 3, 3, 4, 5, 5} 
print (my_set) # {1, 2, 3, 4, 5}

mixed_set = {1, 'hello', (1, 2, 3)}
print (mixed_set)

# add/remove element
my_set = {1, 2, 3, 4, 5}
my_set.add(99)
my_set.remove(2)
print(my_set)

# create using comperehansion
squared_set = {x**2 for x in range(1, 6)}
print(squared_set)

even_set = {x for x in range(1, 11) if x % 2 == 0}
print(even_set)

nested_set = {(x, y) for x in range(1, 3) for y in range(1, 3)}
print(nested_set)

# immutable set 
my_frozen_set = frozenset([1, 2, 3])
print(my_frozen_set) 
# my_frozen_set.add(4) - error