class BankAcoount:
    def __init__(self, balance: float, owner: str) -> None:
        if balance < 0.0:
            raise ValueError(f"Initial balance, {balance} cannot be negative")
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount: float) -> None:
        if amount <= 0.0:
            raise ValueError(f"Deposit must be positive")
        self.__balance += amount
    def balance(self) -> float:
        return self.__balance
    def __repr__(self) -> str:
        return f"Bank account (owner = {self.owner}, balance = {self.__balance: .2f})"
    

class ToDoItem:
    def __init__(self, title: str) -> None:
        self.title = title
        self.done = False
    def mark_done(self) -> None:
        self.done = True
    def __repr__(self) -> str:
        status = "Done" if self.done else "To Do"
        return f"ToDoItem title: {self.title}, status: {status}"

