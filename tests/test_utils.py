import os
import tempfile
import unittest

from core.models import Book
from core.utils import BookManager


class TestUtils(unittest.TestCase):
    def setUp(self):
        """Настройка перед каждым тестом."""
        self.temp_file = tempfile.NamedTemporaryFile(
            delete=False, mode="w", encoding="utf-8"
        )
        self.temp_file.write("[]")
        self.temp_file.close()
        self.file_path = self.temp_file.name
        self.manager = BookManager(self.file_path)
        self.manager.books = [
            Book(1, "Программирование на Python", "Иван Иванов", 2022, "в наличии"),
            Book(2, "Алгоритмы и структуры данных", "Джон Доу", 2021, "выдана"),
        ]

    def tearDown(self):
        """Удаление временных файлов после тестов."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_add_book(self):
        """Тест добавления новой книги."""
        self.manager.add_book("Машинное обучение", "Анна Каренина", 2023)
        self.assertEqual(len(self.manager.books), 3)
        self.assertEqual(self.manager.books[-1].title, "Машинное обучение")

    def test_remove_book(self):
        """Тест удаления книги по ID."""
        result = self.manager.remove_book(1)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.books), 1)
        self.assertNotIn(1, [book.book_id for book in self.manager.books])

    def test_remove_book_invalid_id(self):
        """Тест удаления несуществующей книги."""
        result = self.manager.remove_book(999)
        self.assertFalse(result)

    def test_search_books(self):
        """Тест поиска книг."""
        results = self.manager.search_books("Python", "title")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Программирование на Python")

    def test_update_book_status(self):
        """Тест обновления статуса книги."""
        result = self.manager.update_book_status(2, "в наличии")
        self.assertTrue(result)
        self.assertEqual(self.manager.books[1].status, "в наличии")

    def test_update_book_status_invalid_id(self):
        """Тест обновления статуса несуществующей книги."""
        result = self.manager.update_book_status(999, "в наличии")
        self.assertFalse(result)

    def test_save_and_load_books(self):
        """Тест сохранения и загрузки книг."""
        self.manager.save_books()  # Сохраняем книги в файл
        new_manager = BookManager(self.file_path)  # Создаём новый менеджер
        new_manager.load_books()  # Загружаем книги из файла

        self.assertEqual(len(new_manager.books), len(self.manager.books))
        self.assertEqual(new_manager.books[0].title, "Программирование на Python")


if __name__ == "__main__":
    unittest.main()
