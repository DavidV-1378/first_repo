from models import BankAcoount
from models import ToDoItem

def BA() -> None:
    account = BankAcoount(100.0, "David")
    account.deposit(25.0)
    print(account.balance())
    print(account)

# In models, define "ToDoItem"
# ToDoItem is a class that has a title and done: bool default: false
# Method mark_done returns None and __repr__ that prints class status
# In app.py create two items, mark one of them done and print both

def main() -> None:
    a = ToDoItem("invat")
    b = ToDoItem("mananc")
    a.mark_done()
    print(a, b)


if __name__== "__main__":   
    main()

