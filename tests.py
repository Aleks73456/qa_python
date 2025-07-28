from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('length', [1, 40, 20, 39, 2])
    def test_add_new_book_valid_length(self, length):
        collector = BooksCollector()
        name = 'a' * length
        collector.add_new_book(name)
        assert name in collector.books_genre


    @pytest.mark.parametrize('length', [0, 41])
    def test_add_new_book_not_valid_length(self, length):
        collector = BooksCollector()
        name = 'a' * length
        collector.add_new_book(name)
        assert not name in collector.books_genre

    def test_set_book_genre_add_genre(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Ужасы')
        assert collector.books_genre[name] == "Ужасы"

    def test_get_book_genre_get_genre(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Ужасы')
        assert collector.get_book_genre(name) == 'Ужасы'

    @pytest.mark.parametrize('books', [{'книга 1':'Ужасы', 'книга 2': 'Ужасы', 'книга 3':'Мультфильмы'}])
    def test_get_books_with_specific_genre_valid_genre(self, books):
        collector = BooksCollector()
        for name, book_genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, book_genre)
        assert collector.get_books_with_specific_genre('Ужасы') == ['книга 1', 'книга 2']
        assert collector.get_books_with_specific_genre('Мультфильмы') == ['книга 3']
                                 
    def test_get_books_with_specific_genre_not_valid_genre(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Ужасы')
        assert not name in collector.get_books_with_specific_genre('Фантастика')                            
    
    def test_get_books_genre_get_books_genre(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    @pytest.mark.parametrize('books', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_not_valid_genre(self, books):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.set_book_genre(name, books)
        assert not name in collector.get_books_for_children()

    def test_add_book_in_favorites_add_favorites(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_book(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert not name in collector.get_list_of_favorites_books()
    
    def test_get_list_of_favorites_books_get_favorites(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
