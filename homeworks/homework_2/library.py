from book import Book
from reader import Reader


class Library:
    def __init__(self):
        self.books_list = []
        self.readers_list = []

    def add_book_to_lib(self, book: Book):
        self.books_list.append(book)
        print(f'Book added: {book.id} : \'{book.name}\' by {book.author} , {book.year}')

    # def remove_book_to_lib(self,book:Book):

    def give_book_to_user(self, reader: Reader, book: Book):
        self.readers_list.append(reader)
        self.readers_list.append(book)
        print(f'Book \'{book.name}\' by {book.author} was give to {reader.name} {reader.surname}')

    #def take_book_from_user(self,reader:Reader,book:Book):

