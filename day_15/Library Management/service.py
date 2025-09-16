from dataclasses import dataclass
from datetime import datetime

from models import Book, Member, Loan

from repositories import BookRepository, LoanRepository, MemberRepository

class LibraryError(Exception):
    pass

@dataclass
class LibraryService:

    books: BookRepository
    members: MemberRepository
    loans: LoanRepository

    # def __init__(self, books: BookRepository, members: MemberRepository, loans: LoanRepository):
    #     self.books = books
    #     self.members = members
    #     self.loans = loans

    def add_book(self, book_id: str, title: str, author: str, year: str) -> Book:
        if self.books.get_by_id(book_id) is not None:
            raise LibraryError(f"Book already exists with book id - {book_id}")

        book = Book(book_id, title, author, year) #creating a book object
        self.books.add(book)
        return book

    def register_member(self, member_id: str, name: str) -> Member:
        if self.members.get_member_by_id(member_id) is not None:
            raise LibraryError(f"Member already exists with member id - {member_id}")

        member = Member(member_id, name) #creating a member object
        self.members.add(member)
        return member

    def list_all_books(self):
        return self.books.list_all_books()

    def borrow_book(self, loan_id: str, book_id: str, member_id: str) -> Loan:
        if self.books.get_by_id(book_id) is None:
            raise LibraryError("Book Not Found")

        if self.members.get_member_by_id(member_id) is None:
            raise LibraryError("Member Not Found")

        if not self.books.get_by_id(book_id).is_book_available():
            raise LibraryError("Book Not Available")

        loan = Loan(loan_id, member_id, book_id, datetime.now())
        book = self.books.get_by_id(book_id)
        book.book_lend_member_id = member_id
        self.books.update(book)

        self.loans.add(loan)
        return loan

    def return_book(self, loan_id: str) -> Loan:

        loan = self.loans.get_by_id(loan_id)

        if loan is None:
            raise LibraryError("Loan Doesn't Exist")

        if not loan.is_active():
            raise LibraryError("Loan is Not Active")

        book = self.books.get_by_id(loan.book_id)
        book.book_lend_member_id = None
        self.books.update(book)

        loan.returned_at = datetime.now()
        self.loans.update(loan)

        return loan


    def list_all_loans(self):
        return [loan for loan in self.loans.list_all_loans() if loan.is_active()]