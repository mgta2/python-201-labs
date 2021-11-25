# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def divor(n):
    flag = (n % 4 == 0) or (n % 7 == 0)
    return flag

def divand(n):
    flag = (n % 4 == 0) and (n % 7 == 0)
    return flag

user_input = int(input("Enter an integer between 1 and 1,000,000,000: "))
isdiv_either = divor(user_input)
isdiv_both = divand(user_input)

print("Your number is divisble by either 4 or 7:", isdiv_either)
print("Your number is divislbe by both 4 and 7:", isdiv_both)