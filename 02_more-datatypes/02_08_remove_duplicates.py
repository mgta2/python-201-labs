# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

# 1.
list_noduplicate = list(set(list_))
print(list_noduplicate)

# 2.
new_list = []
for char in list_:
    if char not in new_list:
        new_list.append(char)
print(new_list)