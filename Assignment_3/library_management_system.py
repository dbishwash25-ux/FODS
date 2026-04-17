"""
this program implements a basic library management system
it allows user to search borrow and return books
book data is stored in a file
it uses oop concepts like classes and encapsulation
it also uses try except for error handling
"""

import csv


class Book:
    """
    class to represent a book
    """

    def __init__(self, book_id, title, author, status="available"):
        """
        initialize book attributes
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status

    def get_data(self):
        """
        convert book object into list
        """
        return [self.book_id, self.title, self.author, self.status]


class Library:
    """
    class to manage library operations
    """

    def __init__(self, file_name):
        """
        initialize library file
        """
        self.file_name = file_name

    def read_books(self):
        """
        load books from file
        """
        book_list = []

        try:
            with open(self.file_name, "r") as file_data:
                csv_reader = csv.reader(file_data)

                for row_data in csv_reader:
                    book_list.append(
                        Book(row_data[0], row_data[1], row_data[2], row_data[3])
                    )

        except FileNotFoundError:
            pass

        return book_list

    def write_books(self, book_list):
        """
        save books into file
        """
        try:
            with open(self.file_name, "w", newline="") as file_data:
                csv_writer = csv.writer(file_data)

                for book_data in book_list:
                    csv_writer.writerow(book_data.get_data())

        except Exception:
            print("error while saving books")

    def find_book(self, search_text):
        """
        search book by title
        """
        book_list = self.read_books()
        found_status = False

        for book_data in book_list:
            if search_text.lower() in book_data.title.lower():
                print(
                    f"{book_data.book_id} | "
                    f"{book_data.title} | "
                    f"{book_data.author} | "
                    f"{book_data.status}"
                )
                found_status = True

        if not found_status:
            print("no book found")

    def issue_book(self, book_code):
        """
        borrow book if available
        """
        book_list = self.read_books()

        for book_data in book_list:
            if book_data.book_id == book_code:

                if book_data.status == "available":
                    book_data.status = "borrowed"
                    self.write_books(book_list)
                    print("book borrowed successfully")

                else:
                    print("book already borrowed")

                return

        print("book not found")

    def submit_book(self, book_code):
        """
        return borrowed book
        """
        book_list = self.read_books()

        for book_data in book_list:
            if book_data.book_id == book_code:

                if book_data.status == "borrowed":
                    book_data.status = "available"
                    self.write_books(book_list)
                    print("book returned successfully")

                else:
                    print("book is already available")

                return

        print("book not found")


library_data = Library("books.csv")

while True:
    print("\n1. search book")
    print("2. borrow book")
    print("3. return book")
    print("4. exit")

    user_choice = input("enter choice: ")

    if user_choice == "1":
        title_input = input("enter book title: ")
        library_data.find_book(title_input)

    elif user_choice == "2":
        id_input = input("enter book id: ")
        library_data.issue_book(id_input)

    elif user_choice == "3":
        id_input = input("enter book id: ")
        library_data.submit_book(id_input)

    elif user_choice == "4":
        print("program closed")
        break

    else:
        print("invalid choice")