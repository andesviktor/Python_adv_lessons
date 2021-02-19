from book import Book
from reader import Reader


class Library:
    def __init__(self):
        self.books_list = []
        self.readers_list = []

    def add_book_to_lib(self, book: Book):
        """
        Add book to library
        :param book: Книга
        :return:
        """
        self.books_list.append(book)
        print(f'Book added: \'{book.name}\' by {book.author} , {book.year} — {book.available}')

    def del_book_from_lib(self, book: Book):
        """
        Remove book from library
        :param book:
        :return:
        """
        self.books_list.remove(book)
        print(f'Book deleted: \'{book.name}\' by {book.author} , {book.year}')

    def give_book_to_user(self, reader: Reader, book: Book):
        self.readers_list.append(reader)
        self.readers_list.append(book)
        for guestbooks in self.books_list:
            if book.name == guestbooks.name:
                if not book.available:
                    print("We can't give you this book because of absent")
                else:
                    print(f'Book \'{book.name}\' by {book.author} was given by {reader.name} {reader.surname} — {book.available}')
                    guestbooks.available = False
                    guestbooks.reader = f'{reader.name} {reader.surname}'

    def take_book_from_user(self, reader: Reader, book: Book):
        self.books_list.append(book)
        print(f' {reader.name} {reader.surname} give to library \'{book.name}\' by {book.author}')

    def show_books(self,available: bool = 'None'):
        for books in self.books_list:
            if books.available == available:
                if books.reader == 'None':
                    print(f"\'{books.name}\' by {books.author} , {books.year}")
                else:
                    print(f"\'{books.name}\' by {books.author} , {books.year}. Taken by {books.reader}")

    #def sort_books(self,):

