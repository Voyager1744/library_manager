from typing import List

from core.models import Book
from core.utils import (BookManager, validate_choice, validate_integer,
                        validate_non_empty)

manager = BookManager()


class Library:
    def __init__(self, books: List[Book] = None):
        """Инициализирует библиотеку."""
        self.books = books if books is not None else []

    def add_book(self) -> None:
        """Добавляет книгу в библиотеку."""
        title = validate_non_empty("Введите название книги: ")
        author = validate_non_empty("Введите автора книги: ")
        year = validate_integer("Введите год издания книги: ")
        manager.add_book(title, author, year)
        print("Книга успешно добавлена.")

    def remove_book(self) -> None:
        """Удаляет книгу из библиотеки."""
        if not self.books:
            print("Ошибка: библиотека пуста. Удаление невозможно.")
            return
        book_id = validate_integer("Введите ID книги для удаления: ")
        if manager.remove_book(book_id):
            print("Книга успешно удалена.")
        else:
            print("Ошибка: книга с указанным ID не найдена.")

    def search_book(self) -> None:
        """Поиск книги в библиотеке."""
        field = validate_choice("Выберите поле для поиска", ["title", "author", "year"])
        query = validate_non_empty("Введите запрос для поиска: ")
        results = manager.search_books(query, field)
        if results:
            print("Найдены следующие книги:")
            for book in results:
                print(book.to_dict())
        else:
            print("Ничего не найдено.")

    def show_books(self) -> None:
        """Выводит список всех книг."""
        if self.books:
            print("Список всех книг:")
            for book in self.books:
                print(book)
        else:
            print("Библиотека пуста.")

    def update_status(self) -> None:
        """Изменяет статус книги."""
        if not self.books:
            print("Ошибка: библиотека пуста. Изменение статуса невозможно.")
            return
        book_id = validate_integer("Введите ID книги: ")
        status = validate_choice("Введите новый статус", ["в наличии", "выдана"])
        if manager.update_book_status(book_id, status):
            print("Статус книги успешно обновлён.")
        else:
            print("Ошибка: книга с указанным ID не найдена.")

    def save_books(self) -> None:
        """Сохраняет изменения в библиотеке."""
        try:
            manager.save_books()
            print("Данные сохранены.")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")

    def exit(self) -> bool:
        """Выход из программы."""
        confirm_exit = validate_choice(
            "Вы уверены, что хотите выйти?",
            ["да", "нет"],
        )
        if confirm_exit == "да":
            manager.save_books()
            print("Данные сохранены. Выход.")
            return True
        return False
