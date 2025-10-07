# using % operator
print("I have %d apples" % 5)
print("I have %s apples" % "five")

# using format() method
print("i have {} apples".format(5))

# using f-strings
price1, price2 = 100, 200
total = f'total: {price1 + price2}'
print(total)

# using string template class
from string import Template

str1 = "Hello and welcome $name!"
obj = Template(str1)
print(obj.substitute(name="amogus"))




