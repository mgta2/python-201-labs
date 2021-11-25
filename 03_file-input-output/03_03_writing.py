# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

with open("words.txt", "r") as file_in:
    my_words = file_in.read()

my_words_corrected = ""

for char in my_words:
    if char.isalpha():
        my_words_corrected += char
    else:
        my_words_corrected += " "

my_list = my_words_corrected.split()

new_list = []

for word in my_list:
    new_list.append(word[::-1])

with open("words_reverse.txt", "w") as reverse_words:
    reverse_words.write("\n".join(new_list))