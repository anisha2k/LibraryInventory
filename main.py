import tkinter as tk
from tkinter import messagebox
from collections import defaultdict

# Book class representing a book in the library
class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre

# User class representing a library user
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

# Library class managing books and user transactions
class Library:
    def __init__(self):
        self.books = {}  # Dictionary for book_id -> Book
        self.users = {}  # Dictionary for user_id -> User
        self.transactions = defaultdict(list)  # user_id -> List of borrowed books

    def add_book(self, book):
        if book.book_id in self.books:
            return f"Book with ID {book.book_id} already exists."
        else:
            self.books[book.book_id] = book
            return f"Book '{book.title}' added to the library."

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            return f"Book '{removed_book.title}' removed from the library."
        else:
            return f"No book found with ID {book_id}."

    def add_user(self, user):
        if user.user_id in self.users:
            return f"User with ID {user.user_id} already exists."
        else:
            self.users[user.user_id] = user
            return f"User '{user.name}' registered to the library."

    def borrow_book(self, user_id, book_id):
        if user_id not in self.users:
            return "User ID does not exist."
        if book_id not in self.books:
            return "Book ID does not exist."
        
        user = self.users[user_id]
        book = self.books[book_id]
        if book not in user.borrowed_books:
            user.borrow_book(book)
            self.transactions[user_id].append(book)
            return f"Book '{book.title}' borrowed by '{user.name}'."
        else:
            return f"User '{user.name}' already borrowed the book '{book.title}'."

    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            return "User ID does not exist."
        if book_id not in self.books:
            return "Book ID does not exist."
        
        user = self.users[user_id]
        book = self.books[book_id]
        if book in user.borrowed_books:
            user.return_book(book)
            self.transactions[user_id].remove(book)
            return f"Book '{book.title}' returned by '{user.name}'."
        else:
            return f"User '{user.name}' did not borrow the book '{book.title}'."

    def search_books(self, title=None, author=None):
        results = []
        for book in self.books.values():
            if title and title.lower() in book.title.lower():
                results.append(book)
            elif author and author.lower() in book.author.lower():
                results.append(book)
        return results

    def display_books(self):
        return [f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}" 
                for book in self.books.values()]

# Main Application Window
class LibraryApp:
    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
        self.create_menu()

    def create_menu(self):
        # Clear the window
        self.clear_window()

        # Menu Options
        label_menu = tk.Label(self.root, text="Library Management System", font=("Arial", 16), bg="#f0f0f0")
        label_menu.pack(pady=20)

        button_add_book = tk.Button(self.root, text="Add Book", command=self.add_book_window, width=20)
        button_add_book.pack(pady=5)

        button_remove_book = tk.Button(self.root, text="Remove Book", command=self.remove_book_window, width=20)
        button_remove_book.pack(pady=5)

        button_add_user = tk.Button(self.root, text="Add User", command=self.add_user_window, width=20)
        button_add_user.pack(pady=5)

        button_borrow_book = tk.Button(self.root, text="Borrow Book", command=self.borrow_book_window, width=20)
        button_borrow_book.pack(pady=5)

        button_return_book = tk.Button(self.root, text="Return Book", command=self.return_book_window, width=20)
        button_return_book.pack(pady=5)

        button_search_books = tk.Button(self.root, text="Search Books", command=self.search_books_window, width=20)
        button_search_books.pack(pady=5)

        button_display_books = tk.Button(self.root, text="Display All Books", command=self.display_books_window, width=20)
        button_display_books.pack(pady=5)

        button_exit = tk.Button(self.root, text="Exit", command=self.root.quit, width=20)
        button_exit.pack(pady=5)

    def add_book_window(self):
        self.clear_window()

        label_add_book = tk.Label(self.root, text="Add Book", font=("Arial", 14), bg="#f0f0f0")
        label_add_book.grid(row=0, column=0, columnspan=2, pady=20)

        label_book_id = tk.Label(self.root, text="Book ID", bg="#f0f0f0")
        label_book_id.grid(row=1, column=0)
        self.entry_book_id = tk.Entry(self.root)
        self.entry_book_id.grid(row=1, column=1)

        label_title = tk.Label(self.root, text="Title", bg="#f0f0f0")
        label_title.grid(row=2, column=0)
        self.entry_title = tk.Entry(self.root)
        self.entry_title.grid(row=2, column=1)

        label_author = tk.Label(self.root, text="Author", bg="#f0f0f0")
        label_author.grid(row=3, column=0)
        self.entry_author = tk.Entry(self.root)
        self.entry_author.grid(row=3, column=1)

        label_genre = tk.Label(self.root, text="Genre", bg="#f0f0f0")
        label_genre.grid(row=4, column=0)
        self.entry_genre = tk.Entry(self.root)
        self.entry_genre.grid(row=4, column=1)

        button_add_book = tk.Button(self.root, text="Add Book", command=self.add_book)
        button_add_book.grid(row=5, column=0, columnspan=2, pady=20)

        button_back = tk.Button(self.root, text="Back to Menu", command=self.create_menu)
        button_back.grid(row=6, column=0, columnspan=2)

    def remove_book_window(self):
        self.clear_window()

        label_remove_book = tk.Label(self.root, text="Remove Book", font=("Arial", 14), bg="#f0f0f0")
        label_remove_book.grid(row=0, column=0, columnspan=2, pady=20)

        label_remove_book_id = tk.Label(self.root, text="Book ID", bg="#f0f0f0")
        label_remove_book_id.grid(row=1, column=0)
        self.entry_remove_book_id = tk.Entry(self.root)
        self.entry_remove_book_id.grid(row=1, column=1)

        button_remove_book = tk.Button(self.root, text="Remove Book", command=self.remove_book)
        button_remove_book.grid(row=2, column=0, columnspan=2, pady=20)

        button_back = tk.Button(self.root, text="Back to Menu", command=self.create_menu)
        button_back.grid(row=3, column=0, columnspan=2)

    def add_user_window(self):
        self.clear_window()

        label_add_user = tk.Label(self.root, text="Add User", font=("Arial", 14), bg="#f0f0f0")
        label_add_user.grid(row=0, column=0, columnspan=2, pady=20)

        label_user_id = tk.Label(self.root, text="User ID", bg="#f0f0f0")
        label_user_id.grid(row=1, column=0)
        self.entry_user_id = tk.Entry(self.root)
        self.entry_user_id.grid(row=1, column=1)

        label_name = tk.Label(self.root, text="Name", bg="#f0f0f0")
        label_name.grid(row=2, column=0)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=2, column=1)

        button_add_user = tk.Button(self.root, text="Add User", command=self.add_user)
        button_add_user.grid(row=3, column=0, columnspan=2, pady=20)

        button_back = tk.Button(self.root, text="Back to Menu", command=self.create_menu)
        button_back.grid(row=4, column=0, columnspan=2)

    def borrow_book_window(self):
        self.clear_window()

        label_borrow_book = tk.Label(self.root, text="Borrow Book", font=("Arial", 14), bg="#f0f0f0")
        label_borrow_book.grid(row=0, column=0, columnspan=2, pady=20)

        label_borrow_user_id = tk.Label(self.root, text="User ID", bg="#f0f0f0")
        label_borrow_user_id.grid(row=1, column=0)
        self.entry_borrow_user_id = tk.Entry(self.root)
        self.entry_borrow_user_id.grid(row=1, column=1)

        label_borrow_book_id = tk.Label(self.root, text="Book ID", bg="#f0f0f0")
        label_borrow_book_id.grid(row=2, column=0)
        self.entry_borrow_book_id = tk.Entry(self.root)
        self.entry_borrow_book_id.grid(row=2, column=1)

        button_borrow_book = tk.Button(self.root, text="Borrow Book", command=self.borrow_book)
        button_borrow_book.grid(row=3, column=0, columnspan=2, pady=20)

        button_back = tk.Button(self.root, text="Back to Menu", command=self.create_menu)
        button_back.grid(row=4, column=0, columnspan=2)

    def return_book_window(self):
        self.clear_window()

        label_return_book = tk.Label(self.root, text="Return Book", font=("Arial", 14), bg="#f0f0f0")
        label_return_book.grid(row=0, column=0, columnspan=2, pady=20)

        label_return_user_id = tk.Label(self.root, text="User ID", bg="#f0f0f0")
        label_return_user_id.grid(row=1, column=0)
        self.entry_return_user_id = tk.Entry(self.root)
        self.entry_return_user_id.grid(row=1, column=1)

        label_return_book_id = tk.Label(self.root, text="Book ID", bg="#f0f0f0")
        label_return_book_id.grid(row=2, column=0)
        self.entry_return_book_id = tk.Entry(self.root)
        self.entry_return_book_id.grid(row=2, column=1)

        button_return_book = tk.Button(self.root, text="Return Book", command=self.return_book)
        button_return_book.grid(row=3, column=0, columnspan=2, pady=20)

        button_back = tk.Button(self.root, text="Back to Menu", command=self.create_menu)
        button_back.grid(row=4, column=0, columnspan=2)

    def search_books_window(self):
        self.clear_window()

        label_search_books = tk.Label(self.root, text="Search Books", font=("Arial", 14), bg="#f0f0f0")
        label_search_books.grid(row=0, column=0, columnspan=2, pady=20)

        label_search_title = tk.Label(self.root, text="Title", bg="#f0f0f0")
        label_search_title.grid(row=1, column=0)
        self.entry_search_title = tk.Entry(self.root)
        self.entry_search_title.grid(row=1, column=1)

        label_search_author = tk.Label(self.root, text="Author", bg="#f0f0f0")
        label_search_author.grid(row=2, column=0)
        self.entry_search_author = tk.Entry(self.root)
        self.entry_search_author.grid(row=2, column=1)

        button_search_books = tk.Button(self.root, text="Search Books", command=self.search_books)
        button_search_books.grid(row=3, column=0, columnspan=2, pady=20)

        button_back = tk.Button(self.root, text="Back to Menu", command=self.create_menu)
        button_back.grid(row=4, column=0, columnspan=2)

    def display_books_window(self):
        self.clear_window()

        label_display_books = tk.Label(self.root, text="All Books in Library", font=("Arial", 14), bg="#f0f0f0")
        label_display_books.pack(pady=20)

        books = self.library.display_books()
        if books:
            books_str = "\n".join(books)
        else:
            books_str = "No books available."

        text_display_books = tk.Text(self.root, wrap="word", height=10, width=40)
        text_display_books.insert(tk.END, books_str)
        text_display_books.config(state=tk.DISABLED)
        text_display_books.pack(pady=10)

        button_back = tk.Button(self.root, text="Back to Menu", command=self.create_menu)
        button_back.pack(pady=10)

    def add_book(self):
        try:
            book_id = int(self.entry_book_id.get())
            title = self.entry_title.get()
            author = self.entry_author.get()
            genre = self.entry_genre.get()
            if not title or not author or not genre:
                raise ValueError("All fields must be filled.")

            book = Book(book_id, title, author, genre)
            result = self.library.add_book(book)
            messagebox.showinfo("Add Book", result)
            self.clear_entries(self.entry_book_id, self.entry_title, self.entry_author, self.entry_genre)
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def remove_book(self):
        try:
            book_id = int(self.entry_remove_book_id.get())
            result = self.library.remove_book(book_id)
            messagebox.showinfo("Remove Book", result)
            self.clear_entries(self.entry_remove_book_id)
        except ValueError:
            messagebox.showerror("Error", "Book ID must be a number.")

    def add_user(self):
        try:
            user_id = int(self.entry_user_id.get())
            name = self.entry_name.get()
            if not name:
                raise ValueError("Name field must be filled.")

            user = User(user_id, name)
            result = self.library.add_user(user)
            messagebox.showinfo("Add User", result)
            self.clear_entries(self.entry_user_id, self.entry_name)
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def borrow_book(self):
        try:
            user_id = int(self.entry_borrow_user_id.get())
            book_id = int(self.entry_borrow_book_id.get())
            result = self.library.borrow_book(user_id, book_id)
            messagebox.showinfo("Borrow Book", result)
            self.clear_entries(self.entry_borrow_user_id, self.entry_borrow_book_id)
        except ValueError:
            messagebox.showerror("Error", "Both User ID and Book ID must be numbers.")

    def return_book(self):
        try:
            user_id = int(self.entry_return_user_id.get())
            book_id = int(self.entry_return_book_id.get())
            result = self.library.return_book(user_id, book_id)
            messagebox.showinfo("Return Book", result)
            self.clear_entries(self.entry_return_user_id, self.entry_return_book_id)
        except ValueError:
            messagebox.showerror("Error", "Both User ID and Book ID must be numbers.")

    def search_books(self):
        title = self.entry_search_title.get()
        author = self.entry_search_author.get()
        results = self.library.search_books(title=title, author=author)
        if results:
            results_str = "\n".join([f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}" 
                                     for book in results])
        else:
            results_str = "No matching books found."
        messagebox.showinfo("Search Results", results_str)
        self.clear_entries(self.entry_search_title, self.entry_search_author)

    def clear_entries(self, *entries):
        for entry in entries:
            entry.delete(0, tk.END)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
