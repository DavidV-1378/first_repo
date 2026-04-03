from models import A, Book, Library, BankAccount, ToDoItem, SafeCounter as sc, TagEntry, TagTracker, Order, OrderItem, Expense_2
from models_2 import Category, Expense as exp, Ledger as led, Difficulty, Question, QuestionBank

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

def example_library() -> None:
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


# Create a small tag tracker system:
# A tag entry stores a tag name
# The tracker stores many entires
# The tracker mantains a internal dictionary tag -> count
# Must support adding a entry and returning the count for a given tag

def tracker_entry() -> None:
    tracker = TagTracker()
    entry_1 = TagEntry("SQL")

    tracker.add(entry_1)

    tracker.add(TagEntry("Python"))

    tracker.add(TagEntry("Python"))

    print(tracker.count_entry("Python"))


# Build an order system. 
# An order item has: name, price, qty
# Validate all fields
# An order stores many items
# Expose item_count, customer_id and total_cost as properties

def order_system():
    item_1 = OrderItem("Laptop", 499.9, 1)
    item_2 = OrderItem("Headphones", 49.9, 2)
    item_3 = OrderItem("Mouse", 19.9, 3)
    
    final_order = Order("CI3748")

    final_order.add_item(item_1)
    final_order.add_item(item_2)
    final_order.add_item(item_3)

    print(final_order.item_count)
    print(final_order.total_cost)

# TODO:
# Build an expense class that stores: date, category, amount, note.
# Validate date not empty, category not empty and amount > 0.
# Permit: parsing from a csv line, building from a dictionary.
# Implement repr and str.


def dictionary_expense():
    
    dictionary_expense: dict[str, str|float] = {
        "date": "12:08:2026",
        "category": "food",
        "amount": "50.0",
        "note": "groceries"
    }
    expense_1 = Expense_2.build_from_dictionary(dictionary_expense)

    expense_from_line = Expense_2.from_csv_line("18:06:2025;food;100.0;groc", ";")


# Build an expense system, where categories are a Enum(food, transport, books, fun, other)
# Expense stores date, category, amount and note.
# Ledger stores many Expenses and supports len, Expense in ledger and if Ledger, method by_category that retuns dict[category, float]

def expense_system():
    expense_1 = exp("12:09:2026", Category.FOOD, 25.0, "grocerise")
    expense_2 = exp("27:06:2026", Category.TRANSPORT, 10.0, "taxi")
    expense_3 = exp("15:04:2026", Category.FOOD, 35.0, "grocerise")
    expense_4 = exp("15:04:2026", Category.FOOD, 6.0, "grocerise")

    ledger_1 = led()
    ledger_1.add(expense_1)
    ledger_1.add(expense_2)
    ledger_1.add(expense_3)
    ledger_1.add(expense_4)

    print(len(ledger_1))
    print(f"e1 in ledger: {expense_1 in ledger_1}")
    print(f"Not empty: {bool(ledger_1)}")
    
    for cat, total in ledger_1.by_category().items():
        print(f"{cat.value}: {total}")

# Build a quizz system with a difficulty Enum(easy = 1, medium  = 2, hard = 3)
# Question class stores prompt, answer and difficulty properties and implements custom equlity, comparing by prompt text
# QuestionBank class stores many questions and supports len, question in bank, bank empty, filter by a difficulty -> list[Question]

def main():
    question_1 = Question("1 + 1", "2", Difficulty.EASY)
    question_2 = Question("2 + 2", "4", Difficulty.EASY)
    question_3 = Question("2^2", "4", Difficulty.MEDIUM)

    qb = QuestionBank()

    qb.add(question_1)
    qb.add(question_2)
    qb.add(question_3)

    print(question_1 == question_2)
    print(question_1)
    print(qb.fliter_by_difficulty(Difficulty.EASY))


if __name__ == "__main__":   
    main()

