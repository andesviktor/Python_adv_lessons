from reader import Reader
from book import Book
from library import Library
import time


def main():
    lib = Library()
    user1 = Reader("Djinn", "Co", 25)
    user2 = Reader("Artem", "KFC", 48)
    user3 = Reader("Suga", "Rogue", 35)

    book1 = Book("Ubik", "Philip k. Dick", 1969)
    book2 = Book("The Last Wish", "Andrzej Sapkowski", 2007)
    book3 = Book("It", "Stephen King", 1986)
    print(' ')
    lib.add_book_to_lib(book1)
    lib.add_book_to_lib(book2)
    lib.add_book_to_lib(book3)
    print(' ')
    lib.add_user_to_readerslist(user1)
    lib.add_user_to_readerslist(user2)
    lib.add_user_to_readerslist(user3)
    print(' ')

    time.sleep(3)
    lib.give_book_to_user(user1, book1)
    lib.give_book_to_user(user3, book1)
    time.sleep(3)
    print(' ')
    lib.show_books(available=True)
    print(' ')
    lib.show_books(available=False)
    print(' ')
    lib.sort_books('year')


if __name__ == "__main__":
    main()
