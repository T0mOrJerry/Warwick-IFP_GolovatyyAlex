with open("S15 _ 1_SampleFile.txt") as file:
    num = int(input())
    for i in range(num):
        print(file.readline().strip())