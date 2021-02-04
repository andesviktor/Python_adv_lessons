from collections import UserDict,UserList,UserString

class Book:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# class Lib:
#     def __init__(self):
#         self.listBook = []
#
#     def add_book(self, obj_book: Book):
        # for book in self.listBook:
        #     if obj_book.id == book.id:
        #         raise Exception('id exist')
        # if obj_book.id in [book.id for book in self.listBook]:
        #     raise Exception

        self.listBook.append(obj_book)

class Lib(dict):
    def __init__(self):
        super().__init__()

        self['books'] = {}

lib= Lib()

print(lib.keys())