# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

loses = 0
my_set = set() # Can't use {} else get dictionary.

while loses < 5:
    user_input = input("Enter an integer: ")
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("You did not enter an integer.")
        continue
    if user_input in my_set:
        loses += 1
        print("You've made", loses, "mistakes.")
        continue
    else:
        my_set.add(user_input)
    if len(my_set) > 10:
        print("You've won!")
        break