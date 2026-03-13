from dataclasses import dataclass

# HW1:

@dataclass(frozen = True)
class Book:
    title: str
    genre: str
    price: float

    def __post_init__(self) -> None:
        if not self.title:
            raise ValueError("Title must not be empty")
        if not self.genre:
            raise ValueError("Genre must not be empty")
        if self.price < 0:
            raise ValueError("Price can't be negative")
        

class BookStore:
    def __init__(self) -> None:
        self.books: list = []
        self.genre_counts: dict = {}

    def add_book(self, book: Book):
        self.books.append(book)

        if book.genre in self.genre_counts:
            self.genre_counts[book.genre] += 1
        else:
            self.genre_counts[book.genre] = 1

    def get_count_by_genre(self, genre: str) -> int:
        return self.genre_counts.get(genre.strip(), 0)
    
    def total_books(self) -> int:
        return len(self.books)
    


# HW2:

@dataclass(frozen = True)
class Student:
    name: str
    group: str
    garde: int

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("Name must not be empty")
        if not self.group:
            raise ValueError("Group must not be empty")
        if not 0 <= self.garde <= 10:
            raise ValueError("Garde msut be between 0 and 10 (inclusive)")
        

class CourseRoster:
    def __init__(self) -> None:
        self.student_list: list[Student] = []
        self.groups: dict[str, list[Student]] = {}

    def add_student(self, student: Student) -> None:
        self.student_list.append(student)

        group_name = student.group.strip().upper()
        if group_name not in self.groups:
            self.groups[group_name] = []
        
        self.groups[group_name]. append(student)

    def get_student_in_group(self, group_name: str) -> list[Student]:
        return self.groups.get(group_name.strip(), [])
    
    def total_count(self) -> int:
        return len(self.student_list)
    

# HW3:

@dataclass
class OrderItem:
    name: str
    price: float
    qty: int

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("Name must not be empty")
        if self.price < 0:
            raise ValueError("Price can't be negative")
        if self.qty <= 0:
            raise ValueError("Quantity can't be negative")
        
    def total(self) -> float:
        return self.price * self.qty

class Order:
    customer_id: str
    
    def __init__(self, customer_id: str):
        self.customer_id = customer_id
        self.items = []

    def add_item(self, item: OrderItem):
        self.items.append(item)

    def __post_init__(self):
        if not self.customer_id:
            raise ValueError("Customer ID must not be empty")
        if not self.items:
            raise ValueError("An order must have at least one item")
        
    def total_price(self) -> float:
            return sum(item.total for item in self.items)
        

class OrderManager:
    def __init__(self) -> None:
        self.orders: list[Order] = []
        self._customer_revenue: dict = {}

    def add_order(self, order: Order):
        self.orders.append(order)
        customer_id = order.customer_id

        revenue = order.total_price
        self._customer_revenue[order.customer_id] = self._customer_revenue.get(customer_id, 0.0) + revenue

    def total_revenue(self) -> float:
            return sum(self._customer_revenue.values())
        
    def revenue_for_customers(self, customer_id: str) -> float:
            return self._customer_revenue.get(customer_id, 0.0)
        
    def top_n_customers(self, n: int):
        sorted_revenue = sorted(
           self._customer_revenue.items(),
           key=lambda item:item[1],
           reverse = True
        )
        return sorted_revenue[:n]

    
    # HW 4:

    # 1. When there aren't many entires or there aren't many requests for the stored data.
    # 2. When there are many entires or there are a lot of request for the stored data.
    # 3. If index was used for a procces, the process will not work anymore.
    