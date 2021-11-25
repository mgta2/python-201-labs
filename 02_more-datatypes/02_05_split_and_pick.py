# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

user_input = input("Enter a string: ")

# my_str.split splits up the string by where there are spaces.
# e.g. "hi, good bye".split() = ['hi,', 'good', 'bye']

# First we remove all non-letters, other than spaces.
my_str = ""
for char in user_input:
    if char.isalpha():
        my_str += char
    if char == " ":
        my_str += " "

my_str = my_str.lower()

my_list = my_str.split()

# Use a dictionary to track how many types of word are in my_list

my_dict = {}

for word in my_list:
    if word in my_dict.keys():
        my_dict[word] += 1
    else:
        my_dict[word] = 1

max_value = 0

for key, val in my_dict.items():
    if val > max_value:
        max_value = val
        max_key = key

print("The/a most common word is", max_key)
