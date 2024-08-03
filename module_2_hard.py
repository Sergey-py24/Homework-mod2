import random

def _pass():
    list_pass = []
    a = 0
    range_a = range(3, 21)
    number_a = random.choice(range_a)
    a += number_a
    range_pass = range(1, 21)
    for i in range_pass:
        range_pass2 = range(i + 1, 21)
        for j in range_pass2:
            if i != a and j != a and a % (i + j) == 0:
                list_pass.append(i)
                list_pass.append(j)
    print(f'{a} - первое число')
    print(*list_pass, 'проход открыт')



_pass()
