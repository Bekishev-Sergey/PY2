BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    """Класс для работы с книгами"""

    def __init__(self, id, name, pages):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id}, name=\'{self.name}\', pages={self.pages})'


class Library():
    """Класс для работы с библиотекой"""

    def __init__(self, books="empty"):  # по умолчанию пустая библиотека
        self.books = books


    def get_next_book_id(self):  # получить идентификатор последней книги, увеличенный на 1

        if self.books == 'empty':  # если библиотека пустая, выводится 1
            return 1
        else:  # если в библиотеке есть книги, выводится идентификатор последней книги, увеличенный на 1
            counter = 1  # выводится идентификатор, увеличенный на 1, поэтому присваем счетчику значение 1
            for _ in enumerate(self.books, start=1):
                counter += 1
            return counter

    def get_index_by_book_id(self, id):  # вывод индекса книги по запрашиваемому идентификатору
        counter = 1
        for i in enumerate(self.books, start=1):
            counter += 1
        if counter - 1 < id or id < 1:  # проверка на существование запрашиваемой книги
            raise ValueError("Книги с запрашиваемым id не существует")
        else:
            return id - 1


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
