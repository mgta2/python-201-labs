# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

user_input = input("Enter some text: ")
my_dict = {}

for char in user_input:
    if char.isalpha():
        if char in my_dict.keys():
            my_dict[char] += 1
        else:
            my_dict[char] = 1

print(my_dict)