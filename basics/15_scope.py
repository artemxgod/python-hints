# global scope
pi = 3.14

def circleArea(r):
    return pi * r * r

print("area of circle with radius 10 is", circleArea(10))

# nonlocal scope
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20 # changes x from outer
        print(x)
    inner()
    print(x) 

outer()

def testScope():
    x = 10
    print(globals())
    print(locals()) # {x : 10}

testScope()

