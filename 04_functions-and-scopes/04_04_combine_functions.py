# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def write_letter(name, text):
    my_str = ""
    my_str += greet("Hello", name) + "\n"
    my_str += text + "\n"
    my_str += f"Good bye {name}"
    return my_str

print(write_letter("Jim", "Thanks for the card."))