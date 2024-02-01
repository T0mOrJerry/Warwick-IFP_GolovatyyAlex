with open("S15 _ 1_SampleFile.txt") as file:
    count = 1
    for line in file.readlines():
        print(f"Line {count} contains: {line.strip()}")
        count += 1