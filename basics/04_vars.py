x = 5
y = "John"
z = 'John' # same as double quotes 
X = 10  # does not overwrite x

print(type(x), type(y), x, X)

# can assign values to multiple variables
a, b, c = 1, 2,3 

# can unpack values from collection
fruits = ["apple", "banana", "strawberry"]

ap, ba, st = fruits

print(ap, ba, st, ap)

# concatenation
print (ap + st)

# here + is math operator
print(x + X)

## global and local variables
x = 'awesome' ## global

def local():
    x = 'fantastic' # local
    print(x)

local()
print(x)

def globalVar():
    global x # changes value of x globally
    x = 'fantastic'
    print(x)

globalVar()
print(x)
