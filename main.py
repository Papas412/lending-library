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

    def __str__(self)   :
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) "
           