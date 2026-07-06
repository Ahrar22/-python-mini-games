import random

guess_num = random.randint(1, 100)
while True:
    user_input = input("Enter your guessing number bteween 1 - 100: ")

    if user_input not in guess_num:
        print('Game ended!')
        break
    
    user_input = int(user_input)

    if user_input < guess_num:
        print("Too Low, Guess number!")
    elif user_input > guess_num:
        print("Too High, Guess number!")
    else:
        print("Great, You find the guessing number Congrate!")
        break