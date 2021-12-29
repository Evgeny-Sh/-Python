from re import match


class OwnError(Exception):
    pass


inp_list =[]
while True:
    n = input('Ввведите число: ')
    if n == 'stop':
        break
    try:
        if any(i.isalpha() for i in n):
            raise OwnError(f'{n} - не является числом')
        else:
            inp_list.append(int(n))
    except OwnError as e:
        print(e)

print('Список чисел: ', inp_list)
