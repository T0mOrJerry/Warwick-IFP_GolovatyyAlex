def selection_sort(data: list[int]) -> list[int]:
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[j] < data[i]:
                data[j], data[i] = data[i], data[j]
    return data


print(selection_sort([14, 46, 43, 27, 57, 41, 45, 21, 70]))
