import os
import tempfile
import unittest

from core.models import Book
from core.utils import add_book, remove_book, search_books, update_book_status


class TestUtils(unittest.TestCase):
    def setUp(self):
        """Настройка перед каждым тестом."""
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8")
        self.temp_file.close()
        self.books = [
            Book(1, "Программирование на Python", "Иван Иванов", 2022, "в наличии"),
            Book(2, "Алгоритмы и структуры данных", "Джон Доу", 2021, "выдана"),
        ]
        self.file_path = self.temp_file.name

    def tearDown(self):
        """Удаление временных файлов после тестов."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_add_book(self):
        """Тест добавления новой книги."""
        add_book(self.books, "Машинное обучение", "Анна Каренина", 2023)
        self.assertEqual(len(self.books), 3)
        self.assertEqual(self.books[-1].title, "Машинное обучение")

    def test_remove_book(self):
        """Тест удаления книги по ID."""
        result = remove_book(self.books, 1)
        self.assertTrue(result)
        self.assertEqual(len(self.books), 1)
        self.assertNotIn(1, [book.book_id for book in self.books])

    def test_remove_book_invalid_id(self):
        """Тест удаления несуществующей книги."""
        result = remove_book(self.books, 999)
        self.assertFalse(result)

    def test_search_books(self):
        """Тест поиска книг."""
        results = search_books(self.books, "Python", "title")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Программирование на Python")

    def test_update_book_status(self):
        """Тест обновления статуса книги."""
        result = update_book_status(self.books, 2, "в наличии")
        self.assertTrue(result)
        self.assertEqual(self.books[1].status, "в наличии")

    def test_update_book_status_invalid_id(self):
        """Тест обновления статуса несуществующей книги."""
        result = update_book_status(self.books, 999, "в наличии")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
