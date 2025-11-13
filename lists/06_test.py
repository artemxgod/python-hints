# unique in given list
l1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
l2 = []
for item in l1:
    if item not in l2:
        print(item, end=" ")
        l2.append(item)
print()

# sum of all numbers
l1 = [1, 9, 1, 6, 3, 4]
print(sum(l1))

# 5 random numbers list
import random

l1 = []
for item in range(5):
    l1.append(random.randint(1, 100))
print(l1)
