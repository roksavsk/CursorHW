from functools import wraps

# 1. double_result
# This decorator function should return the result of another function multiplied by two
def double_result(func):
    def inner(a, b):
        return func(a, b) * 2
    return inner


def add(a, b):
    return a + b


print(add(5, 5))  # 10


@double_result
def add(a, b):
    return a + b


print(add(5, 5))  # 20


# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise return the string "Please use only odd numbers!"

def only_odd_parameters(func):
    def inner(*args):
        for a in args:
            if a % 2 == 0:
                return "Please use only odd numbers!"
            else:
                return func(*args)
    return inner


@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5))  # 10
print(add(4, 4))  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print(multiply(1, 3, 5, 7, 9))
print(multiply(2, 3, 4, 5, 6))

# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):


def logged(func):
    @wraps(func)
    def log(*args, **kwargs):
        """
        Logging
        :param args:
        :param kwargs:
        :return:
        """
        return func(*args, **kwargs)
    return log


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


# you called func(4, 4, 4)
# it returned 6


# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.

def type_check(correct_type):
    def check(func):
        @wraps(func)
        def inner(a):
            if isinstance(a, correct_type):
                func(a)
            else:
                print(f"Wrong Type: {type(a).__name__}")
        return inner
    return check


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function