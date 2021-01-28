# try:
#     num = input()
#     print(type(num))

#     print(int(num) / 0)

# except ValueError:
#     print('Вы ввели не число')

# finally:
#     print('FINALLY!')

# import math
# #from random import randint
# from my_package_1 import test_1
# test_1.test()
# from random import randint as rI
# from my_module_1 import my_pi
# print(rI(0,10))
# print(my_pi)

# i=5
# while True:
#     print(i)
#     i += 2

# print(i)

# l = [1,2,3,5,9,10,15]
# for i in l:
#     print(i, end=' ')

# l = [1,2,3,5,9,10,15]
# for i in range(len(l)):
#     print(f'{i} - {l[i]}')

# for s in 'Hello world!':
#     if s == 'a':
#         print('a - exist')
#         break
# else:
#     print('a - not exist')

# if 'a' in 'Hello ward!':
#     print('a - exist')
# else:
#     print('a - not exist')

"""
1 - цикл завершился естественным путем
2 - break

3 - exit()
4 - exception
"""

# def test():
#     print('asshole')

# s = [1, 1.1, 'str','s',[1,2,3], test]

# for i in range(len(s)):
#     print(s[i])

# Генератор списков
# s = []

# for i in range(10):
#     if i % 2 == 1:
#         s.append(i)

# print(s)

# s2 = [i for i in range(10) if i % 2 == 1]
# print(s2)

#a = (1,1,3,4,5,6) #кортеж
#b = [1,1,3,4,5,6] #список

# a = 5
# b = 6
# a, b = b,a
# print(a)
# print(b)
# l = [i+1 for i in range(10)]
# for indx, elem in enumerate(l):
#     print(f'{indx} — {elem}')

# l = [1,1,2,5,2,3,6,7,6,65,4]
# l = sorted(set(l))
# print(l)

# user = {'name':'Ivan',
#         'age':20,
#         'hob':['football','code','python']}
# print(user['name'])
# for i in user:
#     print(i, end='; ')
# print()

# for i in user.keys:
#     print(i, end='; ')
# print()


#def test(*args, **kwargs):