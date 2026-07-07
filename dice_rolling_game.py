#ask the user do you want to roll the dice
# take input from user y/n 
# if user prints y 
#    then generate 2 random numbers
# if user prints n
#    then print "Thanks for playing"
# if user prints anything else
#  then print invalid input 



import random

while True:
    print("do you want to roll dice? (y/n)")

    user_input = input().lower()

    if user_input == 'y':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"you rolled: ({dice1} , {dice2})")
    elif user_input == 'n':
        print("thanks for playing")
        break
    else:
        print("invalid input")
        break