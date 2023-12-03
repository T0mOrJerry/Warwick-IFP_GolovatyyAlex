import sys


for i in sys.stdin:
    print((lambda x: x.isdigit())(i.strip()))
