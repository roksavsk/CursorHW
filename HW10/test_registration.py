import unittest
from Registration import *


class TestRegistration(unittest.TestCase):
    def setUp(self) -> None:
        self.user = Registration()

    def test_register(self):
        with self.assertRaises(ErrorName):
            self.user.register("Yv*nne", "yvonne@gmail.com", "poiuyt098")
            self.user.register("Yv&nne?", "yvonne@gmail.com", "poiuyt098")
        self.user.register("Yvonne", "yvonne@gmail.com", "Poiuyt098")
        with self.assertRaises(EmailError):
            self.user.register("Estella", "estella_m@gmail.com", "zxcvb987")
            self.user.register("Estella", "estellam@@gmail.com", "zxcvb987")
        self.user.register("Estella", "estellam@gmail.com", "Zxcvb987")
        with self.assertRaises(LengthEmailError):
            self.user.register("Iris", "i@mail.com", "asdfg123")
            self.user.register("Iris", "ir@mail.com", "asdfg123")
        self.user.register("Iris", "iris@gmail.com", "Asdfg123")
        with self.assertRaises(UserAlreadyRegistered):
            self.user.register("Lucas", "jacob@gmail.com", "123qwerty")
            self.user.register("Lucas", "jacob@gmail.com", "zxcvb456")
        self.user.register("Lucas", "jacob2@gmail.com", "Zxcvb456")
        with self.assertRaises(PasswordLengthError):
            self.user.register("Grace", "grace@gmail.com", "qaz5")
        self.user.register("Grace", "grace@gmail.com", "Qazwsx579")
        with self.assertRaises(PasswordError):
            self.user.register("Quinn", "quinn@gmail.com", "qu!nn379")
            self.user.register("Quinn", "quinn@gmail.com", "qu!nn$%#379")
        self.assertEqual(self.user.register("Quinn", "quinn@gmail.com", "Quinn379"), 200)

    def test_login_in(self):
        with self.assertRaises(ErrorLogIn):
            self.user.login_in("jacob@gmail.com", "123qw")
            self.user.login_in("quinn@gmail.com", "123Qwerty")
        self.user.login_in("jacob@gmail.com", "123Qwerty")


    def tearDown(self) -> None:
        print("tearDown")
