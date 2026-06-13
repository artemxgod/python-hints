# Original tuple
T1 = (37, 14, 95, 40)
# Elements to be added
new_elements = ('green', 'blue', 'red', 'pink')
# Extracting slices of the original tuple
# Elements before index 2
part1 = T1[:2]  
# Elements from index 2 onward
part2 = T1[2:]  
# Create a new tuple 
updated_tuple = part1 + new_elements + part2
# Printing the updated tuple
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)