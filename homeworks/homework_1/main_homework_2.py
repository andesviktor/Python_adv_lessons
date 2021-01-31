from random import randint

matrix = [[randint(0, 50) for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        print(f'{matrix[i][j]:3}', end=' ')
    print()
while True:
    try:
        find_number = int(input('Введите числа для поиска оного в матрице: '))
    except ValueError:
        print('Введенная информация - не целое число или ВООБЩЕ НЕ ЧИСЛО. Попробуйте еще раз')
    else:
        list111 = [a for a, x in enumerate(matrix[i]) if x == find_number]
        list222 = [b for b, y in enumerate(matrix[i][j]) if y == find_number]
        print(list111)
        print(list222)

        break
