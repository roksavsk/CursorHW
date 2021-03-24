import logging

log_template = '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s'
logging.basicConfig(level=logging.DEBUG, filename="test.log", filemode="a", format=log_template)

operations = ['+', '-', '*', '/', '**', 'V', '%', 'end']


def operation(values):
    if values == '+':
        try:
            return sum(int(input('Enter num1: ')), int(input('Enter num2: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'Wrong  input, enter number'
    if values == '-':
        try:
            return subtraction(int(input('Enter num1: ')), int(input('Enter num2: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'Wrong  input, enter number'
    if values == '*':
        try:
            return multiplication(int(input('Enter num1: ')), int(input('Enter num2: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'Wrong  input, enter number'
    if values == '/':
        try:
            return division(int(input('Enter num1: ')), int(input('Enter num2: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'Wrong  input, enter number'
    if values == '**':
        try:
            return exponentiation(int(input('Enter num1: ')), int(input('Enter num2: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'Wrong  input, enter number'
    if values == 'V':
        try:
            return root_ext(int(input('Enter num1: ')), int(input('Enter root degree: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'Wrong  input, enter number'
    if values == '%':
        try:
            return percentage(int(input('Enter num1: ')), int(input('Enter percent: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'Wrong  input, enter number'


def sum(num1, num2):
    logging.info('Returns sum of two numbers')
    return f'Result: {num1} + {num2} = {num1 + num2}'


def subtraction(num1, num2):
    logging.info('Returns subtraction of two numbers')
    return f'Result: {num1} - {num2} = {num1 - num2}'


def multiplication(num1, num2):
    logging.info('Returns multiplication of two numbers')
    return f'Result: {num1} * {num2} = {num1 * num2}'


def division(num1, num2):
    try:
        logging.info('Returns division of two numbers')
        return f'Result: {num1} / {num2} = {num1 / num2}'
    except ZeroDivisionError:
        logging.error('ZeroDivisionError', exc_info=True)
        return 'You cannot divide by zero'


def exponentiation(num1, num2):
    logging.info('Returns exponentiation of two numbers')
    return f'Result: {num1} ** {num2} = {num1 ** num2}'


def root_ext(num1, num2):
    try:
        logging.info('Returns root extraction from number')
        return f'Result: {num1} ** (1/{num2}) = {num1 ** (1/num2)}'
    except ValueError:
        return 'Number cannot be negative'


def percentage(num1, percent):
    logging.info('Returns percentage of number')
    return f'Result: {percent}% from {num1} = {num1 * percent/100}'


while True:
    inputs = input(f'{operations} Select calculation: ')
    if inputs == 'end':
        logging.info('End calculation')
        print('End calculation')
        break
    if inputs in operations:
        print(operation(inputs))
    else:
        logging.warning('Wrong operation')
        print('This operation is not available')