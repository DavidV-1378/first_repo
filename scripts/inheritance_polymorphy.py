

class Discount:
    def apply(self, total: float) -> float:
        raise NotImplementedError
    
class PrecentageDiscount(Discount):
    def apply(self, total: float) -> float:
        return total * 0.9
    
class FixedDiscount(Discount):
    def apply(self, total: float) -> float:
        return max(0.0, total - 20.0)
    

class Animal:
    def move(self) -> str:
        return "Moving"
    
class Dog(Animal):
    pass

class Car(Animal):
    pass

items = [Dog(), Car()]
for item in items:
    print(item.move())


class LogParser:
    def parse_line(self, line: str) -> str | None:
        raise NotImplementedError
    
class PipeLogParser(LogParser):
    def parse_line(self, line: str) -> str | None:
        parts = line.split("|")
        if len(parts) != 3:
            return None
        return line
    
class CSVLogParser(LogParser):
    def parse_line(self, line: str) -> str | None:
        parts = line.split(",")
        if len(parts) != 3:
            return None
        return line
    
# 1. Create a base class Notifier with method send(mesage: str) -> str: and subclasses EmailNotifier and SMSNotifier.

class Notifier:
    def send(self, message: str) -> str:
        raise NotImplementedError
    
class EmailNotifier(Notifier):
    def send(self, message: str) -> str:
        return f"Email: {message}"

class SMSNotifier(Notifier):
    def send(self, message: str) -> str:
        return f"SMS: {message}"
    
# 2. Write a function broadcast(notifiers: list[Notifier], message: str) -> list[str]: that returns a list[notifiers].

def broadcast(notifiers: list[Notifier], message: str) -> list[str]:
    return [notifier.send(message) for notifier in notifiers]

notifiers = [EmailNotifier(), SMSNotifier()]

print(broadcast(notifiers, "hello"))



# 1. Create and validate a frozen dataclass OrderItem with name, price and qty.
# 2. Add method cost.
# 3. Create a normal class Order(composition) that stores many OrderItems, can add item, is iterable, exposes properties coun and subtotal.
# 4. Create a base class Discount and subclasses: NoDiscount, PrecentageDiscount and FixedDiscount. Each must implement apply.
# 5. Add to Order method total_after(discount: Discount).
# 6. Write tests for subtotal, each discount type and polymorphys usage.

