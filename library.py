books = []
def add_book():
    book = input("Enter book name to add: ")
    books.append(book)
    print("Book added successfully.")
def show_books():
    if not books:
        print("No books available.")
    else:
        print("Available books:")
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")
def menu():
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Exit")
while True:
    menu()
    choice = input("Enter choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        show_books()
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
