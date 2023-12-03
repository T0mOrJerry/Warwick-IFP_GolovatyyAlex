import sys  # Import sys to use streaming input


def longest(lis: list):  # Creating function and state that it takes object of list class
    return len(max(lis, key=lambda x: len(x)))  # Return length of the longest string found using lambda function


li = [i.strip() for i in sys.stdin]  # Creating list of strings using streaming input to stop input use CTRL+M/CMD+D
print(longest(li))
