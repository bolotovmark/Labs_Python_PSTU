import random
import statistics
import math
from gmpy2 import mpz


def series_sum():
    sum = ((0 + 999999) / 2) * (999999 + 1)
    print(sum)
    the_mean_series(sum)


def the_mean_series(sum):
    mean = sum / 2
    print(mean)


def median_product_arr():
    array = []
    for i in range(0, 1000000):
        array.append(random.randint(1, 10))
    print(statistics.median(array))
    print(mpz(math.prod(array)))


if __name__ == '__main__':
    series_sum()
    median_product_arr()
