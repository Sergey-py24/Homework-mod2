_first=int(input('Введите первое число: '))
_second=int(input('Введите второе число: '))
_third=int(input('Введите третье число: '))
if _first==_second and _second==_third:
    print('3')
elif _first==_second or _second==_third or _first==_third:
    print('2')
elif _first!=_second and _second!=_third:
    print('0')
