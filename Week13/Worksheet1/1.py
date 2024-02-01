import bisect

done = False
while not done:
    try:
        li = sorted(list(map(int, input("Input your values, separated with space: ").split())))
        done = True
    except Exception:
        print("Try again, one more time - INPUT INTEGERS SEPARATED WITH SPACE!!!!")
print(li)
done = False
while not done:
    print()
    try:
        a = input("Input your integer value you want to insert in the list,\nIf you want to exit type 'exit'.\n")
        if a == 'exit':
            done = True
        else:
            a = int(a)
            b = bisect.bisect_left(li, a)
            print(b, len(li) - b)
    except Exception:
        print("Try again, one more time - INPUT INTEGER!!!!")
