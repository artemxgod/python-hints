# add
l1 = [11, 21, 31]
l1.append(41)
print(l1) # [11, 21, 31, 41]
l1.extend([51, 61, 71])
print(l1) # [11, 21, 31, 41, 51, 61, 71]
l1.insert(0, 1)
print(l1) # [1, 11, 21, 31, 41, 51, 61, 71]

# remove 
l1.remove(11)
print(l1) # [1, 21, 31, 41, 51, 61, 71]
l1.pop(0)
print(l1) # [21, 31, 41, 51, 61, 71]
l1.clear()
print(l1) # []

# access
l1 = [51, 21, 21]
print(l1.index(21), l1.count(21)) # 1 2

# copy and order
l2 = l1.copy()
print(l2) # [51, 21, 21]
l1.sort()
print(l1) # [21, 21, 51]
l1.reverse()
print(l1) # [51, 21, 21]




