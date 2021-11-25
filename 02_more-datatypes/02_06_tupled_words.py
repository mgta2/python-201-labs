# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

user_input = input("Enter a string: ")
my_str = ""

for char in user_input:
    if char.isalpha():
        my_str += char
    if char == " ":
        my_str += " "

my_list = my_str.split()

result_list = []

for word in my_list:
    result_list.append(tuple(word))

print(result_list)