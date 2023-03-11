import random


num1 = random.randint(1, 100)
num2 = random.randint(1, 100)


rules_of_the_game = 'Find the greatest common divisor of given numbers.'
example = f'{num1} {num2}'


def truth(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


right_answer = str(truth(num1, num2))
text = f" is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, "
