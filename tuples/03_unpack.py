tup = (10,20, 30)

# basic unpacking
x,y,z = tup
print(x,y,z)

# unpack with asterisk
x, *y = tup
print (x,y) # 10, [20,30]
