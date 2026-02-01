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
   e
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
