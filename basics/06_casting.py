# implicit casting

a = True
b = 2
print(a+b)

# explicit casting

a = True
b = 2
print(int(a) + b)

# binary
a = int('101', 2) # 5
print(a)
#octal
a = int('20', 8) # 16
print(a)
#hexadecimal
a = int('10', 16) # 16
print(a)
a = int('A0', 16) # 160
print(a)

# string
a = str(10E4)
print(a, type(a))