import random


def prost(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return 'no'
                break
        else:
            return 'yes'
    else:
        return 'no'


rules_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'
example = random.randint(1, 100)
right_answer = prost(example)
text1 = f" is wrong answer ;(. Correct answer was '{right_answer}'."
text2 = "Let's try again, "
