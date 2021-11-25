# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enum(list_input, start=0):
    counter = start
    output = []
    for var in list_input:
        output.append((counter,var))
        counter += 1
    return output

my_list = ["a", "b", "c"]

print(my_enum(my_list, start = 1))

for index, letter in my_enum(my_list, 1):
    print(f"{index} - {letter}")

# This doesn't just work for lists. Below uses tuple.

my_tuple = ('yes', 23, True)
for index, element in my_enum(my_tuple):
    print(f"The {index} element is {element}.")

# The outputs are identical for the below:

cars = ["audi", "bmi", "ferrari"]
for car in enumerate(cars):
    print(car)
for car in my_enum(cars):
    print(car)

# Below outputs are also identical.

print(list(enumerate(cars, start = 1)))
print(list(my_enum(cars, start = 1)))