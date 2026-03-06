from models import A, Book, Library, BankAccount, ToDoItem, SafeCounter as sc

def BA() -> None:
    account = BankAccount(100.0, "David")
    account.deposit(25.0)
    print(account.balance())
    print(account)

# In models, define "ToDoItem"
# ToDoItem is a class that has a title and done: bool default: false
# Method mark_done returns None and __repr__ that prints class status
# In app.py create two items, mark one of them done and print both

def ToDo() -> None:
    a = ToDoItem("invat")
    b = ToDoItem("mananc")
    a.mark_done()
    print(a, b)


# Create Class save counter that has an internal value _value of type int, starting with 0.
# Create method inc and dec, dec raise value error if lower than 0 and method get.

def safe_counter() -> None:
    a = sc()
    a.inc()
    a.inc()
    a.inc()
    print(a.get())
    a.dec()
    a.dec()
    print(a)

def exempleA() -> None:
    a = A()
    b = a # b.x = 1
    b.x = 5
    print(a.x) # 

# 1. Create a small library system: 
# A book has a title and a number of pages
# A library can store many books
# The library can return total number of pages across books
# Invalid books must be rejected (Empty title or non positive pages)

# 2. Extend the library so it can retrun a dictonary (dict) where:
# Keys are the first letter of each title, upper cased.
# Values are the number of books that start with that letter.

def main() -> None:
    maths_book = Book("Maths 101", 300)
    cs_book = Book("CS 101", 100)
    m_book = Book("Maths 102", 400)
    library = Library()
    library.add_book(cs_book)
    library.add_book(maths_book)
    library.add_book(m_book)
    items = library.items() # Not the same object as libray._items


    print(library.total_pages())
    print(cs_book)
    print(maths_book)
    print(library.total_by_first_letters())
    print(items)

# 3. Add a method to the library that returns all stored books. but witout allowing the caller to mutate the list

if __name__ == "__main__":   
    main()

