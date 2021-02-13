class Book:
    """ Класс книги и действий с ней """

    def __init__(self, book_id: int, book_name: str, book_author: str, book_year: int, book_available: bool):
        """
        :param book_id: ID книги
        :param book_name: Имя книги
        :param book_author: Автор книги
        :param book_year: Год выпуска книги
        :param book_available: Наличие книги
        """
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.book_year = book_year
        self.book_available = book_available