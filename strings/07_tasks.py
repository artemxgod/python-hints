# 1 find number of vowels in a given string.

mystr = "All animals are equal. Some are more equal"
vowels = "aeiou"

res = 0

for sym in mystr:
    if sym.lower() in vowels: res += 1
print(res)

# 2 Python program to convert a string with binary digits to integer.
mystr = '10101'

def strtoint(mystr):
    for sym in mystr:
        if sym not in "01": return "Error. not a binary number"
    num = int(mystr, 2)
    return num

print("binary {} is decimal {}".format(mystr, strtoint(mystr)))

digits = [str(x) for x in range(10)]
mystr = 'He12llo, Py00th55on!'

def dropNums(mystr):
    res = []
    for sym in mystr:
        if sym not in digits: res.append(sym)

    return "".join(res)

print(mystr, dropNums(mystr))
