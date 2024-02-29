def sequential_search(data: list[int], value: int) -> tuple[bool, int]:
    for i in range(len(data)):
        if data[i] == value:
            return True, i
    return False, -1


print(sequential_search([11, 23, 58, 31, 56, 77, 43, 12, 65, 19], 31))
