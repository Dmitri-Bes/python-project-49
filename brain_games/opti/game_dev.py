import prompt
import importlib
import sys

named = ''


def come(road):
    global named
    named = importlib.import_module(road)


def log():
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n{named.rules_of_the_game}')
    result = 0
    while result <= 3:
        if result == 3:
            print(f'Congratulations, {name}!')
            sys.exit()
        print(f'Question: {named.example}')
        answer = prompt.string('Your answer: ')
        if named.right_answer == answer:
            print('Correct!')
            result += 1
            importlib.reload(named)
            continue
        else:
            print(f"'{answer}'{named.text}{name}!")
            sys.exit()

