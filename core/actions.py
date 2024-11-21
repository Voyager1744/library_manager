from typing import List

from core.models import Book
from core.utils import (add_book, remove_book, save_books, search_books,
                        update_book_status, validate_choice, validate_integer,
                        validate_non_empty)


def add_book_action(books: List[Book]) -> None:
    """Добавляет книгу в библиотеку."""
    title = validate_non_empty("Введите название книги: ")
    author = validate_non_empty("Введите автора книги: ")
    year = validate_integer("Введите год издания книги: ")
    add_book(books, title, author, year)
    print("Книга успешно добавлена.")


def remove_book_action(books: List[Book]) -> None:
    """Удаляет книгу из библиотеки."""
    if not books:
        print("Ошибка: библиотека пуста. Удаление невозможно.")
        return
    book_id = validate_integer("Введите ID книги для удаления: ")
    if remove_book(books, book_id):
        print("Книга успешно удалена.")
    else:
        print("Ошибка: книга с указанным ID не найдена.")


def search_book_action(books: List[Book]) -> None:
    """Поиск книги в библиотеке."""
    field = validate_choice("Выберите поле для поиска", ["title", "author", "year"])
    query = validate_non_empty("Введите запрос для поиска: ")
    results = search_books(books, query, field)
    if results:
        print("Найдены следующие книги:")
        for book in results:
            print(book.to_dict())
    else:
        print("Ничего не найдено.")


def show_books_action(books: List[Book]) -> None:
    """Выводит список всех книг."""
    if books:
        print("Список всех книг:")
        for book in books:
            print(book)
    else:
        print("Библиотека пуста.")


def update_status_action(books: List[Book]) -> None:
    """Изменяет статус книги."""
    if not books:
        print("Ошибка: библиотека пуста. Изменение статуса невозможно.")
        return
    book_id = validate_integer("Введите ID книги: ")
    status = validate_choice("Введите новый статус", ["в наличии", "выдана"])
    if update_book_status(books, book_id, status):
        print("Статус книги успешно обновлён.")
    else:
        print("Ошибка: книга с указанным ID не найдена.")


def save_books_action(books: List[Book]) -> None:
    """Сохраняет изменения в библиотеке."""
    try:
        save_books(books)
        print("Данные сохранены.")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")


def exit_action(books: List[Book]) -> bool:
    """Выход из программы."""
    confirm_exit = validate_choice(
        "Вы уверены, что хотите выйти?",
        ["да", "нет"],
    )
    if confirm_exit == "да":
        save_books_action(books)
        print("Данные сохранены. Выход.")
        return True
    return False
