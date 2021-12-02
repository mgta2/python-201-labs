# Include the current weather into your game mechanics.

URL = "https://www.metaweather.com/api/location/44418/"

# Project: Adventure Game updated to include weather API above.

import requests
import random

print("Welcome to the adventure game.")

response = requests.get(URL)
weather_state = response.json()["consolidated_weather"][0]["weather_state_name"]

print("You wake up in a strange room, in London, UK.\n"
      "Because I have to implement a weather API, there is a small window.\n"
      f"From this window you can see that outside the weather is {weather_state.lower()}."
      )
print()
print("There are 3 doors before you...")
print("Input 1, 2 or 3 to enter the respective door.")
inventory = set()

# Randomly assign the doors to objects behind them.

dragon = random.randint(0,2)
binary = random.randint(0,1)
if binary == 0:
    zombie = (1 + dragon) % 3
    empty = (dragon - 1) % 3
else:
    zombie = (dragon - 1) % 3
    empty = (1 + dragon) % 3

zombie += 1
dragon += 1
empty += 1

while True:
    user_input = input("Which door do you choose?: ")
    if user_input.isdigit():
        user_input = int(user_input)
        if not(user_input in [1, 2, 3]):
            print("You did not enter 1, 2 or 3.")
            continue
    else:
        print("You did not enter an integer.")
        continue
    
    if user_input == empty:
        print("You enter a seemingly empty room.")
        user_input = input("Type 'explore' to look around, else leave: ")
        if user_input == "explore":
            print("You find a sword! It is added to your inventory and you leave the room.")
            inventory.add("sword")
            continue
    
    if user_input == zombie:
        print("You enter a room with a zombie!")
        user_input = input("Type 'attack' or leave the room: ")
        if user_input == "attack":
            if "sword" in inventory:
                print("Your sword cuts down the zombie!")
                print("You see the zombie was guarding some armour.")
                print("The armour is added to your inventory and you leave the room.")
                inventory.add("armour")
                continue
            else:
                print("Weaponless, the zombie kills you swiftly.")
                print("--- Game Over ---")
                break
    
    if user_input == dragon:
        print("You enter the room to see a dragon!")
        user_input = input("Type 'attack' or leave the room: ")
        if user_input == "attack":
            
            # Sword gives 50% chance of victory. Armour ensures survival.
            if "sword" in inventory:
                success = random.randint(0,1)
                if success == 0:
                    print("The dragon sees your attack coming and crushes your sword.")
                    inventory.remove("sword")
                    
                    if "armour" in inventory:
                        print("Your armour saves you from death, but your sword is gone.")
                        print("You retreat back from where you came, to search for another weapon.")
                        continue
                    else:
                        print("With no armour, you die.")
                        print("--- Game Over ---")
                        break
                    
                else:
                    print("Your blade strikes the dragon's weak spot!")
                    print("The dragon is dead! You win!")
                    break
            else:
                print("With no weapon you quickly die.")
                print("--- Game Over ---")
                break
        
        else:
            print("You leave the beast alone and retreat the way you came.")
            continue