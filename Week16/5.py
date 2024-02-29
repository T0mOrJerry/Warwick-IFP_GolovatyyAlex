def insertion_sort(data: list[int]) -> list[int]:
    for i in range(1, len(data)):
        a = i
        storage = data[i]
        while a > 0 and data[a - 1] > storage:
            data[a] = data[a - 1]
            a -= 1
        data[a] = storage
    return data


print(insertion_sort([14, 46, 43, 27, 57, 41, 45, 21, 70]))
