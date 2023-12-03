class ReversedString:
    def __init__(self, st):
        self.st = ' '.join(st.split()[::-1])

    def __str__(self):
        return self.st


new_string = ReversedString(input())
print(new_string)