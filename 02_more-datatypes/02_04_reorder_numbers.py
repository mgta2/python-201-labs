# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1

user_input = input("Enter 10 integers separated by commas: ")

my_list = []

comma_exists = True

while comma_exists:
    comma_index = user_input.find(",") # Gives -1 if doesn't exist.
    if comma_index == -1:
        my_list.append(int(user_input))
        comma_exists = False # This step isn't needed but added for clarity.
        break
    my_list.append(int(user_input[:comma_index]))
    user_input = user_input[comma_index+1:]

# Have converted input into a list.

new_list = []

for i in my_list[1::2]:
    new_list.append(i)
for i in my_list[-2::-2]:
    new_list.append(i)

print(new_list)