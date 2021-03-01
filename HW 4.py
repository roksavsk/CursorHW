# 1. Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def vehicle_attributes(self):
        print(f'Vehicle max speed is {vehicle.max_speed} and mileage is {vehicle.mileage}.')


vehicle = Vehicle('100', '60')
vehicle.vehicle_attributes()

# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        self.seating_capacity = seating_capacity
        self.max_speed = max_speed
        self.mileage = mileage
        super().__init__(max_speed, mileage)

    def seating(self):
        print(f'Vehicle seating capacity is {self.seating_capacity}.')


bus = Bus('110','70', '20')
bus.vehicle_attributes()
bus.seating()

# 3. Determine which class a given Bus object belongs to (Check type of an object)

print(isinstance(bus, Vehicle))

# 4. Determine if School_bus is also an instance of the Vehicle class

class School_bus(Vehicle):
    pass

print(isinstance(School_bus, Vehicle))

# 5. Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_attributes(self):
        print(f'School {self.get_school_id} has {self.number_of_students} students.')


school = School('1', '900')
school.school_attributes()

# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own - bus_school_color

class SchoolBus(School, Bus):
    def __init__(self, get_school_id, number_of_students, max_speed, mileage, seating_capacity, bus_school_color):
        super().__init__(get_school_id, number_of_students)
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity
        self.bus_school_color = bus_school_color

    def bus_color(self):
        print(f'School bus color is {self.bus_school_color}.')


school_bus = SchoolBus('2','500','15', '120', '80', 'blue')
school_bus.school_attributes()
school_bus.vehicle_attributes()
school_bus.seating()
school_bus.bus_color()

# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.

class Bear:
    def __init__(self, make_sound):
        self.make_sound = make_sound

    def sound(self):
        print(f'Bear says {self.make_sound}.')

    def about(self):
        print(f'It is a bear.')

class Wolf:
    def __init__(self, make_sound):
        self.make_sound = make_sound

    def sound(self):
        print(f'Wolf says {self.make_sound}.')

    def about(self):
        print(f'It is a wolf.')


bear = Bear('Grrr')
wolf = Wolf('Awooo')

for animal in (bear, wolf):
    animal.sound()
    animal.about()

# Magic methods:
# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".
# 9. Override a printable string representation of the City class and return:
# The population of the city {name} is {population}

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        else:
            print('Your city is too small')

    def __str__(self):
        return f'The population of the city {self.name} is {self.population}'


city = City('Vasylkivka', 1300)
print(city)

city = City('Dnipro', 966400)
print(city)

# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*)
# the value which is greater than 10. And perform this add (+) of two instances.

class Count:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        if self.count > 10 or other.count > 10:
            total_count = self.count * other.count
        else:
            total_count = self.count + other.count
        return Count(total_count)

    def __str__(self):
        return f'Count: {self.count}'


c1 = Count(5)
c2 = Count(11)
c3 = c1 + c2
print(c3)

# 11. The __call__ method enables Python programmers to write classes where
# the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.

class Call:
    def __call__(self, a, b, c):
        d = a + b + c
        return d


call = Call()
print(call(25, 15, 10))

# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False

class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) > 0:
            return True
        else:
            return False


order1 = MyOrder(['a', 'b'], 'Connor')
order2 = MyOrder([], 'Nort')
print(bool(order1))
print(bool(order2))
