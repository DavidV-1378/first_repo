from dataclasses import dataclass
from enum import Enum

class Product:
    def __init__(self, name: str, price: float) -> None:
        self._name: str = name
        self._price: float = price

    def __repr__(self) -> str:
        return f"Product(name: {self._name}, price: {self._price})"
    
    def __str__(self) -> str:
        return f"{self._name} - {self._price:.2f}"
    

product_1 = Product("product_1", 10.0)

print(product_1)

print(repr(product_1))

print(str(product_1))

class Temperature:
    def __init__(self, temperature_in_celcius: float) -> None:
        self._temperature_in_celcius: float = temperature_in_celcius

    @property
    def temperature_in_celcius(self) -> float:
        return self._temperature_in_celcius
    
    @classmethod
    def from_ferenheit(cls, f: float) -> Temperature:
        return cls((f - 32) * 5/9)
    

temperature_1 = Temperature(22.0)

print(temperature_1.temperature_in_celcius)

temperature_2 = Temperature.from_ferenheit(110.0)

print(temperature_2.temperature_in_celcius)


class Colour:
    def __init__(self, r: int, g: int, b: int) -> None:
        self._r: int = r
        self._g: int = g
        self._b: int = b

    @classmethod
    def from_hex(cls, hex: str) -> Colour:
        hex = hex.lstrip("#")
        return cls(int(hex[0:2], 16), int(hex[2:4], 16), int(hex[4:6], 16))

    @classmethod
    def red(cls) -> Colour:
        return cls(255, 0, 0)

colour_1 = Colour.from_hex("#ff0000")
colour_red = Colour.red()

colour_2 = Colour(255, 100, 56)


class Duration:
    def __init__(self, in_minutes: int) -> None:
        self._in_minutes: int = in_minutes

    @classmethod
    def in_seconds(cls, seconds: int) -> Duration:
        return cls(int(seconds / 60))
    
    @classmethod
    def from_hours(cls, hours) -> Duration:
        return cls(int(hours * 60))
    
    @property
    def in_minutes(self) -> int:
        return self._in_minutes
    

time_1 = Duration(135)
time_2 = Duration.in_seconds(500)
time_3 = Duration.from_hours(4)

print(time_1.in_minutes, time_2.in_minutes, time_3.in_minutes)

## __len__
## When you call len(obj), python calls obj.__len__() behinde the scenes.

class Library:
    def __init__(self) -> None:
        self._books = []

    def add(self, title: str) -> None:
        self._books.append(title)

    def __len__(self) -> int:
        return len(self._books)

    #__contains__:

    def __contains__(self, title: str) -> bool:
        return title in self._books

    def __bool__(self) -> bool:
        return len(self._books) > 0


print("here")
library_1 = Library()
print(bool(library_1))
library_1.add("book_1")
library_1.add("book_2")

print(len(library_1))
print("book_1" in library_1)
print("python 101" in library_1)
print(bool(library_1))

#__eq__:
@dataclass(frozen = True)
class Point:
    x: float
    y: float


point_1 = Point(10.0, 9.0)
point_2 = Point(3.0, 6.0)

print(point_1 == point_2)

class Cordinate:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y
        
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cordinate):
            return NotImplemented
        return self._x == other._x and self._y == other._y
        
cordinate_1 = Cordinate(5, 7)
c2 = Cordinate(5, 7)

print(cordinate_1 == c2)
print(c2 == 5)

#Enum:

class Diff(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3    

class Question:
    def __init__(self, text: str, diff: Diff) -> None:
        self._text = text
        self._diff = diff
    
q = Question("2 + 2?", Diff.EASY)
print(q._diff.value)
for d in Diff:
    print(d.name, d.value)

level = Diff.EASY

print(level)
print(level.value)
print(level == Diff.MEDIUM)


