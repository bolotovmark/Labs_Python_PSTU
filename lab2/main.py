import time

from ClassArray import IntArray
import os
import json


def show_input_menu():
    print("[1] - Добавить в массив элемент с заданным диапазоном\n"
          "[2] - Добавить в массив элемент заполненный случайными числами\n"
          "[3] - Вывести все элементы\n"
          "[0] - Выход")


class Menu:
    mas = []

    def __init__(self):
        self.mas = []
        try:
            with open('json_data.json') as json_file:
                data = json.load(json_file)
            for temp in data['mas']:
                current = IntArray()
                self.mas.append(current)
                for num in temp['arr']:
                    current.json_to_class(num)
        except Exception as e:
            print(e)

    def tojson(self):
        dump = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        print(dump)
        with open('json_data.json', 'w') as outfile:
            outfile.write(str(dump))

    def show_array(self):
        i = 0
        for temp in self.mas:
            print("[" + str(i) + "] -", end='')
            temp.show_arr()
            i = i + 1
        print()

    def request_menu(self):

        show_input_menu()
        k = int(input("Выберите пункт: "))
        os.system('cls||clear')
        if k == 0:
            self.tojson()
            quit(0)
        elif k == 1:
            a = int(input("Введите границу диапозона: "))
            b = int(input("Введите границу диапазона: "))
            temp = IntArray()
            temp.diapason(a, b)
            self.mas.append(temp)
            print("Элемент добавлен")
        elif k == 2:
            n = int(input("Введите кол-во элементов: "))
            temp = IntArray()
            temp.random(n)
            self.mas.append(temp)
        elif k == 3:
            self.show_array()
        elif k == 4:
            self.show_array()
            d = input("Выберите номер удаляемого элемента: ")
            self.mas.pop(int(d))
        else:
            print("Неправильно введено значение")


if __name__ == '__main__':
    menu = Menu()
    while True:
        menu.request_menu()
