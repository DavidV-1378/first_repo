#object = state + behavior

class BankAccount:
    def __init__(self, balance: float) -> None:
        if balance < 0:
            raise ValueError("No negative balance allowed!")
        self.balance = balance
    def deposit(self, amount: float) -> None:
        pass

class Dog:
    def __init__(self, name: str) -> None:
        self.name = name
    def talk(self) -> None:
        print("woof" + self.name)

d1 = Dog("Jimmy")

d1.talk()
print(d1.name)

d2 = Dog("Ymmij")

d2.talk()

class A:
    def f(self, x:int) -> int:
        return x + 1
    
a = A()
y = a.f(10)

print(y)

# insatnce vs class attributes:
# -instance attributes belong to each object
# -class attributes are shared

class Counter:
    total = 0 # class attribute
    def __init__(self, value) -> None:
        Counter.total += value
        self.value = value # instance attribute

c1 = Counter(5)
c2 = Counter(6)

print(c1.total, c1.value)
print(c2.total, c2.value)
