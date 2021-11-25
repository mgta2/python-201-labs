# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
dict_3 = {}

for char in dict_1.keys():
    dict_3[char] = dict_1[char]

for char in dict_2.keys():
    if char in dict_1.keys():
        dict_3[char] += dict_2[char]
    else:
        dict_3[char] = dict_2[char]

print(dict_3)