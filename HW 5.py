# 1.
# class Laptop:
#     """
#     Make the class with composition.
#     """
# class Battery:
#     """
#     Make the class with composition.
#     """

class Laptop:
    def __init__(self, name, capacity):
        self.name = name
        self.battery = Battery(capacity)

    def __str__(self):
        return f"Battery's capacity in {self.name} is {self.battery}"


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

    def __str__(self):
        return f'{self.capacity}'


laptop = Laptop('Lenovo', 55)
print(laptop)

# 2.
# class Guitar:
#     """
#     Make the class with aggregation
#     """
# class GuitarString:
#     """
#     Make the class with aggregation
#     """


class Guitar:
    def __init__(self, strings):
        self.strings = strings

    def __str__(self):
        return f'{self.strings}'


class GuitarString:
    def __init__(self):
        pass


strings = GuitarString()
guitar = Guitar(strings)


# 3
# class Calc:
#     """
#     Make class with one method "add_nums" with 3 parameters,
#     which returns sum of these parameters.
#     Note: this method should not take instance as first parameter.
#     """


class Calc:
    @staticmethod
    def add_nums(a, b, c):
        return a + b + c


print(Calc.add_nums(5, 7, 9))

# 4*.
# class Pasta:
#     """
#     Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
#     It should have 2 methods:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#     """


class Pasta:
    def __init__(self, ingridients):
        self.ingridients = ingridients

    @classmethod
    def carbonara(cls):
        return Pasta(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(['forcemeat', 'tomatoes'])
pasta_2 = Pasta.bolognaise()
print(pasta_1.ingridients)
print(pasta_2.ingridients)

# 5*.
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """


class Concert:
    max_visitor_num = 0

    def __init__(self, visitors_count=0):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, visitors):
        if visitors < self.max_visitor_num:
            self._visitors_count = visitors
        else:
            self._visitors_count = self.max_visitor_num


Concert.max_visitor_num = 100
concert = Concert()
concert.visitors_count = 500
print(concert.visitors_count)

# 6.
# class AddressBookDataClass:
#     """
#     Create dataclass with 7 fields - key (int), name (str), phone_number (str),
#     address (str), email (str), birthday (str), age (int)
#     """
import dataclasses


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


person = AddressBookDataClass(3, 'Jacob', '12345', 'Summer Str.', 'jacob.l@mail.com', '06.02.1991', 30)
print(person)

# 7. Create the same class (6) but using NamedTuple
import collections

AddressBookDataClass = collections.namedtuple('AdBook', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])
adbook = AddressBookDataClass(3, 'Jacob', '12345', 'Summer Str.', 'jacob.l@mail.com', '06.02.1991', 30)
print(adbook)

# 8.
# class AddressBook:
#     """
#     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.
#     """


class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook(key = {self.key}, name = {self.name}, phone_number = {self.phone_number}, ' \
               f'address = {self.address}, email = {self.email}, birthday = {self.birthday}, age = {self.age})'


adbook1 = AddressBook(3, 'Jacob', '12345', 'Summer Str.', 'jacob.l@mail.com', '06.02.1991', 30)
print(adbook1)

# 9.
# class Person:
#     """
#     Change the value of the age property of the person object
#     """
#     name = "John"
#     age = 36
#     country = "USA"


class Person:
    name = "John"
    age = 36
    country = "USA"


person = Person()
person.age = 37
print(person.age)

# 10.
# class Student:
#     """
#     Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
#     """
#     id = 0
#     name = ""
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name


class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(123, 'Lucas')
setattr(student, 'email', 'lucas@mail.com')
student.email = 'jl@mail.com'
student_email = getattr(student, 'email')
print(student_email)

# 11*.
# class Celsius:
#     """
#     By using @property convert the celsius to fahrenheit
#     Hint: (temperature * 1.8) + 32)
#     """
#     def __init__(self, temperature=0):
#         self._temperature = temperature
#
#
# # create an object
# {obj} = ...
#
# print({obj}.temperature)


class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return (self._temperature * 1.8) + 32


t = Celsius(36)
print(t.temperature)


