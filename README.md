# qa_python
## 1. Тестирование добавления книг
-  test_add_new_book_valid_length - проверяет добавление книг с корректной длиной (1-40 символов)
-  test_add_new_book_not_valid_length - проверяет невозможность добавления книг с некорректной длиной (0 или 41 символ)

## 2. Тестирование работы с жанрами
-  test_set_book_genre_add_genre - проверяет установку жанра для книги
-  test_get_book_genre_get_genre - проверяет получение жанра книги
- ` est_get_books_genre_get_books_genre - проверяет получение всего словаря книг и жанров

## 3. Тестирование фильтрации книг по жанру
-  test_get_books_with_specific_genre_valid_genre - проверяет получение книг по конкретному жанру
-  test_get_books_with_specific_genre_not_valid_genre - проверяет отсутствие книги при фильтрации по другому жанру

## 4. Тестирование детской подборки книг
-  test_get_books_for_children_not_valid_genre - проверяет исключение взрослых жанров (Ужасы, Детективы)

## 5. Тестирование избранных книг
- test_add_book_in_favorites_add_favorites - проверяет добавление книги в избранное
- test_delete_book_from_favorites_delete_book - проверяет удаление книги из избранного
- test_get_list_of_favorites_books_get_favorites - проверяет получение списка избранных книг
