from faker import Faker

class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """
    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных.
        """
        self.faker = faker

    def text(self) -> str:
        """
        Метод для генерации случайного текста.

        :return: Случайный текст.
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Метод для генерации случайного uuid4.

        :return: Случайный uuid4.
        """
        return self.faker.uuid4()

    def email(self) -> str:
        """
        Метод для генерации случайного email.

        :return: Случайный email.
        """
        return self.faker.email()

    def sentence(self) -> str:
        """
        Метод для генерации случайной строки текста.

        :return: Случайная строка текста.
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Метод для генерации случайного пароля.

        :return: Случайный пароль.
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Метод для генерации случайной фамилии.

        :return: Случайная фамилия.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Метод для генерации случайного имени.

        :return: Случайное имя.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Метод для генерации случайного отчества.

        :return: Случайное отчество.
        """
        return self.faker.first_name()

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Метод для генерации случайного целого числа. По умолчанию от 1 до 100

        :return: Случайное число.
        """
        return self.faker.random_int(start, end)

    def estimated_time(self) -> str:
        """
        Метод для генерации случайной строки со средним временем прохождения курса.

        :return: Случайная строка со средним временем прохождения курса.
        """
        return f"{self.integer(1, 10)} weeks"

    def max_score(self) -> int:
        """
        Метод для генерации случайного максимального балла в диапазоне 50-100.

        :return: Случайный максимальный балл.
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Метод для генерации случайного минимального балла в диапазоне 1-30.

        :return: Случайный минимальный балл.
        """
        return self.integer(1, 30)

fake = Fake(faker=Faker())