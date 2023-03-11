import random


num = random.randint(1, 100)


rules_of_the_game = 'Answer "yes" if the number is even, otherwise answer "no".'
example = num


def truth():
    if example % 2 == 0:
        right_answer = 'yes'
        return right_answer
    else:
        right_answer = 'no'
        return right_answer


right_answer = truth()
text = f" is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, "
