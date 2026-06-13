print("1 find unique numbers in tuple")
T1 = (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
T2 = ()
for x in T1:
   if x not in T2:
      T2+=(x,)

print ("original tuple:", T1)
print ("Unique numbers:", T2)