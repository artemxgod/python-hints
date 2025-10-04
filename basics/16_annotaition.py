# annotation is explanatory metadata does not affect runtime behavior

# type hinting

def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))
print(add("hello ", "galaxy"))
print(add.__annotations__)

