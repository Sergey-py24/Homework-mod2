my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
_x = 0
print(my_list[_x])
while _x <= len(my_list):
    _x = _x + 1
    if my_list[_x] == 0:
        continue
    if my_list[_x] > 0:
        print(my_list[_x])
    else:
        break
while _x > len(my_list):
    break
