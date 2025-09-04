import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # создаем экземпляр (объект) класса BooksCollector
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_get_book_genre_no_genre_initially(self, collector):
        collector.add_new_book('Война и мир')
        assert collector.get_book_genre('Война и мир') == ''

    def test_set_book_genre_valid_genre(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_book_genre('1984') == 'Фантастика'

    def test_get_books_with_specific_genre_returns_correct_books(self, collector):
        collector.add_new_book('Оно')
        collector.add_new_book('Сияние')
        collector.add_new_book('Война и мир')

        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.set_book_genre('Война и мир', 'Фантастика')

        result = collector.get_books_with_specific_genre('Ужасы')

        assert 'Оно' in result and 'Сияние' in result and len(result) == 2

    def test_get_books_for_children_excludes_age_restricted(self, collector):
        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Король Лев')

        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Король Лев', 'Мультфильмы')

        result = collector.get_books_for_children()

        assert 'Гарри Поттер' in result and 'Король Лев' in result
        assert 'Оно' not in result and 'Шерлок Холмс' not in result

    def test_add_book_in_favorites_adds_once(self, collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')

        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Мастер и Маргарита']

    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.add_new_book('Преступление и наказание')
        collector.add_book_in_favorites('Преступление и наказание')

        collector.delete_book_from_favorites('Преступление и наказание')

        assert collector.get_list_of_favorites_books() == []

    def test_add_new_book_does_not_add_duplicates(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Гарри Поттер')

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_title_longer_than_40_is_ignored(self, collector):
        long_title = 'А' * 41
        collector.add_new_book(long_title)

        assert len(collector.get_books_genre()) == 0

    def test_get_books_genre_returns_full_dict(self, collector):
        collector.add_new_book('Три товарища')
        collector.add_new_book('Маленький принц')

        books = collector.get_books_genre()
        assert set(books.keys()) == {'Три товарища', 'Маленький принц'}

    def test_get_book_genre_returns_correct_genre(self, collector):
        collector.add_new_book('1984')
        collector.books_genre['1984'] = 'Фантастика'
        assert collector.get_book_genre('1984') == 'Фантастика'

    def test_get_list_of_favorites_books_returns_correct_list(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Шерлок Холмс')

        collector.add_book_in_favorites('Гарри Поттер')

        result = collector.get_list_of_favorites_books()
        assert result == ['Гарри Поттер']
