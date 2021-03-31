"""
Task3
Напишіть тести до модуля реєстрації юзера (без фласк АРІ, просто окремий клас)
тести повинні перевіряти чи відповідає пароль пошта і ім'я вимогам,
перевіряти чи юзера з таким іменем не має в базі
якщо юзер створений то назад отримуємо строку "200", інакше модуль реєстрації кидатиме ексепшини
 (ексепшини потрібно написати свої)

тести до модуля авторизації юзера
метод авторизації отримує пошту і пароль і звіряє чи є такі в базі данних (за бд можете використати словник)
якщо дані введені вірно і юзер існує то назад повертаєтсья обєкт класу UserToken (майже пустий клас,
містить тільки аргумент строку яка задається рандомним набором символів)

Після написання тестів, реалізуйте ваші методи реєстрації і авторизаії
"""
import uuid


class ErrorName(Exception):
    pass


class EmailError(Exception):
    pass


class LengthEmailError(Exception):
    pass


class PasswordError(Exception):
    pass


class UserAlreadyRegistered(Exception):
    pass


class ErrorLogIn(Exception):
    pass


class UserToken:
    def __init__(self):
        self.__id = uuid.uuid4()

    def __str__(self):
        return self.__id


class Registration:
    user_database = {}
    user_token = UserToken()

    invalid_symbols = " ,:;!?/|\\#$%^&*'-+=(){}[]<>`~_"

    def register(self, name: str, email: str, password: str):

        if self.check_name(name) is False:
            raise ErrorName("Invalid name")

        if self.check_item_email(email) is False:
            raise EmailError("Invalid email")

        if self.check_length_email(email) is False:
            raise LengthEmailError("Invalid email length")

        if email in self.user_database.keys():
            raise UserAlreadyRegistered("This e-mail is already registered")

        if self.check_password(password) is False:
            raise PasswordError("Invalid password")

        else:
            self.user_database.update({email: password})
        print(self.user_database)
        return 200

    def login_in(self, email: str, password: str):
        if email in self.user_database and password in self.user_database.values():
            return self.user_token
        else:
            raise ErrorLogIn('Invalid login or password')

    def check_name(self, name):
        for i in name:
            if i in self.invalid_symbols:
                return False

    def check_item_email(self, email):
        for i in email:
            if i in self.invalid_symbols:
                return False

    def check_length_email(self, email):
        if 12 <= len(email) <= 30:
            return True
        else:
            return False

    def check_password(self, password):
        for i in password:
            if i in self.invalid_symbols:
                return False


user = Registration()
user.register("Jacob", "jacob@gmail.com", "123qwe")
user.login_in("jacob@gmail.com", "123qwe")

