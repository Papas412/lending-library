class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return True
        else:
            return False

    def get_status(self):
        if self.is_available:
            return "Available"
        else:
            return "Borrowed"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        self.books.remove(book)
    
    def get_books(self):
        return self.books
    
    def get_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
    
    def get_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book

    def __str__(self):
        return f"Library with {len(self.books)} books"

    def lend_book(self, book, user):
        if book.borrow():
            user.borrow_book(book)
            return True
        else:
            return False

    def return_book(self, book, user):
        if book.return_book():
            user.return_book(book)
            return True
        else:
            return False



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = []

    def borrow_book(self, book):
        self.books.append(book)

    def return_book(self, book):
        self.books.remove(book)

    def get_books(self):
        return self.books

    def __str__(self):
        return f"User {self.name} with {len(self.books)} books"

user1 = User("John Doe", "john.doe@example.com")
user2 = User("Jane Doe", "jane.doe@example.com")

my_library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("1984", "George Orwell", "9780451524935")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780743273565")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

print(book1)
print(book2)
print(book3)
book1.borrow()
print(book1.get_status())


print(my_library)

book1.return_book()
print(book1.get_status())

my_library.lend_book(book1, user1)
print(book1.get_status())
print(user1.get_books())

print(my_library)