# сигнатура syntax to define a function

"""
def function_name( parameters ):
    "function_dostring"
    function_suite
    return [expression]
"""

def my_function():
    "Greetings function"
    print("Hello from a function")

my_function()

# by reference
def testfunction(arg):
   "test reference"
   print ("Inside function:",arg)
   print ("ID inside the function:", id(arg))
   arg=arg.append(100)
   
var=[10, 20, 30, 40] # will change
print ("ID before passing:", id(var))
testfunction(var)
print ("list after function call", var)

# by value 
def testInt(arg):
    "test value"
    print("Inside function:", arg)
    arg = arg + 1
    print("ID inside the function:", id(arg))

var = 10 # wont change
print("ID before passing:", id(var))
testInt(var)
print("Integer after function call", var)

# keyword arguments 
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# so we specify the parameters by name
printinfo( age=50, name="miki" )

# Positional-only arguments
def posFun(x, y, /, z):
    print(x + y + z)

print("Evaluating positional-only arguments: ")
posFun(33, 22, z=11) 

# Keyword-only arguments 
def keyOnly(*, x, y, z):
    print(x + y + z)

print("Evaluating keyword-only arguments: ")
keyOnly(x=33, y=22, z=11)

# Arbitrary or Variable-length Arguments
# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )

# lambda is anonymous function with a single statement

sum = lambda x, y: x+y 
print("{} + {} = {}".format(10, 20, sum(10, 20)))

# default args used if arg is not passed

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("Russia")
my_function() # Norway default
my_function("Brazil")

# arbitary keyword argument kwarg is a dictionary of argumenets

def addr(**kwargs):
   for k,v in kwargs.items():
      print ("{}:{}".format(k,v))

addr(Name="John", City="Juneau")

# pass four keyword args
addr(Name="Alexander", City="Juneau", ph_no="9123134567", PIN="400001")

