import unittest
from typing import List
from unittest.mock import patch

from core.actions import (add_book_action, remove_book_action,
                          search_book_action, show_books_action,
                          update_status_action)
from core.models import Book


class TestActions(unittest.TestCase):
    def setUp(self):
        """Инициализация списка книг для тестов."""
        self.books: List[Book] = [
            Book(book_id=1, title="Book One", author="Author A", year=2001),
            Book(book_id=2, title="Book Two", author="Author B", year=2002),
        ]

    @patch("builtins.input", side_effect=["Test Title", "Test Author", "2023"])
    def test_add_book_action(self, mock_input):
        """Тест добавления книги."""
        with patch("builtins.print") as mock_print:
            add_book_action(self.books)
        self.assertEqual(len(self.books), 3)
        self.assertEqual(self.books[-1].title, "Test Title")
        self.assertEqual(self.books[-1].author, "Test Author")
        self.assertEqual(self.books[-1].year, 2023)
        mock_print.assert_called_with("Книга успешно добавлена.")

    @patch("builtins.input", side_effect=["1"])
    def test_remove_book_action(self, mock_input):
        """Тест удаления книги."""
        with patch("builtins.print") as mock_print:
            remove_book_action(self.books)
        self.assertEqual(len(self.books), 1)
        self.assertFalse(any(book.book_id == 1 for book in self.books))
        mock_print.assert_called_with("Книга успешно удалена.")

    @patch("builtins.input", side_effect=["title", "Book"])
    def test_search_book_action(self, mock_input):
        """Тест поиска книг."""
        with patch("builtins.print") as mock_print:
            search_book_action(self.books)
        mock_print.assert_any_call("Найдены следующие книги:")
        mock_print.assert_any_call(self.books[0].to_dict())

    def test_show_books_action(self):
        """Тест отображения всех книг."""
        with patch("builtins.print") as mock_print:
            show_books_action(self.books)
        mock_print.assert_any_call("Список всех книг:")
        for book in self.books:
            mock_print.assert_any_call(book)

    @patch("builtins.input", side_effect=["1", "выдана"])
    def test_update_status_action(self, mock_input):
        """Тест изменения статуса книги."""
        with patch("builtins.print") as mock_print:
            update_status_action(self.books)
        self.assertEqual(self.books[0].status, "выдана")
        mock_print.assert_called_with("Статус книги успешно обновлён.")


if __name__ == "__main__":
    unittest.main()
