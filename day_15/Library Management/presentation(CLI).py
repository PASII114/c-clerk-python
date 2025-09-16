import time
from datetime import datetime

from repositories import InMemoryLoanRepository, InMemoryMemberRepository, InMemoryBookRepository
from service import LibraryService, LibraryError

library_service = LibraryService(books= InMemoryBookRepository(), members= InMemoryMemberRepository(), loans= InMemoryLoanRepository())

def list_books():
    books = library_service.list_all_books()

    for book in books:
        status = "Available" if book.is_book_available() else f"Out by - {book.book_lend_member_id}"

        print(f"""
        Book Id - {book.book_id}
        Title - {book.title}
        Author - {book.author}
        Year - {book.year}
        Status - {status}
""")
        time.sleep(2)

def add_books():

    book_id = input("Enter Book Id: ")
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    year = input("Enter Published Year: ")

    try:
        library_service.add_book(book_id, title, author, year)
    except LibraryError as e:
        print(e)

    time.sleep(2)

def add_members():

    member_id = input("Enter Member id: ")
    name = input("Enter Member Name: ")

    try:
        library_service.register_member(member_id, name)
    except LibraryError as e:
        print (e)

    time.sleep(2)

def borrow_books():

    loan_id = input("Enter Loan Id: ")
    member_id = input("Enter Member id: ")
    book_id = input("Enter Book id: ")

    try:
        library_service.borrow_book(loan_id, book_id, member_id)
    except LibraryError as e:
        print(e)

        time.sleep(2)


def return_books():
    loan_id = input("Enter loan id: ")

    try:
        library_service.return_book(loan_id)
    except LibraryError as e:
        print(e)

def list_all_loans():
    loans = library_service.list_all_loans()

    for loan in loans:
        status = "Active" if loan.is_active() else "Loan is Not Active"

        print(f"""
        Loan ID - {loan.loan_id}
        Member ID - {loan.member_id}
        Book ID - {loan.book_id}
        Borrowed at - {loan.borrowed_at}
        Status - {status}
        """)

        time.sleep(2)


while True:
    print("======================= Library System =======================")
    print("""
    1. Press 1 to List Books
    2. Press 2 to Add Books
    3. Press 3 to Add Members
    4. Press 4 to Borrow Books
    5. Press 5 to return Books
    6. Press 6 to List Loans
    """)

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        list_books()

    if choice == 2:
        add_books()

    if choice == 3:
        add_members()

    if choice == 4:
        borrow_books()

    if choice == 5:
        return_books()

    if choice == 6:
        list_all_loans()