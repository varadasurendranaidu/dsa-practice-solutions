
# DSA Practice Solutions and Unit Tests

A Python repository containing readable implementations of
common data structures and algorithms problems, with automated
unit tests for correctness and edge-case handling.

## Algorithms Implemented

### 1. Duplicate Detection
Checks whether a list contains repeated values using a set.

- Time complexity: O(n) average
- Space complexity: O(n)

### 2. Two Sum
Finds two distinct indices whose values add up to a target,
using a dictionary to store previously visited values.

- Time complexity: O(n) average
- Space complexity: O(n)

### 3. Binary Search
Searches for a target in an ascending sorted list by repeatedly
halving the search interval.

- Time complexity: O(log n)
- Auxiliary space complexity: O(1)

## Tech Stack

- Python 3
- unittest
- Git and GitHub

## Project Structure

```text
dsa-practice-solutions/
├── solutions.py
├── test_solutions.py
├── README.md
└── .gitignore
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/dsa-practice-solutions.git
cd dsa-practice-solutions
```

No external Python packages are required.

## Run the Example Solutions

```bash
python3 solutions.py
```

## Run Unit Tests

```bash
python3 -m unittest -v
```

The test suite checks normal inputs, empty lists, missing
results, negative numbers, and other edge cases.

## Design Decisions

- Sets provide efficient average-case duplicate detection.
- A dictionary allows Two Sum to look up complements efficiently.
- Binary search uses an iterative approach to maintain constant
  auxiliary space.
- unittest provides repeatable checks without external dependencies.

## Limitations

- Two Sum returns one valid pair, not every possible pair.
- Binary search requires input sorted in ascending order.
- Duplicate detection assumes values are hashable.
- Time-complexity claims describe typical algorithmic behavior,
  not guaranteed execution time for every input.

## Future Improvements

- Add more array, string, and searching problems.
- Add randomized tests and performance benchmarks.
- Organize solutions by topic and difficulty.
- Introduce continuous integration to run tests automatically.

## Author

Varada Surendra Naidu
