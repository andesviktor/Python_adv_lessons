class Book:
    """ Класс книги """
    def __init__(self, id: int, name: str, author: str, year: int):
        """
        Создание книги
        :param id: ID книги
        :param name: Название книги
        :param author: Автор книги
        :param year: Год выпуска
        """
        self.id = id
        self.name = name
        self.author = author
        self.year = year

    def remove_book_to_library(self, id: int, name: str, author: str, year: int):
        print(f'Book removed: {id} : \'{name}\' by {author} , {year}')
