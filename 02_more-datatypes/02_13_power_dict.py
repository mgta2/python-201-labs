# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

my_dict = {}

for i in range(1,11):
    my_dict[i] = i**2

print(my_dict)