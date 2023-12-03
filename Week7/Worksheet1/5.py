class StringClass:
    def __init__(self):
        self.st = ''

    def get_string(self):
        self.st = input()

    def print_string(self):
        print(self.st.upper())


string_in_out = StringClass()
string_in_out.get_string()
string_in_out.print_string()

