# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(bread_type, *args):
    my_str = ""
    my_str += bread_type + "\n"
    for toppings in args:
        my_str += toppings + "\n"
    my_str += bread_type
    return my_str

print(make_sandwich("ciabatta", "cheese", "meatballs", "tomato sauce"))