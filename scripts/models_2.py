from enum import Enum
from dataclasses import dataclass

# Build an expense system, where categories are a Enum(food, transport, books, fun, other)
# Expense stores date, category, amount and note.
# Ledger stores many Expenses and supports len, Expense in ledger and if Ledger, method by_category that retuns dict[category, float]

class Category(Enum):
    FOOD = "food"
    TRANSPORT = "transport"
    BOOKS = "books"
    FUN = "fun"
    OTHER = "other"

@dataclass(frozen = True)
class Expense:
    date: str
    category: Category
    amount: float
    note: str

    def __post_init__(self) -> None:
        if not self.date.strip():
            raise ValueError("Date must not be empty.")
        if self.amount <= 0: 
            raise ValueError("Amounr cannot be zero or negative.")
        
class Ledger:
    def __init__(self) -> None:
        self._expenses: list[Expense] = []

    def add(self, expense: Expense) -> None:
        self._expenses.append(expense)

    def __len__(self) -> int:
        return len(self._expenses) 
    
    def __contains__(self, expense: Expense) -> bool:
        return expense in self._expenses
    
    def __bool__(self) -> bool:
        return len(self._expenses) > 0 
    
    def by_category(self) -> dict[Category, float]: 
        total: dict[Category, float] = {}
        for expense in self._expenses:
            total[expense.category] = total.get(expense.category, 0.0) + expense.amount
        return total
    
# Build a quizz system with a difficulty Enum(easy = 1, medium  = 2, hard = 3)
# Question class stores prompt, answer and difficulty properties and implements custom equlity, comparing by prompt text
# QuestionBank class stores many questions and supports len, question in bank, bank empty, filter by a difficulty -> list[Question]

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class Question():
    def __init__(self, prompt: str, answer: str, difficulty: Difficulty) -> None:
        cleaned_prompt = prompt.strip()
        if not cleaned_prompt:
            raise ValueError("Promopt must not be empty")
        
        cleaned_asnwer = answer.strip()
        if not cleaned_asnwer:
            raise ValueError("Answer must be given")
        
        self._prompt = cleaned_prompt
        self._answer = cleaned_asnwer
        self._difficulty = difficulty

    def __eq__(self, q2: object) -> bool:
        if not isinstance(q2, Question):
            return NotImplemented
        return self._prompt == q2._prompt
    
    @property
    def prompt(self) -> str:
        return self._prompt
    
    @property
    def answer(self) -> str:
        return self._answer
    
    @property
    def difficulty(self) -> Difficulty:
        return self._difficulty
    
    def __repr__(self) -> str:
        return f"Question(prompt={self._prompt},answer={self._answer}, difficulty={self._difficulty.name})"
    

class QuestionBank():
    def __init__(self) -> None:
        self._questions: list[Question] = []

    def fliter_by_difficulty(self, difficulty: Difficulty) -> list[Question]:
        return [q for q in self._questions if q.difficulty == difficulty]
    
    def add(self, q: Question) -> None:
        self._questions.append(q)
        