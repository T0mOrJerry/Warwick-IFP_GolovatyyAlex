class Book:
    # to create a book object with its attributes
    def __init__(self, title: str, author: str, ISBN: str, quantity: int):
        self.title = title.lower()
        self.author = author
        self.ISBN = ISBN
        self.quantity = quantity

    # methods
    # display book details:
    def __str__(self):
        return f"--Book Title: {self.title}\tBook Author: {self.author}\tBook ISBN: {self.ISBN}\tQuantity Available: " \
               f"{self.quantity}"

    # update quantity (for borrow, return)
    # num input can be (-1) for borrow, and can be (1) for return
    # if you guys have any other idea let me know :)
    def update_quantity(self, num: int):
        self.quantity += num

    def check_availability(self):
        return bool(self.quantity)


# Class User used to make operations with users
class User:
    def __init__(self, name: str, studentid: str, staff: bool):
        self.name = name
        self.studentid = studentid
        self.books_borrowed = []
        self.staff = staff

    # Function to show the information about the object of this class
    def __str__(self):
        return f"--User {self.name} has id ({self.studentid}) borrowed\n" + '\n'.join(list(map(str, self.books_borrowed)))


# Class library contains all the information about the users and the books in the library
# It also contains the functions which create interaction between User and Book classes
class Library:
    def __init__(self):
        self.books = []  # Storage of all the Book class objects
        self.books_title = {}  # Dictionary for searching which mapping object Book with its attribute - title
        self.books_ISBN = {}  # Dictionary for searching which mapping object Book with its attribute - ISBN
        self.users = []    # Storage of all the User class objects
        self.user_id = {}  # Dictionary for searching which mapping object User with its attribute - studentid

    # Function which add already created book to the library and to the searching dictionaries
    def add_book(self, book: Book):
        self.books.append(book)
        self.books_title[book.title] = book
        self.books_ISBN[book.ISBN] = book

    # Function which add already created user to the library and to the searching dictionaries
    def add_user(self, user: User):
        self.users.append(user)
        self.user_id[user.studentid] = user

    # check availability
    def check_availability_library(self, key: str, title: bool):
        if title:  # Here we distinguish whether we search for a title of the book or for its ISBN
            if key.lower() in self.books_title:
                return self.books_title[key.lower()].check_availability()
            return None
        if key in self.books_ISBN:
            return self.books_ISBN[key].check_availability()
        return None

    # Functions of borrowing or returning books by user - It had more sense to state them inside Library class,
    # because the idea of Library class - actions which require both classes - Book and User
    def borrow_book(self, key: str, title: bool, stu_id: str):
        if stu_id not in self.user_id:  # Check if the user exists
            return 'Error - No such user. Try again'
        else:
            st = self.user_id[stu_id]
            av = self.check_availability_library(key, title)  # Check if the book exist and available
            if av is None:
                return 'Error - No such book. Try again'
            elif not av:
                return 'Error - No available copies of the book. Try again later'
            else:
                if title:  # Check if user borrowed the book
                    bk = self.books_title[key.lower()]
                else:
                    bk = self.books_ISBN[key.lower()]
                st.books_borrowed.append(bk)
                bk.update_quantity(-1)
                return 'Success'

    def return_book(self, key: str, title: bool, stu_id: str):
        if stu_id not in self.user_id:
            return 'Error - No such user. Try again'
        else:
            st = self.user_id[stu_id]
            av = self.check_availability_library(key, title)
            if av is None:
                return 'Error - No such book. Try again'
            elif not av:
                return 'Error - No available copies of the book. Try again'
            else:
                if title:
                    bk = self.books_title[key.lower()]
                else:
                    bk = self.books_ISBN[key.lower()]
                if bk in st.books_borrowed:
                    st.books_borrowed.pop(st.books_borrowed.index(bk))
                    bk.update_quantity(1)
                    return 'Success'
                else:
                    return "You haven't borrowed this book"


# Creating the library and add some books and users for tests
Warwick_Library = Library()
Warwick_Library.add_book(Book("Wonder", "R. J. Palacio", "3465879", 2))
Warwick_Library.add_book(Book("The Witcher: Sword of destiny", "A. Sapkowski", "12345678", 1))
Warwick_Library.add_book(Book("The Lord Of The Rings: The Two Towers", "J. R. R. Tolkien", "9876543", 0))
Warwick_Library.add_book(Book("War and Peace", "Leo Tolstoy", "74659374", 4))
Warwick_Library.add_book(Book("1984", "George Orwell", "3647683769", 3))
Warwick_Library.add_user(User("Joe", "0000", True))
Warwick_Library.add_user(User("Alex", "1111", False))
mainloop = True
while mainloop:  # Loop for menu of actions
    print()
    a = int(input(
        'Choose action:\n0 - exit\n1 - add new book\n2 - add new user\n3 - open user action menu'
        '\n4 - open staff action menu\n'))
    if a == 0:
        mainloop = False
    elif a == 1:
        b_title = input('Type title of the book: ')
        b_author = input('Type author of the book: ')
        b_ISBN = input('Type ISBN of the book: ')
        b_quantity = int(input('Type starting amount of books: '))
        Warwick_Library.add_book(Book(b_title, b_author, b_ISBN, b_quantity))
        print("--Book has been successfully added--")
    elif a == 2:
        u_name = input('Type your name: ')
        u_id = input('Type your student id: ')
        u_staff = input('Are you a staff member? (y/n): ')
        if u_staff == 'y':
            Warwick_Library.add_user(User(u_name, u_id, True))
            print("--User has been successfully added--")
        elif u_staff == 'n':
            Warwick_Library.add_user(User(u_name, u_id, False))
            print("--User has been successfully added--")
        else:
            print("(y/n) - it's not that complicated! Try again!")
    elif a == 3:
        b = int(input(
            'Choose action:\n1 - to borrow book\n2 - to return book\n3 - to check availability of the book\n'))
        if b == 1:
            student = input("Type your student/staff ID: ")
            search_attribute = int(input(
                'Type 1 if you want to search a book by title\nType 2 if you want to search the book by ISBN\n'))
            if search_attribute == 1:
                t = input('Type a title of the book you want to borrow: ')
                print(f"--The result of the operation - {Warwick_Library.borrow_book(t, True, student)}--")
            elif search_attribute == 2:
                t = input('Type an ISBN of the book you want to borrow: ')
                print(f"--The result of the operation - {Warwick_Library.borrow_book(t, False, student)}--")
        elif b == 2:
            student = input("Type your student/staff ID: ")
            search_attribute = int(input(
                'Type 1 if you want to search a book by title\nType 2 if you want to search the book by ISBN\n'))
            if search_attribute == 1:
                t = input('Type a title of the book you want to return: ')
                print(f"--The result of the operation - {Warwick_Library.borrow_book(t, True, student)}--")
            elif search_attribute == 2:
                t = input('Type an ISBN of the book you want to return: ')
                print(f"--The result of the operation - {Warwick_Library.return_book(t, False, student)}--")
        elif b == 3:
            availability = None
            search_attribute = int(input(
                'Type 1 if you want to search a book by title\nType 2 if you want to search the book by ISBN\n'))
            if search_attribute == 1:
                t = input('Type a title of the book you want check for availability: ')
                availability = Warwick_Library.check_availability_library(t, True)
            elif search_attribute == 2:
                t = input('Type an ISBN of the book you want check for availability: ')
                availability = Warwick_Library.check_availability_library(t, False)
            if availability is None:
                print("--Library doesn't have this book--")
            elif availability:
                print('--You can take this book--')
            else:
                print('--Unfortunately there are no books left--')
    elif a == 4:
        staff = input('Type your staff id: ')
        if staff not in Warwick_Library.user_id:
            print("--The user doesn't exist__")
        elif not Warwick_Library.user_id[staff].staff:
            print("--You're a student, you don't have access--")
        else:
            print("--You were successfully loged in as a staff member--")
            secondloop = True
            while secondloop:
                print()
                b = int(input(
                    'Choose action:\n1 - to show the list of books\n2 - to show the list of users\n3 - Exit\n'))
                if b == 1:
                    print('\n'.join(list(map(str, Warwick_Library.books))))
                elif b == 2:
                    print('\n'.join(list(map(str, Warwick_Library.users))))
                elif b == 3:
                    secondloop = False
