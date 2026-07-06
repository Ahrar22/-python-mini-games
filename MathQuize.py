import random

Score = 0
rounds = 10

for i in range(rounds):

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*', '/'])

    if operation == '+':
        correct = num1 + num2
    elif operation == '-':
        correct = num1 - num2
    elif operation == '*':
        correct = num1 * num2
    else:
        correct = round(num1 / num2, 2)
    
    answer = input(f"Questions: {num1} {operation} {num2} = ?: ").strip()

    if answer.lower() == 's':
        print(f"Score: {Score}")
        continue

    try:
        user_answer = float(answer)
    except:
        print("Invalid input!")
        break

    if round(user_answer, 2) == round(correct, 2):
        print("Correct!")
        Score += 1
    else:
        print("Wrong!")
        break
print(f"Game over! Final score: {Score}")
