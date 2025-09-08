a = 21
b = 10
c = 0

# arithmetic operators
#  + - * / % ** //

# exponent (степень)
a = 2
b = 10
c = a**b 
print ("a: {} b: {} a**b: {}".format(a,b,c))

# floor division (целочисленное деление)
a = 10
b = 6
c = a//b
print ("a: {} b: {} a//b: {}".format(a,b,c))

# comparison operators 
# == != < > <= >=

# assignment operators 
# = += -= *= /= %= //= **= &= |= ^= <<= >>=

# bytwise operators
# & | ^ ~ << >>
a = 20            
b = 10            

print ('a=',bin(a),'b =',bin(b))
c = 0

c = a & b;        
print ("result of AND is ", c,':',bin(c))

c = a | b 
print ("result of OR is ", c,':',bin(c))

c = a ^ b # xor allows to find unique value
print ("result of XOR is ", c,':',bin(c))

c = ~a # not (see two-complement system) (turns x to -(x+1))
print ("result of NOT is ", c,':',bin(c))

c = a << 2 # left shift
print ("result of left shift is ", c,':',bin(c))

c = a >> 2 # right shift
print ("result of right shift is ", c,':',bin(c))

# logical operators
# and or not
var = 5

print(var > 3 and var < 10)
print(var > 3 or var < 4)
print(not (var > 3 and var < 10))

# membership operators
# in not in
list = [1, 2, 3, 4, 5]

print (2 in list) # true
print (6 not in list) # true

var = "TutorialsPoint"
a = "P"
b = "tor"
c = "in"
d = "To"
print (a, "in", var, ":", a in var)
print (b, "in", var, ":", b in var)
print (c, "in", var, ":", c in var)
print (d, "in", var, ":", d in var)

# identity operators compare the memory locations of two objects
# is is not

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

print("identity operators")
print(a is c)
print(a is b)

print(a is not c)
print(a is not b)

