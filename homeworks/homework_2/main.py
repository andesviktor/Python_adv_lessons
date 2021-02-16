from reader import Reader
from book import Book
from library import Library
import time

def main():
    user1 = Reader(0, "Djinn", "Co", 25)
    user2 = Reader(1, "Artem", "KFC", 48)
    user3 = Reader(2, "Suga", "Rogue", 35)

    book1 = Book(0, "Ubik", "Philip k. Dick", 1969)
    book2 = Book(1, "The Last Wish", "Andrzej Sapkowski", 2007)
    book3 = Book(2, "It", "Stephen King", 1986)
    lib = Library()
    print(' ')
    lib.add_book_to_lib(book1)
    lib.add_book_to_lib(book2)
    lib.add_book_to_lib(book3)
    print(' ')
    time.sleep(3)
    lib.give_book_to_user(user1,book1)
    lib.give_book_to_user(user3,book2)

if __name__ == "__main__":
    main()
