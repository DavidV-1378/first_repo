from collections import deque

# Determine wether "( and )" match correctly. Ignore other charcters.

# "((( )))" "()()()"  retun true.
# )(), (() returns false.

def balanced_par(pars: str) -> bool:
    depth = 0
    for par in pars:
        if par == "(":
            depth += 1
        elif par == ")":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0

# Including "[]" and "{}".

def balnaced_del(dels: str) -> bool:
    closing_for: dict = {
        "(": ")",
        "[": "]",
        "{": "}"        
    }

    opened_dels: list[str] = []
    for dele in dels:
        if dele in closing_for:
            opened_dels.append(closing_for[dele])
        elif dele in ")]}":
            if not opened_dels:
                return False
            if opened_dels.pop() != dele:
                return False
    return not opened_dels

# Process request in arrival order. 

def process_in_order(requests: list[str]) -> list[str]:
    queue = deque(requests)
    processed = []

    while queue:
        processed.append(queue.popleft())
    return processed 

# In postfix notation, an operator comes after the two values it uses. 
# Example: "3 4 +" means 3 + 4. "3 4 + 2 *" means (3 + 4) * 2

def evaluate_postfix(expression: str) -> int:
    stack = []
    for token in expression.split():
        if token not in {"+", "-", "*"}:
            try:
                stack.append(int(token))
            except ValueError:
                raise ValueError("Invalid token")
            continue
        if len(stack) < 2:
            raise ValueError("Not enough operands")
        right = stack.pop()
        left = stack.pop()
        if token == "+":
            total = right + left
        elif token == "-":
            total = left - right
        else:
            total = right * left
        stack.append(total)
    if len(stack) != 1:
        raise ValueError("Stack has too many elements")
    return stack.pop()


# 3, no, [3]
# 4, no, [3, 4]
# +, right = 4, left = 3 [7]
# 2, no [7, 2]
# *, [14]


# Each task gets at most q units of processing. 
# Unfinshed tasks return to the back of the queue.
# Return completion order.

tasks = [("a", 5), ("b", 2), ("c", 3)]
q = 2

def task_completion_order(tasks: list[tuple[str, int]], q: int) -> list[str]:
    if q <= 0:
        raise ValueError("q must be positive")
    if any(work <= 0 for _,work in tasks):
        raise ValueError ("Work must be positive")

    queue = deque(tasks)
    complition_order = []

    while queue:
        name, remaning = queue.popleft()
        remaning -= min(q, remaning)
        if remaning == 0:
            complition_order.append(name)
        else:
            queue.append((name, remaning))
    return complition_order


