import pytest

@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем книги из БД")

@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Создаем новые книги в БД")

@pytest.mark.usefixtures("clear_books_database", "fill_books_database")
class TestLibrary:
    def test_read_book_from_library(self):
        pass

    def test_delete_book_from_library(self):
        pass