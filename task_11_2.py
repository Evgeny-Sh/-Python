class OwnError(Exception):
    pass


a = float(input("Введите делимое a: "))
b = float(input("Введите делитель b: "))

try:
    if b == 0:
        raise OwnError('Делитель не может равняться 0')
    else:
        print(f'a/b={a/b}')
        
except OwnError as e:
    print(e)
