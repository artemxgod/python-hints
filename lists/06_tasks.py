import random

print('1 find unique numbers in a given list')
L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
L2 = []

for num in L1:
    if num not in L2:
        L2.append(num)
L2.sort() # for readablity
print(L2)


print('\n2 find sum of all numbers in a list')
L1 = [1, 9, 1, 6, 3, 4]
mus = 0

for num in L1:
    mus += num
print("Using loop: ", mus)
mus = sum(L1)
print("Using sum(): ", mus)


print("\n3 create a list of 5 random integers")
l1 = []

for idx in range(5):
    l1.append(random.randint(0, 100))
print("Using loop: ", l1)

l1 = [random.randint(0, 100) for _ in range(5)]
print("Using comprehension: ", l1)