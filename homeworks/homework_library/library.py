from book import Book
from reader import Reader


class Library:
    def __init__(self):
        """ Список людей и книг """
        with open('list.json') as infolist:
            data = json.load(infolist)
            self.books_list = data.books
            self.persons_list = data.persons

    def get_books_list(self):
        return self.books_list
