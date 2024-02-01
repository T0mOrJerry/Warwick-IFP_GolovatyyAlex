with open("S15 _ 1_SampleFile.txt") as file:
    data = file.read()
    print(data)
print()
with open("S15 _ 1_SampleFile.txt") as file:
    data = file.readline()
    print(data)
with open("S15 _ 1_SampleFile.txt") as file:
    for line in file.readlines():
        print(line.strip())