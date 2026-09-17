# Algorithmics Homework — B02-B05

## Working and submission rules

- Work on a homework branch, using the agreed pattern `hw/weekXX-<topic>`.
- Open a GitHub pull request to `main`. 
- For implementation tasks, write a 1-2 examples before coding and include automated tests. 
- Include ordinary inputs and relevant edge cases. Follow each task's specified contract; document any behavior left for you to decide.
- Keep explanations short and in your own words. A trace table or small diagram is welcome.

## B02 — Input Size, Repeated Work, and Growth

### H1 — Define the input sizes

For each task, state what `n` represents:

1. Scan a list of temperatures.
2. Inspect every character in a string.
3. Answer membership queries against registered usernames.

For the third task, also define `q` as a separate relevant size. Give one concrete input and its size values for each task.

### H2 — Operation-count table

Consider a left-to-right linear search for a target that is absent.

- Record the number of equality checks for list lengths `0`, `1`, `2`, `5`, and `10`.
- Describe the pattern in words.
- Then give its growth classification and notation.
- State which operation you counted; do not treat the count as milliseconds.

### H3 — Classify from counts

Consider these three operations on `values`:

1. Retrieve and return `values[0]`, with a non-empty-input contract.
2. Visit every value once in a single loop.
3. Visit every ordered pair using two full nested loops over the list.

For each:

- name the operation being counted;
- count it for `n = 1`, `2`, and `4`;
- classify its growth as constant, linear, or quadratic;
- explain the classification from your table.

### H4 — Best-case and worst-case inputs

For left-to-right list membership on a list of five items:

- give a best-case input and target;
- give a worst-case input and target;
- count the equality checks in both cases;
- explain why lists of the same length can require different amounts of work.

### H5 — Compare duplicate detectors

Implement two functions that return whether a list of integers contains a duplicate:

- `has_duplicate_slow`: a pair-comparison version;
- `has_duplicate_seen`: a version using a set of previously encountered values.

Both must return the same Boolean result for every valid input.

Required evidence:

- tests for empty input, all unique values, an early duplicate, and a late duplicate;
- a hand-count of pair comparisons for your slow version on a unique four-item list;
- a plain-language explanation of what the set represents;
- a time/extra-storage tradeoff explanation, without estimating exact byte counts.

### H6 — Integrator: repeated product lookups

Given a list of product IDs and a list of query IDs, produce one Boolean membership answer per query, in query order.

Implement:

- repeated membership checks against the original list;
- membership checks against one set prepared before answering the queries.

Confirm that both produce identical results. Include tests for empty products, empty queries, present and absent IDs, repeated queries, and duplicate product IDs.

Write a short explanation covering:

- what `n` and `q` mean;
- which approach is simpler for one query;
- which is better suited to many queries;
- what additional state the set-based approach stores;
- setup work versus query work.


## B03 — One-Pass Scans and Running State

### H1 — Trace the largest-value scan

Trace the discussed `largest` algorithm on `[3, 8, 2, 8, 5]`.

- Show the processed portion and `best` after every step.
- Include the initialization.
- Explain what `best` means at each point.

### H2 — Count even values

Implement `count_even(values)` for a list of integers.

- Return the number of even values.
- Handle empty input.
- Include zero and negative values in your tests.
- Complete: "After processing the first `i` values, `count` equals ..."
- Explain time and auxiliary-space complexity.

### H3 — Longest equal consecutive run

Implement `longest_equal_run(values)`.

- Return the length of the longest consecutive run of equal integers.
- Equal values separated by other values do not belong to the same run.
- Return `0` for empty input.

Test empty input, one item, all equal values, all different neighboring values, and a longest run at the beginning, middle, or end.

Submit a trace and explain the meaning of every state variable after a processed prefix. Include time and auxiliary-space complexity.

### H4 — Second-largest distinct value

Implement `second_largest_distinct(values)`.

- Return the second-largest distinct integer.
- Repeated copies of the largest value do not count as second place.
- Return `None` if fewer than two distinct values exist.
- Use the one-pass approach discussed rather than sorting.

Test empty input, one distinct value, exactly two distinct values, duplicates, negative values, and ordinary input. Explain the state meanings. If implementation remains difficult, submit a correct manual trace and your partial attempt.

### H5 — Integrator: ticket wait summary

Given integer ticket waiting times and a limit, return:

- the minimum wait;
- the maximum wait;
- the average wait;
- the zero-based index of the first wait strictly above the limit, or `None` if there is none.

Use one pass. Define and document empty-input behavior before coding.

Required evidence:

- examples and edge cases, including a wait exactly equal to the limit;
- a trace table;
- the meaning of every state variable;
- one combined invariant in ordinary language;
- an explanation of `O(n)` time and `O(1)` auxiliary space;
- automated tests.

### Optional — Best buy/sell profit

Given prices in chronological order, return the largest possible profit from buying once and selling on a later day. Return `0` when no profitable trade exists. Define behavior for fewer than two prices. Derive the state yourself, include a trace, and test increasing, decreasing, and repeated prices.

## B04 — Prefix Preprocessing and Repeated Queries

All ranges in this section use `[start, end)`: include `start`, exclude `end`. Valid boundaries satisfy `0 <= start <= end <= input length`, unless a task explicitly requires a non-empty range.

### H1 — Manual prefix table

Build prefix sums for `[3, -2, 5, 0, 4]`.

Answer these ranges using the completed table:

- `[0, 2)`;
- `[1, 4)`;
- `[2, 5)`;
- `[4, 4)`.

Show the boundary labels, the meaning of each prefix entry, and the calculation used for every query. Predict the results before checking them in Python.

### H2 — Count even values in ranges

Implement preprocessing for a list of integers so later queries can report the number of even values in any valid half-open range.

- Reuse the discussed range-query interface where appropriate.
- Cover the full range, a single item, an empty range, zero, and negative integers.
- Define invalid-range behavior.
- Explain preprocessing time, query time, and extra space separately.

### H3 — Vowel range queries

Given a string, preprocess it so queries can report how many vowels occur in `text[start:end]`.

- Treat `a`, `e`, `i`, `o`, and `u` as vowels, in either case.
- Do not count other characters as vowels.
- Support valid empty ranges.
- Test empty text, uppercase/lowercase vowels, no vowels, punctuation, and boundary ranges.
- Explain preprocessing and per-query costs.

### H4 — Compare direct and prefix solutions

Implement a direct range-sum function and a prefix-based query version.

- Generate deterministic input and valid queries.
- Verify that both produce identical results for every query.
- Measure prefix construction, direct queries, and prefix queries separately.
- Do not rebuild the prefix index inside every query.
- Record `n`, the number of queries `q`, and the timing setup.
- Explain the time/memory tradeoff and when preprocessing is justified.

### H5 — Integrator: sensor query service

Create a small class that receives sensor readings and an alert threshold once, then answers interval-summary queries.

Each non-empty query must return:

- total of the readings;
- average of the readings;
- number of readings at or above the threshold.

Requirements:

- Use the preprocessing techniques taught in class.
- Reject invalid and empty summary ranges consistently.
- Test full range, single item, invalid range, and a range with no alerts.
- Explain construction time, query time, and stored space.
- Add a short design note explaining whether the index is a snapshot, what happens if the caller later changes the original list, and whether updates are supported.


## B05 — Two Pointers and Monotonic Progress

### H1 — Manual pair-sum trace

Trace `pair_sum_sorted([1, 2, 4, 7, 11, 15], 15)` using the algorithm discussed.

Include columns for:

- `left` and its current value;
- `right` and its current value;
- pair sum;
- pointer movement or return decision.

Explain why each movement is safe. The function returns two different indices, not the pair of values.

### H2 — Normalized palindrome

Implement `normalized_palindrome(text)`.

- Ignore non-alphanumeric characters.
- Compare without regard to case.
- Return a Boolean.
- Do not first construct an entirely normalized copy of the string.
- Treat empty text, or text with no alphanumeric characters, as a palindrome.

Test empty input, one character, mixed case, punctuation, digits, a palindrome, and a non-palindrome. Explain pointer movement, the invariant, and complexity.

### H3 — Remove duplicates from sorted values in place

Implement `deduplicate_sorted(values)` for integers sorted in ascending order.

- Modify the existing list so its beginning contains each distinct value once, in sorted order.
- Return the new logical length.
- Only the prefix up to that length is part of the result; the unused tail need not be cleared.
- Do not create a full copied result or use a set to replace the read/write exercise.

Test empty input, one item, all duplicates, no duplicates, and several duplicate groups. Explain the pointer meanings, invariant, and complexity.

### H4 — Merge timestamped readings

Merge two lists of readings, each already ordered by timestamp, into a new timestamp-ordered list.

- Preserve every reading, including those with equal timestamps.
- When timestamps tie, readings from the first input must appear before readings from the second.
- Preserve the original order within each input for equal timestamps.
- Do not change the inputs or sort the combined list as a substitute for merging.

Choose and document a reading representation. Test empty inputs, interleaved timestamps, one exhausted input, and timestamp ties. Explain the invariant and costs in terms of the two input lengths.

### H5 — Integrator: best pair under budget

Given sorted integer item prices and a budget, return the pair of prices with the largest total that does not exceed the budget.

- Use two different positions; equal prices are allowed if they occur at different positions.
- Return `None` if no pair qualifies.
- Define a deterministic rule for ties between equally good pairs.
- Use the two-pointer approach discussed 
- Ensure a later, lower-total valid pair cannot replace a better answer already found.

Submit examples, tests, a manual trace, an invariant, a tie-contract note, and an `O(n)` time explanation.

Include tests for fewer than two prices, no valid pair, a total exactly equal to the budget, duplicate prices, tied best totals, and large gaps between neighboring prices.

### Optional stretch — Online-judge two-pointer task

Solve one canonical two-pointer problem on an online judge. Submit the link, reasoning written before coding, additional tests, and complexity. Do not use AI or an editorial before acceptance or a documented 45-minute independent attempt.
Examples of online judge problems: 
1. Leetcode: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
2. HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem - Solve it with the one-pass reasoning from class, not by sorting.
3. CSES - https://cses.fi/problemset/task/1069
4. Kattis (https://open.kattis.com/problems) - Initially browse problems around difficulty 1.0–2.0
Feel free to do more than 1!