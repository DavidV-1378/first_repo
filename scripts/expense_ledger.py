# You are buliding a small cli(terminal) style expense ledger.
# Each input line is a raw record with format: "YYYY-MM-DD;category=<cat>;amount=<float>;note=<text>"
# Invalid lines may exist: missing fields, amount NaN(not a number), negative ot zero amount, category empty.
# 1. Create Class Expense, with fields: date, category, amount and note. Include validation for amount 0> and for catgory not empty.
# 2. Create Class Ledger that stpres a list of Expense, methods: addExpense, total, by_category and largest- top n by amount, descending.
# 3. Create function pasre_expense that retuns "None" for invalid lines.
# 4. In main, define raw_lines list with at least 5 lines, 2 invalid.
# Parse, add valid expenses, then print: total spent, total by category, top three expenses. 