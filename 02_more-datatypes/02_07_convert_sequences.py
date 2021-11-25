# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

my_tup = tuple(string)
print(my_tup)
my_list = list(my_tup)
print(my_list)

for i in range(0,len(my_list)):
    if my_list[i] == "c":
        my_list[i] = "k"

print(my_list)
new_tup = tuple(my_list)
print(new_tup)