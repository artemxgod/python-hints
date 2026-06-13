# concat
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print (tup3);

# comprehension join
joined_tuple = [item for subtuple in [tup1, tup2] for item in subtuple]
print(joined_tuple)

# delete 
del tup3 # deleted completely, cant be printed

# methods 

tup1 = (25, 12, 10, -21, 10, 100)
print ("Tup1:", tup1)
x = tup1.index(10)
cnt = tup1.count(10)
print ("First index of 10:", x)
print ("amount of object instances in tuple", cnt)