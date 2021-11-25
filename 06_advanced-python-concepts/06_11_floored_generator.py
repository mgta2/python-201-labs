# Adapt your Generator expression from the previous exercise:
# Add a floor division by 1111 on it.
# What numbers do you get?

my_gen = (x//1111 for x in range(1000000) if x % 1111 == 0)

for x in my_gen:
    print(x)

# Gets numbers from 0 to 1000000//1111 = 900.