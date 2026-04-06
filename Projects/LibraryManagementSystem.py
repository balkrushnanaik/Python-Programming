import json
import os

FILE_NAME = "library_data.json"

# ---------- Helper Functions ----------
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# ---------- Library Functions ----------
def add_book():
    data = load_data()

    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False,
        "issued_to": None
    }

    data.append(book)
    save_data(data)

    print("Book added successfully!")

def view_books():
    data = load_data()

    if not data:
        print("No books available.")
        return

    for book in data:
        print("\nID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Issued:", book["issued"])

def search_book():
    data = load_data()

    keyword = input("Enter title to search: ").lower()

    found = False
    for book in data:
        if keyword in book["title"].lower():
            print("\nBook Found:")
            print(book)
            found = True

    if not found:
        print("Book not found.")

def issue_book():
    data = load_data()

    book_id = input("Enter Book ID to issue: ")

    for book in data:
        if book["id"] == book_id:
            if book["issued"]:
                print("Book already issued.")
                return

            user = input("Enter student name: ")
            book["issued"] = True
            book["issued_to"] = user

            save_data(data)
            print("Book issued successfully!")
            return

    print("Book not found.")

def return_book():
    data = load_data()

    book_id = input("Enter Book ID to return: ")

    for book in data:
        if book["id"] == book_id:
            if not book["issued"]:
                print("Book was not issued.")
                return

            book["issued"] = False
            book["issued_to"] = None

            save_data(data)
            print("Book returned successfully!")
            return

    print("Book not found.")

def delete_book():
    data = load_data()

    book_id = input("Enter Book ID to delete: ")

    new_data = [book for book in data if book["id"] != book_id]

    save_data(new_data)

    print("Book deleted successfully!")

# ---------- Main Menu ----------
while True:
    print("\n====== Library Menu ======")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        delete_book()

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")