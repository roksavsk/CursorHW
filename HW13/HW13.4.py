# 4. Divide the work between 2 methods: print_cube that returns the cube of number
# and print_square that returns the square of number.
# These two methods should be executed by using 2 different processes.
from concurrent.futures.process import ProcessPoolExecutor


def print_cube(x):
    print(x ** 3)


def print_square(x):
    print(x ** 4)


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(print_cube, 3)
        pool.submit(print_square, 3)
