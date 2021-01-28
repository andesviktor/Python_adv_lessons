from abc import ABCMeta, abstractmethod


# Note: Классы

# class Reader:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         print('This is constructor Reader')

#     def print_full_name(self):
#         print(f'{self.name} {self.surname}')


# reader_1 = Reader('Ivan', 'Petrov', 30)
# # reader_1.print_self()  ## equal print(reader_1)
# reader_1.print_full_name()

# Note: Наследование

# class Vehicle(metaclass=ABCMeta):
#     def __init__(self, doors, tires, color):
#         print('Constructor Vehicle')
#         self.doors = doors
#         self.tires = tires
#         self.color = color
#
#     def brake(self):
#         print(f'{self.color} braking')
#
#     @abstractmethod
#     def drive(self):
#         pass
#
#
# class Car(Vehicle):
#     def drive(self):
#         print(f'Driving a {self.color} car')
#
#
# class Truck(Vehicle):
#     pass
#     # def drive(self):
#     #     print(f'Driving a {self.color} truck')
#
#
# car = Car(4, 4, 'red')
# car.drive()
# car.brake()
# print()
# car = Car(2, 6, 'black')
# car.drive()
# car.brake()

# Note: Полиморфизм
# print(1 + 1)
# print('1' + '1')


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         raise NotImplementedError
#
#
# class Cat(Animal):
#     def talk(self):
#         print('Meow!')
#
#
# class Dog(Animal):
#     def talk(self):
#         print('Woof!')
#
#
# def print_talk(animal):
#     animal.talk()
#
#
# animals = [
#     Cat('Miss'),
#     Dog('Far'),
#     Dog('Bar-Bar')
# ]
#
# for animal in animals:
#     animal.talk()
#
# print()
# print_talk(animals[1])

# Note:Магические методы
# class Reader:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # def __gt__(self, other):  #Note: Сравнения в большую сторону
#     #     return self.age > other.age

# def __lt__(self, other):  #Note: Сравнения в меньшую сторону
#     #     return self.age < other.age
#
# r_1 = Reader('Ivan', 20)
# r_2 = Reader('Petr', 15)
# print(r_1 > r_2)

# Note: Пример правильного комментирования
# def add(x1:int,x2:int) -> int:
#     """
#     Функция сложения двух чисел
#     :param x1: Первое число для сложения
#     :param x2: Второе число для сложения
#     :return: Сумма двух чисел
#     """
#     return x1+x2
# add()
