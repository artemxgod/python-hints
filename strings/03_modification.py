# To modify string we can turn into list 
name = "Ulys"
listName = list(name)

print(name) # Ulys

listName.insert(4, "s")
print(listName) # ['U', 'l', 'y', 's', 's']

name = ''.join(listName)
print(name) # Ulyss

# stringIO
import io

name = "Kraos"
print(name)

nameio = io.StringIO(name)
nameio.seek(3)
nameio.write("tos")

name = nameio.getvalue()
print(name)

