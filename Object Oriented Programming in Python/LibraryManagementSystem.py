# Library Management System using Class and Object

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False


class Library:
    def __init__(self):
        self.books = []

    # Add Book
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    # Display Books
    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                status = "Issued" if book.is_issued else "Available"
                print(f"ID: {book.book_id} | "
                      f"Title: {book.title} | "
                      f"Author: {book.author} | "
                      f"Status: {status}")

    # Issue Book
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    print(f"Book '{book.title}' issued successfully.")
                else:
                    print("Book already issued.")
                return
        print("Book not found.")

    # Return Book
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    print(f"Book '{book.title}' returned successfully.")
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")


# Main Program
library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        book_id = int(input("Enter Book ID to issue: "))
        library.issue_book(book_id)

    elif choice == 4:
        book_id = int(input("Enter Book ID to return: "))
        library.return_book(book_id)

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid choice.")