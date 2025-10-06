# accessing value
var1 = "Hello"
var2 = "Python"
print(var1[0]) # H
print(var2[1:5]) # ytho

# update (using reassign), cant update elements because string is immutable
var1 = 'Hello World!'
var2 = var1[:6] + 'Python'
print ("Updated String:", var2)

# String Formatting Operator
print("My name is %s and age is %d" % ("Kain", 27))

# print quotes (works vice versa)
print('He said, "Hello World!"')
print("He said, \"Hello World!\"")

# triple quotes
print('''He said, "Hello World!", i said 'bib bob' ''')



