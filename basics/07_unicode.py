# unicode is used to represent characters

var = "3/4"
print (var)
var = "\u00BE" # symbol 3/4
print (var)
var = "\u0031\u0030" # 10
print (var)

# encode string to bytes
string = 'Hail'
tobytes= string.encode('utf-8')
print(tobytes) # b'Hail'
string = tobytes.decode('utf-8')
print(string) # Hail

