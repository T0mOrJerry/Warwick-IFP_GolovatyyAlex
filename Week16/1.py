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


print(binary_search([1, 2, 3, 5, 6, 8], 6))
print(binary_search([1, 2, 3, 8], 5))
