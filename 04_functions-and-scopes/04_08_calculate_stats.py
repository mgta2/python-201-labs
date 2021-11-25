# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(*args):
    the_min = args[0]
    the_max = args[0]
    the_sum = 0
    n = len(args)
    for num in args:
        if num > the_max:
            the_max = num
        if num < the_min:
            the_min = num
        the_sum += num
    the_average = the_sum/n
    return [the_min, the_max, the_average]

# call the function below here
my_list = stats(*example_list)
for i in range(0,3):
    print(my_list[i])