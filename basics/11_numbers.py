a = int("10") # 10
b = int(10.5) # 10

print(a, b)

# base 2, 8, 16 numbers

ba = 0b101 # 5
octa = 0o21 # 17
hexa = 0xA # 10
print(ba, octa, hexa) # print in decimal

bina = bin(a)
print(bina) # print in binary

a = int('20', 8) # with base 8
print(a) # print in decimal

# e notation (e is ten raised to)
a = 1.23e4
print(a) # 12300

# complex
a=complex(5.3,6) # 5.3+6j = x + y*j
b=complex(1.01E-2, 2.2E3)
print ("a:", a, "type:", type(a))
print ("b:", b, "type:", type(b))

a = a.conjugate() # 5.3-6j
print ("a:", a, "type:", type(a))
