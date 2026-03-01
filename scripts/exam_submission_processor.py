# ============================================================
# Exam Submission Processor
# ============================================================

"""
You are building a small helper for processing exam submissions
in a university grading system.

Each submission comes as a raw string with the following format:

    "student_id=<id>;score=<score>;status=<status>"

Example:
    "student_id=ST123;score=87;status=submitted"

Where:
- student_id is a non-empty string
- score is an integer between 0 and 100 (inclusive)
- status must be one of: "submitted", "late"

The system is noisy and may produce invalid submissions.
"""

# ------------------------------------------------------------
# Data setup
# ------------------------------------------------------------

"""
1. Create a list raw_submissions with at least 6 strings.

The list MUST contain:
- at least 2 different student_id values
- at least 2 INVALID lines (wrong format, missing fields, wrong types, etc.)
- at least 1 line with an INVALID status (not "submitted" or "late")
"""

raw_submissions: list[str] = [
   
]

# ------------------------------------------------------------
# 1) Parsing and validation
# ------------------------------------------------------------

"""
Write a function:

    def parse_submission(line: str) -> dict[str, object]

The function must:
- parse ONE submission line
- return a dictionary with keys:
    "student_id": str
    "score": int
    "status": str

Rules:
- If the line structure is invalid, raise ValueError.
- If score cannot be converted to int, raise ValueError.
- If score is outside [0, 100], raise ValueError.
- If status is not "submitted" or "late", raise ValueError.
- Any ValueError message MUST include the original line.
"""

def parse_submission


# ------------------------------------------------------------
# 2) Safe parsing wrapper
# ------------------------------------------------------------

"""
Write a function:

    def safe_parse_submission(line: str) -> dict[str, object] | None

Behavior:
- Calls parse_submission(line)
- If parse_submission raises ValueError:
    * print: "Skipping invalid submission: <error message>"
    * return None
- Otherwise, return the parsed dictionary
"""

def safe_parse_submission


# ------------------------------------------------------------
# 3) Closure: Per-student average calculator
# ------------------------------------------------------------

"""
You now want to compute averages per student.

Write a function:

    def make_student_averager(student_id: str)

That returns a function add_score(score: int) -> float which:
- keeps track of all scores for THAT student using a closure
- every time it is called:
    * adds the score
    * returns the current average score for that student

IMPORTANT:
- Use a closure.
- Use nonlocal.
- The returned function must take exactly ONE argument.
"""

def make_student_averager


# ------------------------------------------------------------
# 4) Decorator: Reject late submissions
# ------------------------------------------------------------

"""
Late submissions should not be processed automatically.

Write a decorator:

    def reject_late(func)

The decorator must wrap a function that takes ONE argument:
    submission: dict[str, object]

Behavior of the wrapper:
- If submission["status"] == "late":
    * print: "Submission rejected (late)"
    * return None
- Otherwise:
    * call the original function
    * return its result

IMPORTANT:
- Do NOT modify the decorated function.
- Do NOT use *args or **kwargs.
"""

def reject_late


# ------------------------------------------------------------
# 5) Decorator FACTORY: Score access control (HARD)
# ------------------------------------------------------------

"""
Only instructors with sufficient permission may process high scores.

Write a DECORATOR FACTORY:

    def require_min_permission(level: int)

Usage example:

    @require_min_permission(5)
    def process_submission(submission: dict[str, object]) -> None:
        ...

Behavior:
- require_min_permission(level) returns a decorator.
- The decorator wraps a function that takes ONE argument:
      submission: dict[str, object]

The wrapper must:
- assume submission contains a key "permission_level" (int)
- if submission["permission_level"] < level:
    * raise PermissionError("Insufficient permission")
- otherwise:
    * call the original function
    * return its result

IMPORTANT:
- This MUST be a decorator factory.
- Use closures.
- Do NOT use global variables.
"""

def require_min_permission


# ------------------------------------------------------------
# 6) Processing pipeline
# ------------------------------------------------------------

"""
Write a function:

    def process_submissions(lines: list[str]) -> dict[str, float]

The function must:
- iterate over raw submission lines
- safely parse each line
- ignore invalid and late submissions
- compute the FINAL AVERAGE SCORE per student
- return a dictionary:
      student_id -> average_score

Rules:
- Use closures from make_student_averager
- Use dictionaries to manage per-student state
- The function must NOT crash due to invalid input
"""

def process_submissions


# ------------------------------------------------------------
# 7) Demo section
# ------------------------------------------------------------

"""
In the __main__ section:
- Call process_submissions(raw_submissions)
- Print results like:
      Student ST123: average score = 82.5
"""

if __name__ == "__main__":
    # TODO: run processing and print results
    pass

from __future__ import annotations
from typing import Callable

from __future__ import annotations
from typing import Callable

# ============================================================
# Exam Submission Processor — CORRECTED REFERENCE SOLUTION
# ============================================================


# ------------------------------------------------------------
# Data setup
# ------------------------------------------------------------

raw_submissions: list[str] = [
    "student_id=ST001;score=80;status=submitted",
    "student_id=ST002;score=90;status=submitted",
    "student_id=ST001;score=70;status=submitted",
    "student_id=ST003;score=85;status=late",          # late
    "student_id=ST004;score=abc;status=submitted",    # invalid score
    "student_id=ST005;status=submitted",               # missing score
    "student_id=ST006;score=95;status=unknown",        # invalid status
]


# ------------------------------------------------------------
# 1) Parsing and validation
# ------------------------------------------------------------

def parse_submission(line: str) -> dict[str, object]:
    """
    Parse and validate ONE submission line.
    """
    try:
        parts = line.split(";")
        data: dict[str, str] = {}

        for part in parts:
            key, value = part.split("=")
            data[key] = value

        student_id = data["student_id"].strip()
        if not student_id:
            raise ValueError("Empty student_id")

        score = int(data["score"])
        if not (0 <= score <= 100):
            raise ValueError("Score out of range")

        status = data["status"]
        if status not in ("submitted", "late"):
            raise ValueError("Invalid status")

        return {
            "student_id": student_id,
            "score": score,
            "status": status,
        }

    except Exception as e:
        raise ValueError(f"Invalid submission line: {line}") from e


# ------------------------------------------------------------
# 2) Safe parsing wrapper
# ------------------------------------------------------------

def safe_parse_submission(line: str) -> dict[str, object] | None:
    """
    Safely parse a submission line.
    """
    try:
        return parse_submission(line)
    except ValueError as e:
        print("Skipping invalid submission:", e)
        return None


# ------------------------------------------------------------
# 3) Closure: Per-student average calculator (FIXED)
# ------------------------------------------------------------

def make_student_averager() -> Callable[[int], float]:
    """
    Returns a function that accumulates scores
    and returns the running average.
    """
    total = 0
    count = 0

    def add_score(score: int) -> float:
        nonlocal total, count
        total += score
        count += 1
        return total / count

    return add_score


# ------------------------------------------------------------
# 4) Decorator: Reject late submissions
# ------------------------------------------------------------

def reject_late(func: Callable[[dict[str, object]], None]) -> Callable[[dict[str, object]], None]:
    def wrapper(submission: dict[str, object]) -> None:
        if submission["status"] == "late":
            print("Submission rejected (late)")
            return None
        return func(submission)

    return wrapper


# ------------------------------------------------------------
# 5) Decorator FACTORY: Permission control
# ------------------------------------------------------------

def require_min_permission(level: int):
    def decorator(func: Callable[[dict[str, object]], None]):
        def wrapper(submission: dict[str, object]) -> None:
            permission_level = submission.get("permission_level", 0)
            if permission_level < level:
                raise PermissionError("Insufficient permission")
            return func(submission)

        return wrapper
    return decorator


# ------------------------------------------------------------
# 6) Processing pipeline (FIXED, NO HACKS)
# ------------------------------------------------------------

def process_submissions(lines: list[str]) -> dict[str, float]:
    """
    Process submissions and compute final average per student.
    """
    averagers: dict[str, Callable[[int], float]] = {}
    results: dict[str, float] = {}

    for line in lines:
        parsed = safe_parse_submission(line)
        if parsed is None:
            continue

        if parsed["status"] == "late":
            continue

        student_id = parsed["student_id"]
        score = parsed["score"]

        if student_id not in averagers:
            averagers[student_id] = make_student_averager()

        # Store the latest average returned by the closure
        results[student_id] = averagers[student_id](score)

    return results


# ------------------------------------------------------------
# 7) Demo section
# ------------------------------------------------------------

if __name__ == "__main__":
    results = process_submissions(raw_submissions)
    for student, avg in results.items():
        print(f"Student {student}: average score = {avg:.2f}")
