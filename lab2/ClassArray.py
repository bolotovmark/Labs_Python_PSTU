import random


class IntArray:
    arr = []

    def __init__(self):
        self.arr = []

    def diapason(self, a, b):
        for i in range(a, b+1):
            self.arr.append(i)

    def random(self, n):
        for i in range(n):
            self.arr.append(random.randint(0, 100))

    def show_arr(self):
        print("[ ")
        for temp in self.arr:
            print(temp + " ")

    def __del__(self):
        print("Массив очищен!")