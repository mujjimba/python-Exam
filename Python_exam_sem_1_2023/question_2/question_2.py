# (i) Creating an instance of the Book class

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        
book1 = Book("To Kill a Barking dog", "Brett Young", 354)

# Displaying the information about the book
book1.display_info




#(ii) Create a derived class "EBook" that inherites from the "Book" class
class EBook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format

    def display_info(self):
        super().display_info()
        print(f"Format: {self.format}")

# Creating an instance of the EBook class
ebook1 = EBook("Animal Farm", "Prince Louis", 324, "PDF")

# Displaying the information about the eBook
ebook1.display_info()



# (iii) Create a function on the "Book" class that returns the book title and it's author
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
       

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        

    def get_title_author(self):
        return f"Title: {self.title}\nAuthor: {self.author}"

# Creating an instance of the Book class
book1 = Book("To Kill a Barkin dog", "Brett Young")

# Displaying the information about the book
title_author = book1.get_title_author()


# (iv)
# a) Class is a blueprint or a template for creating objects.
# b) Object is an instance of a class.