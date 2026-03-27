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




