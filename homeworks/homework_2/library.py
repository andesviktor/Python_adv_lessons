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

    def add_user_to_readerslist(self, reader: Reader):
        """
        Add new user to Readlist
        :param reader: Reader
        :return:
        """
        self.readers_list.append(reader)
        print(f'User has been registered: {reader.name} {reader.surname}, {reader.age} years old')

    def remove_user_from_readerlist(self,reader:Reader):
        self.readers_list.remove(reader)
        print(f'User has been removed: {reader.name} {reader.surname}, {reader.age} years old')

    def give_book_to_user(self, reader: Reader, book: Book):
        """
        Give Book to Reader
        :param reader: Reader
        :param book: Book
        :return:
        """
        for guestbooks in self.books_list:
            if book.name == guestbooks.name:
                if not book.available:
                    print("We can't give you this book because of absent")
                else:
                    print(
                        f'Book \'{book.name}\' by {book.author} was given by {reader.name} {reader.surname} — {book.available}')
                    guestbooks.available = False
                    guestbooks.reader = f'{reader.name} {reader.surname}'

    def take_book_from_user(self, reader: Reader, book: Book):
        """
        Take Book from Reader
        :param reader: Reader
        :param book:  Book
        :return:
        """
        self.books_list.append(book)
        print(f' {reader.name} {reader.surname} give to library \'{book.name}\' by {book.author}')

    def show_books(self, available: bool = 'None'):
        """
        Show all books
        :param available: Show available(True),not available(False) or all books(default)
        :return:
        """
        for books in self.books_list:
            if books.available == available:
                if books.reader == 'None':
                    print(f"\'{books.name}\' by {books.author} , {books.year}")
                else:
                    print(f"\'{books.name}\' by {books.author} , {books.year} — WAS GIVEN TO {books.reader}")

    def sort_books(self, findkey = 'year'):
        """
        Sort books by 'name','author' or 'year'
        :param findkey: 'name','author' or 'year'(default)
        :return:
        """
        sorted_list = sorted(self.books_list, key=lambda sortedlist: sortedlist.__getattribute__(findkey))
        for b in sorted_list:
            if b.reader == 'None':
                print(f"\'{b.name}\' by {b.author} , {b.year}")
            else:
                print(f"\'{b.name}\' by {b.author} , {b.year} — WAS GIVEN TO {b.reader}")