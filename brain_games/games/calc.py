import random


num1 = str(random.randint(1, 100))
num2 = str(random.randint(1, 100))
op = random.choice('+-*')


rules_game = 'What is the result of the expression?'
example = f'{num1} {op} {num2}'
right_answer = str(eval(num1 + op + num2))
text1 = f" is wrong answer ;(. Correct answer was '{right_answer}'."
text2 = "Let's try again, "
