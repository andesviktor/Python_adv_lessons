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

class UpAttrClass(type):
    def __new__(cls, class_name, class_parent, class_attrs):
        up_attr = {}
        for name, value in class_attrs.items():
            if not name.startswith('__'):
                up_attr[name.upper()] = value
            else:
                up_attr[name] = value

        up_attr['print_type'] = cls.print_type

        # return type.__new__(cls, class_name,class_parent, up_attr)
        return super(UpAttrClass, cls).__new__(cls, class_name, class_parent, up_attr)

    def print_type(self):
        print(type(self))


class User(metaclass=UpAttrClass):
    name = 'Ivan'
    age = 20


user_1 = User()
print(dir(user_1))
user_1.print_type()
