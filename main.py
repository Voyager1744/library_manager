from core.actions import Library
from core.utils import (BookManager, validate_choice, validate_integer,
                        validate_non_empty)


def main() -> None:
    manager = BookManager()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Сохранить изменения")
        print("0. Выход")

        choice = validate_choice(
            "Выберите действие", ["1", "2", "3", "4", "5", "6", "0"]
        )

        if choice == "1":
            title = validate_non_empty("Введите название книги: ")
            author = validate_non_empty("Введите автора книги: ")
            year = validate_integer("Введите год издания книги: ")
            manager.add_book(title, author, year)
        elif choice == "2":
            book_id = validate_integer("Введите ID книги для удаления: ")
            manager.remove_book(book_id)
        elif choice == "3":
            field = validate_choice(
                "Выберите поле для поиска", ["title", "author", "year"]
            )
            query = validate_non_empty("Введите запрос для поиска: ")
            manager.search_books(query, field)
        elif choice == "4":
            manager.show_books()
        elif choice == "5":
            book_id = validate_integer("Введите ID книги: ")
            status = validate_choice("Введите новый статус", ["в наличии", "выдана"])
            manager.update_book_status(book_id, status)
        elif choice == "6":
            manager.save_books()
        elif choice == "0":
            print("Выход из программы.")
            break


if __name__ == "__main__":
    main()
