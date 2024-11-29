import json
import os
from typing import List

from core.models import Book


class BookManager:
    """Класс для управления коллекцией книг и операций с ними."""

    def __init__(self, file_path: str = "data/books.json"):
        """
        Инициализирует менеджер книг.

        :param file_path: Путь к JSON-файлу для хранения данных.
        """
        self.file_path = file_path
        self.books = self.load_books()

    def load_books(self) -> List[Book]:
        """Загружает книги из JSON-файла."""
        try:
            with open(self.file_path, "r", encoding="utf-8-sig") as f:
                data = json.load(f)
                return [Book.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            print("Файл с книгами не найден или повреждён. Загружен пустой список.")
            return []

    def save_books(self) -> None:
        """Сохраняет список книг в JSON-файл."""
        temp_file = f"{os.path.dirname(self.file_path)}/temp_books.json"
        try:
            with open(temp_file, "w", encoding="utf-8-sig") as f:
                json.dump(
                    [book.to_dict() for book in self.books],
                    f,
                    ensure_ascii=False,
                    indent=4,
                )
            os.replace(temp_file, self.file_path)
            print("Изменения успешно сохранены.")
        except Exception as e:
            if os.path.exists(temp_file):
                os.remove(temp_file)
            print(f"Ошибка при сохранении данных: {e}")

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавляет книгу в коллекцию."""
        new_id = max((book.book_id for book in self.books), default=0) + 1
        self.books.append(Book(new_id, title, author, year))
        print("Книга успешно добавлена.")

    def remove_book(self, book_id: int) -> bool:
        """Удаляет книгу по ID."""
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Книга успешно удалена.")
                return True
        print("Ошибка: книга с указанным ID не найдена.")
        return False

    def search_books(self, query: str, field: str) -> List[Book]:
        """Ищет книги по указанному полю."""
        field_map = {"title": "title", "author": "author", "year": "year"}
        results = [
            book
            for book in self.books
            if query.lower() in str(getattr(book, field_map.get(field, ""), "")).lower()
        ]
        if results:
            print("Найдены следующие книги:")
            for book in results:
                print(book.to_dict())
        else:
            print("Ничего не найдено.")
        return results

    def update_book_status(self, book_id: int, status: str) -> bool:
        """Изменяет статус книги."""
        for book in self.books:
            if book.book_id == book_id:
                book.status = status
                print("Статус книги успешно обновлён.")
                return True
        print("Ошибка: книга с указанным ID не найдена.")
        return False

    def show_books(self) -> None:
        """Выводит все книги из коллекции."""
        if self.books:
            print("Список всех книг:")
            for book in self.books:
                print(book)
        else:
            print("Библиотека пуста.")


def validate_non_empty(prompt: str) -> str:
    """Проверяет, что пользователь ввёл непустую строку."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Ошибка: значение не может быть пустым. Попробуйте ещё раз.")


def validate_integer(prompt: str) -> int:
    """Проверяет, что пользователь ввёл целое число."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Ошибка: введите корректное число.")


def validate_choice(prompt: str, choices: list[str]) -> str:
    """Проверяет, что пользователь выбрал значение из предложенных."""
    choices_str = "/".join(choices)
    while True:
        value = input(f"{prompt} ({choices_str}): ").strip().lower()
        if value in choices:
            return value
        print(f"Ошибка: введите одно из следующих значений: {choices_str}.")
