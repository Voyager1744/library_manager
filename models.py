class Book:
    """
    Модель книги.

    :param book_id: Уникальный идентификатор книги.
    :param title: Название книги.
    :param author: Автор книги.
    :param year: Год издания книги.
    :param status: Статус книги ("в наличии" или "выдана").
    """

    def __init__(
        self,
        book_id: int,
        title: str,
        author: str,
        year: int,
        status: str = "в наличии",
    ):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self) -> str:
        """
        Метод преобразования атрибутов объекта к строке.
        Returns:
            str: Строка, представляющая атрибуты объекта.
        """
        return f"{self.title}, {self.author}, {self.year}, {self.status}"

    def to_dict(self) -> dict:
        """
        Преобразует объект книги в словарь.
        """
        return self.__dict__

    @staticmethod
    def from_dict(data: dict) -> "Book":
        """
        Создаёт объект книги из словаря.
        """
        return Book(**data)
