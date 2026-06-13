from collections import namedtuple

# Define a namedtuple
Vertex = namedtuple('Vertex', ['x', 'y'])

# Create an instance
v = Vertex(x=10,y=20)

# Access fields
print("Vertex-1:", v.x)
print("Vertex-2:", v.y)

Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# Create a new instance using _make()
p2 = Point._make([30, 40])

# Access fields
print("p2.x:", p2.x)
print("p2.y:", p2.y)

Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('voron', '23', '2541997')

# initializing iterable
li = ['nishu', '19', '411997']

# initializing dict
di = {'name': "navi", 'age': 24, 'DOB': '1391997'}

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**di))