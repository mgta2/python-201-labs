# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.

my_gen = (x**2 for x in range(10))

print(my_gen)

for x in my_gen:
    print(x)