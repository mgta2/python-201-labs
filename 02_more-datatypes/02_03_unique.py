# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

my_list = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

unique_list = []

for char in my_list:
    if char not in unique_list:
        unique_list += [char]
    else:
        unique_list.remove(char)

print(unique_list)