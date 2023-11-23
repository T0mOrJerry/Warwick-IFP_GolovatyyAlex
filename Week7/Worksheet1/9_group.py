class Book:
    # to create a book object with its attributes
    def __init__(self, title, author, ISBN, quantity):
        self.title = title.lower()
        self.author = author
        self.ISBN = ISBN
        self.quantity = quantity

    # methods
    # display book details:
    def __str__(self):
        return f"Book Title: {self.title}\nBook Author: {self.author}\nBook ISBN: {self.ISBN}\nQuantity Available: {self.quantity}"

    # update quantity (for borrow, return)
    # num input can be (-1) for borrow, and can be (1) for return
    # if you guys have any other idea let me know :)
    def update_quantity(self, num):
        self.quantity += num


# Class User used to make operations with users
class User:
    def __init__(self, name, studentid):
        self.name = name
        self.studentid = studentid
        self.books_borrowed = []

    # Function to show the information about the object of this class
    def __str__(self):
        print(f"{self.name} ({self.studentid}) {self.books_borrowed}")


# Class library contains all the information about the users and the books in the library
# It also contains the functions which create interaction between User and Book classes
class Library:
    def __init__(self):
        self.books = []  # Storage of all the Book class objects
        self.books_title = {}  # Dictionary for searching which mapping object Book with its attribute - title
        self.books_ISBN = {}  # Dictionary for searching which mapping object Book with its attribute - ISBN
        self.users = []    # Storage of all the User class objects
        self.user_id = {}  # Dictionary for searching which mapping object User with its attribute - studentid
        self.users_books = {}  # Dictionary for storing all the books, which a user has borrowed

    # Function which add already created book to the library and to the searching dictionaries
    def add_book(self, book: Book):
        self.books.append(book)
        self.books_title[book.title] = book
        self.books_ISBN[book.ISBN] = book

    # Function which add already created user to the library and to the searching dictionaries
    def add_user(self, user: User):
        self.users.append(user)
        self.user_id[user.studentid] = user
        self.users_books[user] = []

    # check availability
    def check_availability(self, key: str, title: bool):
        if title:  # Here we distinguish whether we search for a title of the book or for its ISBN
            if key in self.books_title:
                return bool(self.books_title[key.lower()].quantity)
            return None
        if key in self.books_ISBN:
            return bool(self.books_ISBN[key.lower()].quantity)
        return None

    # Functions of borrowing or returning books by user - mostly the same as check_availability
    def borrow_book(self, key: str, title: bool, stu_id: int):
        pass

    def return_book(self, key: str, title: bool, stu_id: int):
        pass


# Creating the library and add some books
Warwick_Library = Library()
Warwick_Library.add_book(Book("Wonder", "R. J. Palacio", 3465879, 2))
Warwick_Library.add_book(Book("The Witcher: Sword of destiny", "A. Sapkowski", 12345678, 1))
Warwick_Library.add_book(Book("The Lord Of The Rings: The Two Towers", "J. R. R. Tolkien", 9876543, 0))
Warwick_Library.add_book(Book("War and Peace", "Leo Tolstoy", 74659374, 4))
Warwick_Library.add_book(Book("1984", "George Orwell", 3647683769, 3))
mainloop = True
while mainloop:  # Loop for menu of actions
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
        Warwick_Library.add_user(User(u_name, u_id))
        print("--User has been successfully added--")
    elif a == 3:
        b = int(input(
            'Choose action:\n1 - to borrow book\n2 - to return book\n3 - to check availability of the book\n'))
        if b == 1:
            print('!!! WE ARE STILL DESIGNING THIS SECTION !!!')
        elif b == 2:
            print('!!! WE ARE STILL DESIGNING THIS SECTION !!!')
        elif b == 3:
            availability = None
            search_attribute = int(input(
                'Type 1 if you want to search a book by title\nType 2 if you want to search the book by ISBN\n'))
            if search_attribute == 1:
                t = input('Type a title of the book you want to borrow: ')
                availability = Warwick_Library.check_availability(t, True)
            elif search_attribute == 2:
                t = input('Type an ISBN of the book you want to borrow: ')
                availability = Warwick_Library.check_availability(t, False)
            if availability is None:
                print("--Library doesn't have this book--")
            elif availability:
                print('--You can take this book--')
            else:
                print('--Unfortunately there are no books left--')
    elif a == 4:
        b = int(input(
            'Choose action:\n1 - to show the list of books\n2 - to show the list of users\n'))
        print('!!! WE ARE STILL DESIGNING THIS SECTION !!!')
