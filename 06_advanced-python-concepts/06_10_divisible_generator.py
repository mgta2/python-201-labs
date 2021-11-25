# Create a Generator that loops over the given range and prints out only
# the items that are divisible by 1111.

# Not sure exactly what question is asking for.

# Option 1
nums = range(1, 1000000)

my_gen = (x for x in nums)

for x in my_gen:
    if x % 1111 == 0:
        print(x)

# Option 2
other_gen = (x for x in nums if x % 1111 == 0)

for x in other_gen:
    print(x)