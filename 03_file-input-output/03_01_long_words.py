# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

with open("words.txt", "r") as file_in:
    my_words = file_in.read()

my_words_corrected = ""

for char in my_words:
    if char.isalpha():
        my_words_corrected += char
    else:
        my_words_corrected += " "

my_list = my_words_corrected.split()
big_words = []

for word in my_list:
    if len(word) > 20:
        big_words.append(word)

print(big_words)

# Result:
#   counterdemonstrations
#   hyperagressiveness
#   microminiaturizations