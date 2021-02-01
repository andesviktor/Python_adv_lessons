"""
Программа принимает от пользователя диапазоны для коэффициентов a, b, c квадратного уравнения: ax2 + bx + c = 0. Перебирает все варианты целочисленных коэффициентов в указанных диапазонах, определяет квадратные уравнения, которые имею решение
"""

from math import sqrt


def main():
    print("Формула: ax^2+bx+c=0", sep='\n')
    while True:
        try:
            start_a = int(input('Введите начальное значение диапазона a: '))
            finish_a = int(input('Введите конечное значение диапазона a: '))
            start_b = int(input('Введите начальное значение диапазона b: '))
            finish_b = int(input('Введите конечное значение диапазона b: '))
            start_c = int(input('Введите начальное значение диапазона c: '))
            finish_c = int(input('Введите конечное значение диапазона c: '))
        except ValueError:
            print('ВНИМАНИЕ: не целое числовое значение или вообще не числовое значение. Повторите')
        else:
            break
    print() #start_a, finish_a, start_b, finish_b, start_c, finish_c
    list_a = sorted([start_a, finish_a])
    list_b = sorted([start_b, finish_b])
    list_c = sorted([start_c, finish_c])
    for a in range(list_a[0], list_a[1] + 1):
        for b in range(list_b[0], list_b[1] + 1):
            for c in range(list_c[0], list_c[1] + 1):
                d = b ** 2 - 4 * a * c
                if d == 0:
                    try:
                        x = (-b + sqrt(d)) / (2 * a)
                    except ArithmeticError:
                        print(a, b, c, 'No:', 'Происходит деление на ноль')
                        continue
                    print(a, b, c, 'Yes', x)
                elif d < 0:
                    continue
                else:
                    try:
                        x1 = (-b + sqrt(d)) / (2 * a)
                        x2 = (-b - sqrt(d)) / (2 * a)
                    except ArithmeticError:
                        print(a, b, c, 'No:', 'Происходит деление на ноль')
                        continue
                    print(a, b, c, 'Yes', x1, x2, )


if __name__ == "__main__":
    main()
