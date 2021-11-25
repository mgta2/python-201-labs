# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

string = "codingnomads"
tup = tuple(string)
print(tup) # ('c', 'o', 'd', 'i', ...etc...)

for char in tup:
    print(char)
# Get c, o, d,... on new lines as expected.

for character in string:
    print(character)
# Same output as above, seems to be no difference.