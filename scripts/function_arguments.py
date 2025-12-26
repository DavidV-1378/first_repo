# f(10, 20, x = 30)


# packing
def f(*args): # * -> pack or unpack
    print(args)

f(1, 2, 3)


# unpacking
values = (1, 2 ,3)

f(*values)


def f(**kwargs):
    print(kwargs)

f(x = 20, y = 15)


options = {"host": "localhost", "port": 1001}

# == connect("host": "localhost", "port": 1001)
# connect(**options) 

def f(a, b, *args, c = 10, **kwargs):
    print(args, kwargs)

f(5, 7, 8, 9, 10, c = 11, d = 12, e = 13)
f(5, 7, c = 11)
# f(5, c = 3)

def outer(*args, **kwargs):
    return inner(*args, **kwargs) # argument forwarding

def total(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s

print(total(2, 5, 9, 11))


def configure(**options):
    timeout = options.get("timeout", 10)
    retires = options.get("retries", 3)
    print(timeout, retires)

configure(timeout = 20)


def debug(func):
    def wrapper(*args, **kwargs):
        print(f"arguments:{args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper


# Write a function count args that returns total number of argumnts passed

def count_args(*args, **kwargs):
    return len(args) + len(kwargs)

print(count_args(3, 6, 8, c = 34, d = 12))

# Write a decorator that prints "calling <function name>"" with
# <n> positional arguments and <m> keywords arguments

def function_call(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__} with {len(args)} positional arguments and {len(kwargs)} keyword arguments")
        return func(*args, **kwargs)
    return wrapper

@function_call
def add(a = 5, b = 7):
    return a + b

print(add(8, b = 6))

#Implement a function "send e-mail" that has a positional parameter "to" of type str
#two keyword onlt parameters "subject" and "body", both of type str, that prints the following
#info: "to:<to> subject:<subject> body: <body>"

def send_email(to: str, *, subject: str, body: str) -> None:
    print(f"to:{to} subject:{subject} body:{body}")

send_email("David", subject = "python", body = "python 1234")

#Implement a decorator "memoize_with_stats" that:
#Works for any function signature
#Caches results by a key derived from "args, kwargs"
#On each call it prints "<func name>: calls = <n> hits = <h> misses = <k>"
#Returns the cached value if available, otherwise computes, stores and retuns it
#Add a method "clear cache" that empties the cache and resets stats
from typing import Any, cast

def memoize_with_stats(func):
    cache = {}
    calls: int = 0
    hits: int = 0
    misses: int = 0
    def make_key(args, kwargs):
        return args, tuple(sorted(kwargs.items()))
    def cache_clear() -> None:
        nonlocal hits, misses, calls
        calls = 0
        hits = 0
        misses = 0
        cache.clear()
    def wrapper(*args, **kwargs):
        nonlocal calls, hits, misses
        key = make_key(cast(tuple[Any, ...],args), cast(dict[str, Any], kwargs))
        calls += 1
        if key in cache:
            hits += 1
            print(f"HIT: {func.__name__}: calls = {calls} hits = {hits} misses = {misses}")
            return cache[key] 
        misses += 1
        result = func(*args, **kwargs)
        cache[key] = result
        print(f"MISS: {func.__name__}: calls = {calls} hits = {hits} misses = {misses}")
        return result
    setattr(wrapper, "cache_clear", cache_clear)
    return wrapper

@memoize_with_stats
def fib(n): 
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(3))
fib.cache_clear()


@memoize_with_stats
def add(a, b):
    return a + b
print(add(2, 3))
add.cache_clear()
print(add(2, 3))