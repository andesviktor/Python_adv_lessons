import json
import time

from book import Book
from library import Library
from reader import Reader


def main_menu(books_list, persons_list):
    time.sleep(1)
    print("Чем могу вам помочь?")
    while True:
        try:
            print_main_menu()
            time.sleep(0.5)
            choice = int(input("Выбрать: "))
        except ValueError:
            print('ВНИМАНИЕ: не целое числовое значение или вообще не числовое значение. Повторите')
        else:
            break
    if choice == 1:
        get_all_books(books_list)
        main_menu(books_list, persons_list)
    elif choice == 2:
        get_all_members(persons_list)
        main_menu(books_list, persons_list)
    elif choice == 3:
        add_book_to_library()
        main_menu(books_list, persons_list)
    elif choice == 4:
        delete_book_from_library()
        main_menu(books_list, persons_list)
    else:
        print('Хорошего дня!')


def print_main_menu():
    """ Печатать главное меню админки """
    print("1. Список книг")
    print("2. Список читателей")
    print("3. Добавить книгу в базу")
    print("4. Удалить книгу из базы")
    print("5. Отдать книгу читателю")
    print("6. Принять книгу от читателя")
    print("7. Вывести список всех книг")
    print("8. Вывести список книг в определенном условии")
    print(" ")
    print("0.Выход")


def get_all_books(books_list):
    print("Список книг")
    print(" ")
    for p in books_list:
        print(f'ID: {p["id"]}')
        print(f'Book: \"{p["name"]}\" by {p["author"]}')
        if p["available"]:
            print("Available")
        elif not p["available"]:
            print("OUT OF STOCK")
        else:
            print("Something wrong with status")
        print(" ")


def get_all_members(persons_list):
    print("Список читателей")
    print(" ")
    for p in persons_list:
        print(f'ID: {p["id"]}')
        print(f'{p["name"]} {p["surname"]}')
        print("Owned books:")
        for j in p["owned_books"]:
            print(f'{j["id"]}: \"{j["name"]}\" by {j["author"]}')


def add_book_to_library():
    while True:
        try:
            book_name = input("Имя книги: ")
            book_author = str(input("Автор книги: "))
            book_year = int(input("Год выпуска книги: "))
        except ValueError:
            print("""
ВНИМАНИЕ: Вы ввели неправильные типы значений:
Автор книги - буквами
Год выпуска - цифрами
Повторите
 """)
        else:
            break
    answer = input(
        f"Вы точно хотите добавить книгу \"{book_name}\" за авторством {book_author} {book_year} года выпуска? Y or n: ")
    if answer == 'y':
        #TODO: Найти код из работы и сделать унифицированный JSON
        #TODO: Сделать for по book_id
        add_book = Book(book_id=5, book_name=book_name, book_author=book_author, book_year=book_year,
                        book_available=True)
        adding_book = {"id": add_book.book_id,
                       "name": add_book.book_name,
                       "author": add_book.book_author,
                       "year": add_book.book_year,
                       "available": add_book.book_available}
        with open('list.json', 'r+') as file:
            data = json.load(file)
            books_list = data['books']
            books_list.append(adding_book)
            file.seek(0)
            json.dump(data, file)
    elif answer == 'n':
        print("Возвращаемся обратно в главное меню")
        time.sleep(2)
    else:
        print('Упс, вы сделали неправильный выбор. В качестве наказания за слепоту - повторите все еще раз')


def main():
    with open('list.json') as infolist:
        data = json.load(infolist)
        books_list = data["books"]
        persons_list = data["persons"]
    print("Добро пожаловать в админку библиотеку")
    main_menu(books_list, persons_list)


if __name__ == "__main__":
    main()

print(Library.get_all_books())
print(Reader.print_full_name())
print(Book)
