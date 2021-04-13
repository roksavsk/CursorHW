# 3. Use Pool.apply() to get the row wise common items in list_a and list_b.
# list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
# list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
from multiprocessing import Pool


def common_items():
    list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
    list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
    return [set(a).intersection(b) for a, b in zip(list_a, list_b)]


if __name__ == '__main__':
    with Pool() as pool:
        print(pool.apply(common_items))
