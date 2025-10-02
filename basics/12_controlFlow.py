# match statement
def checkVowel(n):
   match n: # switch
      case 'a': return "Vowel alphabet"
      case 'e': return "Vowel alphabet"
      case 'i': return "Vowel alphabet"
      case 'o': return "Vowel alphabet"
      case 'u': return "Vowel alphabet"
      case _: return "Simple alphabet"
print (checkVowel('a'))
print (checkVowel('m'))
print (checkVowel('o'))

words = ["one", "two", "three"]
for x in words:
  print(x)

i = 1
printList = []
while i < 6:
  printList.append(i)
  i += 1
print(printList, sep=", ")

# if else
age=25
print ("age: ", age)
if age >=18:
   print ("eligible to vote")
else:
   print ("not eligible to vote")

# for range
for x in range(85, 87):
   print(x) # 85, 86

# for else
for count in range(6):
   print ("Iteration № {}".format(count))
else:
   print ("for loop over. Now in else block") # print once
print ("End of for loop")

# check prime

import math

i = 2
while (i < 25):
    j = 2
    while (j <= i/j):
        if i % j == 0: break
        j = j+1
    if j > math.sqrt(i): print("{} is prime".format(i))
    i = i + 1