from task1_class_Book import BOOKS_DATABASE, Book

class Library():
    """Класс для работы с библиотекой"""
    def __init__(self, books=None):  # по умолчанию пустая библиотека
        """Метод-конструктор

        Keyword argument:
        books -- список книг

        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):  # получить идентификатор последней книги, увеличенный на 1
        """Метод, возвращающий идентификатор для добавления новой книги в библиотеку"""
        if len(self.books) == 0:  # если библиотека пустая, выводится 1
            return 1
        else:  # если в библиотеке есть книги, выводится идентификатор последней книги, увеличенный на 1
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_): # вывод индекса книги по запрашиваемому идентификатору
        """Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса

        Keyword argument:
        id_ -- идентификатор запрашиваемой книги

        """
        for index, book in enumerate(self.books):
            if book.id_ == id_:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
