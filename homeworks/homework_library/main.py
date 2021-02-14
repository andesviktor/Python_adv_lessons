import json, os, time

from book import Book
from library import Library
from reader import Reader


def load_config_file(config):
    if config is None:
        return False

    if not os.path.exists(config):
        return False

    try:
        with open(config, 'r+') as json_file:
            config = json.load(json_file)
    except Exception as exc:
        print(repr(exc))
        return False

    return config


def write_json(config: str, y: dict):
    with open(config, 'r+') as file:
        data = json.load(file)
        data.append(y)
        json.dumps(data, file, indent=2)


def main_menu():
    time.sleep(1)
    books_list = load_config_file("books.json")
    persons_list = load_config_file("persons.json")
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
        main_menu()
    elif choice == 2:
        get_all_members(persons_list)
        main_menu()
    elif choice == 3:
        add_book_to_library(books_list)
        main_menu()
    elif choice == 4:
        delete_book_from_library()
        main_menu()
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


def add_book_to_library(books_list):
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
    if answer == 'y' or answer == 'Y':
        # TODO: Сделать for по book_id
        i = 0
        book_id_list = []
        for p in books_list:
            book_id_list.append(int(p['id']))
        book_id_list = sorted(book_id_list)
        i = 0
        for j in book_id_list:
            for i in range(0, i+1):
                if not i == book_id_list[j]:
                    book_id_list.append(j)
                    book_id_list = sorted(book_id_list)
                else:
                    i += 1
                    j += 1
        add_book = Book(book_id=book_id, book_name=book_name, book_author=book_author, book_year=book_year,
                        book_available=True)
        adding_book = {"id": add_book.book_id,
                       "name": add_book.book_name,
                       "author": add_book.book_author,
                       "year": add_book.book_year,
                       "available": add_book.book_available}
        write_json("books.json", adding_book)
    elif answer == 'n' or answer == 'N':
        print("Возвращаемся обратно в главное меню")
        time.sleep(2)
    else:
        print('Упс, вы сделали неправильный выбор. В качестве наказания за слепоту - повторите все еще раз')


def main():
    print("Добро пожаловать в админку библиотеку")
    main_menu()


if __name__ == "__main__":
    main()

print(Library.get_all_books())
print(Reader.print_full_name())
print(Book)
