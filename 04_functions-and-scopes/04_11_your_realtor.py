# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def advert(**kwargs):
    my_str = ""
    for key, value in kwargs.items():
        my_str += f"{key:>15} : {value}" + "\n"
    print(my_str)
    return None

print("There is an exciting new property available on the market!")
advert(Address = "Planet Earth, Sol, Milky Way", Price = "$2.53", Description = "Cloudy/Blue")