import copy

# shallow (copy reference)
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
shallow_copied_list = copy.copy(original_list)
shallow_copied_list[0][0] = 100
print("original list: {}\nshallow copied list: {}".format(original_list, shallow_copied_list))


# deep copy (completely new object)
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
deep_copied_list = copy.deepcopy(original_list)
deep_copied_list[0][0] = 100
print("original list: {}\ndeep copied list: {}".format(original_list, deep_copied_list))

# slice notation
original_list = [1, 2, 3, 4, 5]
copied_list = original_list[:3]
copied_list[0] = 100

print("original list: {}\ncopied list: {}".format(original_list, copied_list))



