from Utils.math_utils import add
import Utils.math_utils as mu
from Utils.string_utils import shout, whisper
from Utils.string_utils import *
from counter import counts_to

result: int = mu.add(1,5)
print(result)

print(add(3,7))

result_1: int = mu.add(2,9)
print(result_1)

print(__name__)

def run_program() -> None:
    print(counts_to(5))
    shouting: str = shout("hello")
    print (shouting)
    print(whisper(shouting))
    result: int = mu.add(1,5)
    print(result)
    print("Program Entry_2")

if __name__ == "__main__":
    run_program()

