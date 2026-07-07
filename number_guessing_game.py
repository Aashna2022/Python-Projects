"""generate a random number between 1 and 50 
start a loop 
take user input for guess 
if user input == random number then win and break the loop
if user input < random number the print(gues larger number)
if user input > random number then print(guess smaller number)"""

import random
random_number = random.randint(1,50)


while True:
    try:
        user_input = int(input("guess a number between 1 and 50: "))
    except ValueError:
        print("invalid input")
        break

    if user_input == random_number:
        print("you win")
        break
    elif user_input < random_number:
        print("guess larger number")
    elif user_input > random_number:
        print("guess smaller number")
    else:
        print("invalid input")
        break