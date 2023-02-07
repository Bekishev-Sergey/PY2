class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        """Инкапсуляция name"""
        return self._name

    @property
    def author(self):
        """Инкапсуляция author"""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Бумажная книга"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает значение pages"""
        return self._pages

    @pages.setter
    def pages(self, new_pages) -> None:
        """Проверяет тип данных pages"""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типом int")
        self._pages = new_pages

    def __str__(self):
        tmp_str = super().__str__()
        return f"{tmp_str} Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """Аудиокнига"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        """Возвращает значение duration"""
        return self._duration

    @duration.setter
    def duration(self, check_duration) -> None:
        """Проверка типа данных duration"""
        if not isinstance(check_duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть типом float")
        self._duration = check_duration

    def __str__(self):
        tmp_str = super().__str__()
        return f"{tmp_str} Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

