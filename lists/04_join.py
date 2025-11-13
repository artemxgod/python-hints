# concat
L1 = [10, 20, 30]
L2 = [11, 22, 33]

L3 = L1 + L2
print(L3)

# comprehension
L1 = [10, 20, 30]
L2 = [11, 22, 33]

L3 = [item for sublist in [L1, L2] for item in sublist]
print(L3)

