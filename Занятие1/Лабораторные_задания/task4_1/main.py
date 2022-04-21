from itertools import count


def task():
    counter = count(100, 10)


    for i in range(1, 11):  # печатаем первые несколько элементов первого итератора строки
        print(next(counter))


if __name__ == "__main__":
    task()


