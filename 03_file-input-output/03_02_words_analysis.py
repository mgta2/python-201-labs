# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

with open("words.txt", "r") as file_in:
    my_words = file_in.read()

my_words_corrected = ""

for char in my_words:
    if char.isalpha():
        my_words_corrected += char
    else:
        my_words_corrected += " "

my_list = my_words_corrected.split()

small_words = []
big_words = []
total_words = len(my_list)
minimum = len(my_list[0])
maximum = len(my_list[0])

for word in my_list:
    length = len(word)
    if length > maximum:
        maximum = length
    if length < minimum:
        minimum = length

for word in my_list:
    if len(word) == minimum:
        small_words.append(word)
    if len(word) == maximum:
        big_words.append(word)

print(small_words) # Lots of two-letter words.
print(big_words) # The three big words from previous lab exercise.
print(total_words) # 113809
print(maximum) # 21