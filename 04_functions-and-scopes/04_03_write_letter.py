# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.

def write_letter(name, text):
    my_str = ""
    my_str += f"Dear {name}, \n"
    my_str += text + "\n"
    my_str += f"Good bye {name}"
    return my_str

print(write_letter("Jim", "Thanks for the card."))