# Library Management System
# Name       : Manthan Sharma
# Course     : Programming for Problem Solving using Python
# Roll No.   : 2501410037

class Library:
    def __init__(self, filename="library.txt"):
        self.filename = filename

        # Create file if it doesn't exist
        try:
            f = open(self.filename, "r")
            f.close()
        except:
            f = open(self.filename, "w")
            f.close()

    def add_book(self, title, author, isbn):
        f = open(self.filename, "a")
        f.write(title + "," + author + "," + isbn + ",available\n")
        f.close()
        print("Book added successfully.")

    def issue_book(self, isbn):
        f = open(self.filename, "r")
        lines = f.readlines()
        f.close()

        found = False
        new_lines = []

        for line in lines:
            data = line.strip().split(",")

            if data[2] == isbn:
                found = True
                if data[3] == "available":
                    data[3] = "issued"
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
            new_lines.append(",".join(data) + "\n")

        if not found:
            print("Book not found.")
            return

        f = open(self.filename, "w")
        f.writelines(new_lines)
        f.close()

    def return_book(self, isbn):
        f = open(self.filename, "r")
        lines = f.readlines()
        f.close()

        found = False
        new_lines = []

        for line in lines:
            data = line.strip().split(",")

            if data[2] == isbn:
                found = True
                if data[3] == "issued":
                    data[3] = "available"
                    print("Book returned successfully.")
                else:
                    print("Book is already available.")
            new_lines.append(",".join(data) + "\n")

        if not found:
            print("Book not found.")
            return

        f = open(self.filename, "w")
        f.writelines(new_lines)
        f.close()

    def search_title(self, title):
        f = open(self.filename, "r")
        lines = f.readlines()
        f.close()

        found = False

        for line in lines:
            data = line.strip().split(",")
            if title.lower() in data[0].lower():
                print("Title:", data[0], "Author:", data[1], "ISBN:", data[2], "Status:", data[3])
                found = True

        if not found:
            print("No matching book found.")

    def display_all(self):
        f = open(self.filename, "r")
        lines = f.readlines()
        f.close()

        if not lines:
            print("No books in the library.")
            return

        for line in lines:
            data = line.strip().split(",")
            print("Title:", data[0], "Author:", data[1], "ISBN:", data[2], "Status:", data[3])


def main():
    lib = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book By Title")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            lib.add_book(title, author, isbn)

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            lib.issue_book(isbn)

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            lib.return_book(isbn)

        elif choice == "4":
            lib.display_all()

        elif choice == "5":
            title = input("Enter title to search: ")
            lib.search_title(title)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

main()
