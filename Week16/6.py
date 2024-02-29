from random import randint, randrange
import time
import matplotlib.pyplot as plt


def binary_search(data: list[int], value: int) -> bool:
    while data:
        cursor = len(data) // 2
        if data[cursor] == value:
            return True
        elif data[cursor] < value:
            data = data[cursor + 1:]
        else:
            data = data[:cursor]
    return False


def sequential_search(data: list[int], value: int) -> tuple[bool, int]:
    for i in range(len(data)):
        if data[i] == value:
            return True, i
    return False, -1


def bubble_sort(data: list[int]) -> list[int]:
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def selection_sort(data: list[int]) -> list[int]:
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[j] < data[i]:
                data[j], data[i] = data[i], data[j]
    return data


def insertion_sort(data: list[int]) -> list[int]:
    for i in range(1, len(data)):
        a = i
        storage = data[i]
        while a > 0 and data[a - 1] > storage:
            data[a] = data[a - 1]
            a -= 1
        data[a] = storage
    return data



li1x = []
li1y = []
li2x = []
li2y = []
li3x = []
li3y = []
li4x = []
li4y = []
li5x = []
li5y = []
for i in range(100, 10000, 1000):
    li_sort = [randrange(0, i) for j in range(i)]
    li_search = [j for j in range(i)]
    #
    start = time.time()
    binary_search(li_search, li_search[-1])
    end = time.time()
    li1x.append(i)
    li1y.append(end - start)
    #
    start = time.time()
    sequential_search(li_search, li_search[-1])
    end = time.time()
    li2x.append(i)
    li2y.append(end - start)
    #
    start = time.time()
    bubble_sort(li_sort)
    end = time.time()
    li3x.append(i)
    li3y.append(end - start)
    #
    start = time.time()
    selection_sort(li_sort)
    end = time.time()
    li4x.append(i)
    li4y.append(end - start)
    #
    start = time.time()
    insertion_sort(li_sort)
    end = time.time()
    li5x.append(i)
    li5y.append(end - start)
    #
plt.plot(li1x, li1y, color='green')
plt.plot(li2x, li2y, color='blue')
plt.plot(li3x, li3y, color='black')
plt.plot(li4x, li4y, color='red')
plt.plot(li5x, li5y, color='yellow')
plt.show()