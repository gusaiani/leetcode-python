## Project structure

- Implementation files: `src/<problem_name>.py` (e.g., `src/fibonacci_number.py`)
- Test files: `tests/<problem_name>_test.py` (e.g., `tests/fibonacci_number_test.py`)
- Branch name: kebab-case problem name (e.g., `fibonacci-number`)
- File and module names use `snake_case`.

Implementation file template:
```python
"""LeetCode <number>. <Title>.

<url>

<problem description>
"""


def <function_name>(<params>) -> <ReturnType>:
    _ = (<params>)
    raise NotImplementedError
```

Test file template:
```python
from src.<problem_name> import <function_name>


def test_example_1():
    assert <function_name>(<input>) == <expected>
```

Run tests:
- `uv run pytest` — run all tests
- `uv run pytest tests/<problem_name>_test.py` — run a single problem's test file
- `uv run pytest tests/<problem_name>_test.py -v` — verbose output

## Solved problems

Read `README.md` — the "Solved Problems" table is the source of truth for which problems are already solved here and what patterns/approaches they cover. Use the Approach column to infer covered patterns when doing gap analysis.

## Avoiding duplicates with the JS and Rust repos

This repo is a companion to `/Users/gustavosaiani/code/estudo/js/leetcode` and `/Users/gustavosaiani/code/estudo/rust/leetcode`. When picking a new challenge, also read those repos' `README.md` "Solved Problems" tables and **skip any problem already solved in either**. The goal is breadth across all three repos, not redundant coverage.

---

Use the term "Stub challenge" as a command to:

- create a branch named after the kebab-case problem
- create a test file at `tests/<problem_name>_test.py` with multiple test cases (cover examples + edge cases)
- create an implementation file at `src/<problem_name>.py` with a stubbed function body using `raise NotImplementedError`
- update `README.md`'s "Solved Problems" table with a new row marking the problem as stubbed (leave Approach/Time/Space as `—` until solved)
- open the editor with both files: `cursor tests/<problem_name>_test.py src/<problem_name>.py`

Do not give hints about how to solve the problem.

Use the term "Stub job challenge" as a command to:

1. Pick a LeetCode challenge that maximizes odds of passing a technical interview for a senior engineer role paying US$150–200k/year, remote from Brazil.
2. Consider which patterns and topics are missing from this repo **and** from the JS repo at `/Users/gustavosaiani/code/estudo/js/leetcode/README.md` **and** from the Rust repo at `/Users/gustavosaiani/code/estudo/rust/leetcode/README.md`. Skip any problem already solved in any of the three repos. Fill the most impactful gap (e.g., BFS, DFS, dynamic programming, sliding window, stack, trie, graph traversal, matrix problems, bit manipulation).
3. Difficulty mix: 50% easy, 40% medium, 10% hard.
4. "Stub challenge" from the choice of challenge above.
5. Explain why the chosen problem is relevant for senior interviews at that salary range, and call out the Python-specific learning value (decorators, generators, itertools, collections, typing, concurrency) when applicable.
