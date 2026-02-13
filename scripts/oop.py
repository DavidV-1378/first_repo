class A:
    def f(self, x:int) -> int:
        return x + 1
    
a = A() 
print(a.f(10)) # Python does A.f(a, 10)

class Counter:
    total = 0
    def __init__(self) -> None:
        Counter.total += 1
        self.value = 0 

# When we create an object of type class, we    INSTANTIATE an object, meaning we crate an instance

# ENCAPSULATION = hide internals, expose interface

class SafeCounter:
    def __init__(self) -> None:
        self.__value = 0
    def get(self) -> int:
        return self.__value
    def set(self, x:int) -> None:
        if x < 0:
            raise ValueError("x cannot be lower than 0")
        self.__value = x
        
a = SafeCounter()

a.__value = -3
# a.set(3)
print(a.get())