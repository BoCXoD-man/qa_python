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
        # Тут была ошибка, вместо assert len(collector.get_books_genre()) == 2 был assert len(collector.get_books_rating()) == 2, метода которого нет
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("book_name", [
        "1234567890123456789012345678901234567890",  # 40 символов
        "Книга",  # короткое имя
    ])
    def test_add_new_book_valid_name_book_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    def test_add_new_book_invalid_length_not_added(self):
        collector = BooksCollector()
        long_name = "А" * 41  # 41 символ — превышает лимит
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_set_book_genre_valid_book_and_genre_genre_set(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_set_book_genre_invalid_genre_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Романтика')
        assert collector.get_book_genre('Дюна') == ''

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна']

    def test_get_books_for_children_returns_only_safe_genre_books(self):
        collector = BooksCollector()
        collector.add_new_book('Маша и Медведь')
        collector.set_book_genre('Маша и Медведь', 'Мультфильмы')
        collector.add_new_book('Стивен Кинг')
        collector.set_book_genre('Стивен Кинг', 'Ужасы')
        assert collector.get_books_for_children() == ['Маша и Медведь']

    def test_add_book_in_favorites_adds_only_existing_books_once(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')  # Повторно
        assert collector.get_list_of_favorites_books() == ['Дюна']

    def test_add_book_in_favorites_ignores_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == []

    def test_get_books_genre_returns_full_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_genre() == {'Дюна': 'Фантастика'}