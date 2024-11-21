from core.actions import (add_book_action, exit_action, remove_book_action,
                          save_books_action, search_book_action,
                          show_books_action, update_status_action)
from core.utils import load_books


def main() -> None:
    books = load_books()

    actions = {
        "1": add_book_action,
        "2": remove_book_action,
        "3": search_book_action,
        "4": show_books_action,
        "5": update_status_action,
        "6": save_books_action,
        "0": exit_action,
    }

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Сохранить изменения")
        print("0. Выход")

        try:
            choice = input("Введите номер действия: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nОшибка: ввод был прерван. Попробуйте снова.")
            continue

        action = actions.get(choice)
        if action:
            if choice == "0":
                if action(books):
                    break
            else:
                action(books)
        else:
            print("Ошибка: неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
