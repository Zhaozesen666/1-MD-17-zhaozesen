import random


def math_game():
    correct_answers = 0

    while correct_answers < 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_result = num1 + num2

        answer = input(f"{num1} + {num2} = ")

        if answer.isdigit() and int(answer) == correct_result:
            print("Correct!")
            correct_answers += 1
        else:
            print("Wrong answer")

    print(f"Game over. Correct answers: {correct_answers}")


math_game()