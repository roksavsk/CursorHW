import unittest
from Registration import *


class TestRegistration(unittest.TestCase):
    def setUp(self) -> None:
        self.user = Registration()

    def test_register(self):
        with self.assertRaises(ErrorName):
            self.user.register("Yv*nne", "yvonne@gmail.com", "poi098")
        with self.assertRaises(EmailError):
            self.user.register("Estella", "estella_m@gmail.com", "zxcvb987")
        with self.assertRaises(LengthEmailError):
            self.user.register("Iris", "i@mail.com", "asd123")
        with self.assertRaises(UserAlreadyRegistered):
            self.user.register("Lucas", "jacob@gmail.com", "123qwe")
        with self.assertRaises(PasswordError):
            self.user.register("Quinn", "quinn@gmail.com", "qu!nn379")
        self.assertEqual(self.user.register("Estella", "estella@gmail.com", "zxc987"), 200)

    def test_login_in(self):
        with self.assertRaises(ErrorLogIn):
            self.user.login_in("jacob@gmail.com", "123qw")
        self.user.login_in("jacob@gmail.com", "123qwe")

    def tearDown(self) -> None:
        print("tearDown")
