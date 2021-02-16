# Note: Интерполяция строк

# from random import randint
# matrix = [[randint(0,200) for i in range(10)]for j in range(10)]
#
# for i in matrix:
#     for j in i:
#         print(f'{j:^5}', end='')
#     print()

# msg = 'C:\\Users\\andes\\AppData\\Local\\Programs\\Python\\Python38\\python.exe P:/Python/Python_adv_lessons/lessons/lesson_6/main.py'
#
# msg_len = f'{len(msg):5}'
#
# print(msg_len)
# print(len(msg_len))
# print(int(msg_len))

# Note: Шаблонные строки
# from string import Template
#
# t_hey_str = Template('Hey, $name')
# names = ['Ivan', 'Petr']
#
# for name in names:
#     print(t_hey_str.substitute(name=name))

# errno = 50159747054
# name = 'Iva'
# templ_string = 'Hi $name, there is an $error error $key!'
# args = {'name': name,
#         'error': hex(errno),
#         'key' : '=)'}
#
# print(Template(templ_string).substitute(args))

# Note: Работа из OS

# import os
# os.rename('test.txt', './folder_1/new_test.txt')
# print(os.listdir('./'))

# Note Работа с контекстным менеджером

# class Book:
#     def __init__(self,title,author,years):
#         self.title = title
#         self.author = author
#         self.years = years
#
#     def __repr__(self):
#         return f''
#
# with open('books.txt') as f:
#     for line in f:
#         list_data = line.strip().split(',')
#         print(Book)

# class Resource:
#     def __init__(self, name):
#         print(f'Resource: create {name}')
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def post_work(self):
#         print('Resource: closed!')
#
#
# class ResourceWith:
#     def __init__(self, name):
#         self.__obj = Resource(name)
#
#     def __enter__(self):
#         # do som..
#         return self.__obj
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_type)
#         print(exc_val)
#         print(exc_tb)
#
#         self.__obj.post_work()
#
#
# with ResourceWith('worker') as r:
#     print(5/0)
#     print(f'name: {r.get_name()}')

# Note: Контекст-менеджер
from contextlib import contextmanager

#@contextmanager
# def context():
#     print('Start')
#     print('Start context')
#
#     yield
#
#     print('Finished context!')
#
# with context():
#     print('do somth')

class Resource:
    def __init__(self, name):
        print(f'Resource: create {name}')
        self.__name = name
    def get_name(self):
        return self.__name
    def post_work(self):
        print('Resource: closed!')


@contextmanager
def ResourceWith(name):
    try:
        obj = Resource(name)
        yield obj
    except:
        pass
    finally:
        obj.post_work()

with ResourceWith('worker') as r:
    print(f'name:{r.get_name()}')