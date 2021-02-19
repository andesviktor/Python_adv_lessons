class Book:
    """ Класс книги """

    def __init__(self, name: str, author: str, year: int, available: bool = True, reader: str = "None"):
        """
        Create new book
        :param name: Book Name
        :param author: Books' Author
        :param year: Year of the book
        :param available: Is this book available. Default - True
        """
        self.name = name
        self.author = author
        self.year = year
        self.available = available
        self.reader = reader
