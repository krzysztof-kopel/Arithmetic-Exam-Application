import random
signs = '+', '-', '*'
number_of_tries = 5


def take_input():
    answer = 0
    while True:
        try:
            answer = int(input())
        except ValueError:
            print("Incorrect format.")
            continue
        else:
            break
    return answer


def calculate(operation):
    current_sign = None
    score = 0
    for element in operation:
        if element in signs:
            current_sign = element
        elif element not in signs and current_sign is not None:
            if current_sign == "+":
                score += int(element)
            elif current_sign == "-":
                score -= int(element)
            elif current_sign == '*':
                score *= int(element)
        elif element not in signs and current_sign is None:
            score += int(element)
    return score


def play_level_1():
    right_counter = 0
    for i in range(number_of_tries):
        equation = f"{random.randint(2, 9)} {random.choice(signs)} {random.randint(2, 9)}"
        print(equation)
        answer = take_input()
        if answer == calculate(equation.split()):
            print("Right!")
            right_counter += 1
        else:
            print("Wrong!")
    return right_counter


def play_level_2():
    right_counter = 0
    for i in range(number_of_tries):
        number = random.randint(11, 29)
        print(number)
        answer = take_input()
        if answer == number ** 2:
            print("Right!")
            right_counter += 1
        else:
            print("Wrong!")
    return right_counter


level1 = 1, "simple operations with numbers 2-9"
level2 = 2, "integral squares of 11-29"
levels = [level1, level2]
print("Which level do you want? Enter a number:")
for level in levels:
    print(f"{level[0]} - {level[1]}")
chosen_level = int(input())
result = 0
if chosen_level == 1:
    result = play_level_1()
    print(f"Your mark is {result}/{number_of_tries}. Would you like to save the result? Enter yes or no.")
elif chosen_level == 2:
    result = play_level_2()
    print(f"Your mark is {result}/{number_of_tries}. Would you like to save the result? Enter yes or no.")

answer_to_file = input()
if answer_to_file in ["yes", "YES", "y", "Yes"]:
    name = input("What is your name?\n")
    file = open("results.txt", 'a')
    file.write(f"{name}: {result}/{number_of_tries} in level {chosen_level} ({levels[chosen_level - 1][1]}).\n")
    print('The results are saved in "results.txt".')
    file.close()
