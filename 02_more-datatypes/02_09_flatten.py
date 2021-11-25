# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

result_list = []

for alist in starter_list:
    result_list += alist

print(result_list)

# We could try and generalise this using nested functions?
# i.e. For each element in list, if not already flat apply same function to it.
# e.g. [[1,2],[2,[1,5]]] -> [[1,2],[2,1,5]] -> [1,2,2,1,5]