def bubble_sort(data: list[int]) -> list[int]:
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


print(bubble_sort([14, 46, 43, 27, 57, 41, 45, 21, 70]))
