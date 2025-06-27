# Тестирование BooksCollector

## Описание
Проект содержит класс `BooksCollector` и тесты для проверки всех его методов.

## Реализованные тесты:

- `test_add_new_book_valid_name_book_added` — добавление книг с корректными именами
- `test_add_new_book_invalid_length_not_added` — не добавляется книга с длиной > 40
- `test_set_book_genre_valid_book_and_genre_genre_set` — установка корректного жанра
- `test_set_book_genre_invalid_genre_genre_not_set` — игнорируется невалидный жанр
- `test_get_book_genre` — получение жанра книги
- `test_get_books_with_specific_genre_returns_correct_books` — выборка книг по жанру
- `test_get_books_for_children_returns_only_safe_genre_books` — только "безопасные" жанры
- `test_add_book_in_favorites_adds_only_existing_books_once` — добавление в избранное
- `test_delete_book_from_favorites_removes_book` — удаление из избранного
- `test_get_books_genre_returns_full_dict` — словарь жанров
- `test_get_list_of_favorites_books` — список избранного

## Как запустить

```bash
pytest -v
pytest --cov=main --cov-report=term-missing
```
## Требования

Python 3.11+
pytest
pytest-cov