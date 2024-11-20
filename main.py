from utils import (add_book, load_books, remove_book, save_books, search_books,
                   update_book_status, validate_choice, validate_integer,
                   validate_non_empty)


def main():
    books = load_books()

    def add_book_action(books):
        title = validate_non_empty("Введите название книги: ")
        author = validate_non_empty("Введите автора книги: ")
        year = validate_integer("Введите год издания книги: ")
        add_book(books, title, author, year)
        print("Книга успешно добавлена.")

    def remove_book_action(books):
        if not books:
            print("Ошибка: библиотека пуста. Удаление невозможно.")
            return
        book_id = validate_integer("Введите ID книги для удаления: ")
        if remove_book(books, book_id):
            print("Книга успешно удалена.")
        else:
            print("Ошибка: книга с указанным ID не найдена.")

    def search_book_action(books):
        field = validate_choice("Выберите поле для поиска", ["title", "author", "year"])
        query = validate_non_empty("Введите запрос для поиска: ")
        results = search_books(books, query, field)
        if results:
            print("Найдены следующие книги:")
            for book in results:
                print(book.to_dict())
        else:
            print("Ничего не найдено.")

    def show_books_action(books):
        if books:
            print("Список всех книг:")
            for book in books:
                print(book.to_dict())
        else:
            print("Библиотека пуста.")

    def update_status_action(books):
        if not books:
            print("Ошибка: библиотека пуста. Изменение статуса невозможно.")
            return
        book_id = validate_integer("Введите ID книги: ")
        status = validate_choice("Введите новый статус", ["в наличии", "выдана"])
        if update_book_status(books, book_id, status):
            print("Статус книги успешно обновлён.")
        else:
            print("Ошибка: книга с указанным ID не найдена.")

    def save_books_action(books):
        try:
            save_books(books)
            print("Данные сохранены.")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")

    def exit_action(books):
        confirm_exit = validate_choice("Вы уверены, что хотите выйти? Все несохраненные изменения будут потеряны", ["да", "нет"])
        if confirm_exit == "да":
            save_books_action(books)
            print("Данные сохранены. Выход.")
            return True
        return False

    actions = {
        "1": add_book_action,
        "2": remove_book_action,
        "3": search_book_action,
        "4": show_books_action,
        "5": update_status_action,
        "6": save_books_action,
        "0": exit_action
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
