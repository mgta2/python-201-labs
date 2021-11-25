# Add type annotations to the three functions shown below.

def multiply(num1 : float, num2 : float) -> float:
    return num1 * num2

def greet(greeting : str, name : str) -> str:
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def shopping_list(*args : str) -> tuple:
    [print(f"* {item}") for item in args]
    return args

#args gets "put in" as a tuple according to type(shopping_list(""))