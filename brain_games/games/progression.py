import random


list = []


def new_list():
    global list
    list.append(random.randint(1, 100))
    list_max = random.randint(5, 9)
    step = random.randint(1, 9)
    i = 0
    while i < list_max:
        ind = list[i] + step
        list.append(ind)
        i += 1
    return list


list2 = []


def reform():
    global list2
    new_list()
    index = random.randint(0, len(list) - 1)
    for i, item in enumerate(list):
        if i != index:
            list2.append(item)
        else:
            item = '..'
            list2.append(item)
    return list2


xmpl = ''


def goin():
    reform()
    global xmpl
    for i in list2:
        xmpl += f'{i} '
    return xmpl


tru = ''


def truth():
    goin()
    global tru
    for i, item in enumerate(list2):
        if item == '..':
            tru = str(list[i])
    return tru


truth()


rules_of_the_game = 'What number is missing in the progression?'
example = xmpl
right_answer = tru
text = f" is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, "
