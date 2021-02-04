# """Это докстринг модуля, он однострочный"""
#
# def function(a,b,c):
#     """
#
#     :param a:
#     :param b:
#     :param c:
#     :return:
#     """
#     pass
#
# class UselessClass(object):
#     """Это класс с докстрингом"""
#
#     def method_of_class(self):
#         """А это метод с докстрингом"""

# from datetime import date
#
#
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # метод экземляра класс
#     def get_full_info(self):
#         return f'Name: {self.name}; Age: {self.age}'
#
#     # метод класса
#     @classmethod
#     def from_birth_year(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     # Note: Верхний def равносильно нижнему
#     def copy(self):
#         return self.__class__(self.name, self.age)
#
#     @staticmethod
#     def get_birth_year(age):
#         return date.today() - age
#
#
# user = User('Van', 25)
#
# print(user.get_full_info())
#
# user_2 = user.from_birth_year('Petr', 1990)
# print(user_2.get_full_info())
#
# print(User.get_birth_year)

# d = dict.fromkeys("HELLO")
# print(d)

# Note Динамическое создание классов
# a = 5
# print(type(a))

# def choose_class(name):
#     if name == 'A':
#         class A:
#             pass
#         return A
#     else:
#         class B:
#             pass
#         return B
#
# my_class = choose_class(input())
# print(my_class)

# class User0:
#     value = 1
# print(User0.value)
#
#
# '''
# type( <class name>,
# <tuple - родительские класса>,
# <dict - поля>
# '''
#
# User = type('User', (), {'value': 1})
# print(User.value)

# def upper_attr(class_name,class_parent,class_attrs):
#     up_attr = {}
#     for name,value in class_attrs.items():
#         if not name.startswith('__'):
#             up_attr[name.upper()] = value
#         else:
#             up_attr[name] = value
#     return type(class_name,class_parent,up_attr)

# Note: Метакласс

# class UpAttrClass(type):
#     def __new__(cls, class_name, class_parent, class_attrs):
#         up_attr = {}
#         for name, value in class_attrs.items():
#             if not name.startswith('__'):
#                 up_attr[name.upper()] = value
#             else:
#                 up_attr[name] = value
#
#         up_attr['print_type'] = cls.print_type
#
#         # return type.__new__(cls, class_name,class_parent, up_attr)
#         return super(UpAttrClass, cls).__new__(cls, class_name, class_parent, up_attr)
#
#     def print_type(self):
#         print(type(self))
#
#
# class User(metaclass=UpAttrClass):
#     name = 'Ivan'
#     age = 20
#
#
# user_1 = User()
# print(dir(user_1))
# user_1.print_type()

# Note: Декораторы класса
# class Functor:
#     def __call__(selfs,a,b):
#         print (a + b)
# f = Functor()
#
# f(1,2)

# class Functor:
#     def __init__(self,N):
#         self.n = N
#     def call1(self,func,*args,**kwargs):
#         for i in range(3):
#             func(*args,**kwargs)
#     def call2(self, func,*args,**kwargs):
#         func(*args, **kwargs)
#     def test(self):
#         print('This is test...')
#     def __call__(self, func):
#         def helper(*args,**kwargs):
#             if self.n == 1:
#                 return self.call1(func,*args,**kwargs)
#             elif self.n == 2:
#                 return self.call2(func,*args,**kwargs)
#         return helper
# @Functor(1)
# def foo():
#     print('Hello')
# @Functor(2)
# def boo():
#     print('Bye')
# foo()
# boo()

from time import time, sleep


def benchmark(method):
    def helper(*args, **kwargs):
        time_start = time()
        res = method(*args, **kwargs)
        print(f'Time process:{time() - time_start} sec.')
        return res

    return helper()


def decor_benchmark_methods(cls):
    class NewClass:
        def __init__(self, *args, **kwargs):
            self.__obj = cls(*args, **kwargs)

        def __getattribute__(self, item):
            # Проверяем чей объект. Если наш, просто возвращаем его
            # если декорированного класа - модифицируем
            try:
                is_my_attr = super(NewClass, self).__getattribute__(item)
            except AttributeError:
                pass
            else:
                return is_my_attr

            # получаем атрибут
            attr = self.__obj.__getattribute__(item)

            # полученный атрибут - это поле или метод?
            if callable(attr):
                # если метод - модифицируем
                return benchmark(attr)
            else:
                # если поле - возвращаем
                return attr

    return NewClass


class Test:
    def method_1(self):
        print('Start method #1')
        sleep(1)
        print('Finished method #1')

    def method_2(self):
        print('Start method #2')
        sleep(1)
        print('Finished method #2')


Test = decor_benchmark_methods(Test)

t = Test()
t.method_1()
t.method_2()
print(type(t))
