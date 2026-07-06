import random

options = ["Rock", "Paper", "Scissors"]

while True:
    user_chioce = input("Enter Rock, Paper or Scissors: ")

    computer_choice = random.choice(options)
    print(f"Computer Choice: {computer_choice}")

    if user_chioce not in options:
        print("Invlid input!")

    elif user_chioce == computer_choice:
        print("It's a Tie!")

    elif (
        (user_chioce == "Rock" and computer_choice == "Paper")
        or (user_chioce == "Paper" and computer_choice == "Scissors")
        or (user_chioce == "Scissors" and computer_choice == "Rock")
    ):
        print("You win!")

    else:
        print("you lose!")
    print()
