from models import BankAcoount
from models import ToDoItem
from models import SafeCounter as sc

def BA() -> None:
    account = BankAcoount(100.0, "David")
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

def main() -> None:
    a = sc()
    a.inc()
    a.inc()
    a.inc()
    print(a.get())
    a.dec()
    a.dec()
    print(a)





if __name__== "__main__":   
    main()

