import json
import os
import tempfile
from typing import List

from models import Book

FILE_PATH = "data/books.json"


def load_books() -> List[Book]:
    """
    Загружает книги из JSON-файла.
    """
    try:
        with open(FILE_PATH, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
            return [Book.from_dict(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_books(books: List[Book]) -> None:
    """
    Сохраняет список книг в JSON-файл.
    """
    if not all(isinstance(book, Book) for book in books):
        raise ValueError("Все элементы в списке должны быть экземплярами класса Book.")

    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
    try:
        with temp_file as f:
            json.dump([book.to_dict() for book in books], f, ensure_ascii=False, indent=4)
        os.replace(temp_file.name, FILE_PATH)
    except Exception as e:
        os.remove(temp_file.name)
        print(f"При сохранении книг произошла ошибка: {e}")


def add_book(books: List[Book], title: str, author: str, year: int) -> None:
    """
    Добавляет новую книгу в список.

    :param books: Список существующих книг.
    :param title: Название книги.
    :param author: Автор книги.
    :param year: Год издания.
    """
    new_id = max([book.book_id for book in books], default=0) + 1
    books.append(Book(new_id, title, author, year))


def remove_book(books: List[Book], book_id: int) -> bool:
    """
    Удаляет книгу по ID.

    :param books: Список существующих книг.
    :param book_id: ID книги для удаления.
    :return: True, если книга успешно удалена, иначе False.
    """
    for book in books:
        if book.book_id == book_id:
            books.remove(book)
            return True
    return False


def search_books(books: List[Book], query: str, field: str) -> List[Book]:
    """
    Ищет книги по указанному полю.

    :param books: Список книг.
    :param query: Запрос для поиска.
    :param field: Поле для поиска (title, author, year).
    :return: Список найденных книг.
    """
    field_map = {"title": "title", "author": "author", "year": "year"}
    return [book for book in books if query.lower() in str(getattr(book, field_map[field], "")).lower()]


def update_book_status(books: List[Book], book_id: int, status: str) -> bool:
    """
    Изменяет статус книги.

    :param books: Список книг.
    :param book_id: ID книги.
    :param status: Новый статус ("в наличии" или "выдана").
    :return: True, если статус успешно изменён, иначе False.
    """
    for book in books:
        if book.book_id == book_id:
            book.status = status
            return True
    return False


def validate_non_empty(prompt: str) -> str:
    """
    Проверяет, что пользователь ввёл непустую строку.

    :param prompt: Сообщение для ввода.
    :return: Валидированная строка.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Ошибка: значение не может быть пустым. Попробуйте ещё раз.")


def validate_integer(prompt: str) -> int:
    """
    Проверяет, что пользователь ввёл целое число.

    :param prompt: Сообщение для ввода.
    :return: Валидированное целое число.
    """
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Ошибка: введите корректное число.")


def validate_choice(prompt: str, choices: list[str]) -> str:
    """
    Проверяет, что пользователь выбрал значение из предложенных.

    :param prompt: Сообщение для ввода.
    :param choices: Список допустимых значений.
    :return: Выбранное значение.
    """
    choices_str = "/".join(choices)
    while True:
        value = input(f"{prompt} ({choices_str}): ").strip().lower()
        if value in choices:
            return value
        print(f"Ошибка: введите одно из следующих значений: {choices_str}.")
