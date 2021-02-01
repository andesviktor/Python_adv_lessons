"""
Дана матрица целых чисел 10x10. Вводится число. Выяснить, какие строки и столбцы матрицы содержат данное число. (либо рандом либо чтение из файла (input.txt))
"""

from random import randint


def main():
    matrix = [[randint(10, 51) for i in range(10)] for j in range(10)]
    for i in range(10):
        for j in range(10):
            print(f'{matrix[i][j]:3}', end=' ')
        print()
    while True:
        try:
            find_number = int(input('Введите число от 10 до 50 для поиска оного в матрице: '))
        except ValueError:
            print('Введенная информация - не целое число или ВООБЩЕ НЕ ЧИСЛО. Попробуйте еще раз')
        else:
            print(f'Number range(10,50) — {find_number}')
            break
    row_list = []
    column_list = []
    for i, value1 in enumerate(matrix):
        for j, value2 in enumerate(matrix[i]):
            if value2 == find_number:
                if i not in row_list:
                    row_list.append(i)
                if j not in column_list:
                    column_list.append(j)
    for list_id, number in enumerate(row_list):
        row_list[list_id] = number + 1  # подсчет производить для пользователя именно с цифры 1
    for list_id, number in enumerate(column_list):
        column_list[list_id] = number + 1  # подсчет производить для пользователя именно с цифры 1

    print(sorted(row_list))
    print(sorted(column_list))


if __name__ == "__main__":
    main()
