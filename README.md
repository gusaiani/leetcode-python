![Tests](https://github.com/gusaiani/leetcode-python/actions/workflows/test.yml/badge.svg)
![Lint](https://github.com/gusaiani/leetcode-python/actions/workflows/lint.yml/badge.svg)

# LeetCode in Python

Solutions to LeetCode problems in Python, each with a test suite.

Companion to the [JavaScript](https://github.com/gusaiani/leetcode-js) and [Rust](https://github.com/gusaiani/leetcode-rust) repos. Problems are not duplicated across the three — each new challenge here is one not yet solved in either sibling repo (see [Avoiding duplicates](#avoiding-duplicates)).

## Solved Problems

| #   | Problem                                                         | Difficulty | Approach | Time | Space |
| --- | --------------------------------------------------------------- | ---------- | -------- | ---- | ----- |
| 509 | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | Easy     | —        | —    | —     |

## Project structure

- Implementation: `src/<problem_name>.py`
- Tests: `tests/<problem_name>_test.py`

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/). Install uv if needed:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then:

```sh
uv sync
```

### Pre-push hook

A repo-tracked git hook at `.githooks/pre-push` runs the same checks CI runs (format, lint, test) before each `git push`. Enable it once per clone:

```sh
git config core.hooksPath .githooks
```

Bypass for a single push with `git push --no-verify`.

## Scripts

| Command                     | Description                 |
| --------------------------- | --------------------------- |
| `uv run pytest`             | Run all tests               |
| `uv run pytest tests/<name>` | Run a single problem's tests |
| `uv run ruff format`        | Format code                 |
| `uv run ruff format --check` | Check formatting            |
| `uv run ruff check`         | Lint                        |

## Workflow

1. Ask Claude to "Stub challenge `<problem>`" or "Stub job challenge".
2. Implement the function in `src/<problem_name>.py` — replace `raise NotImplementedError` with your solution.
3. Run `uv run pytest tests/<problem_name>_test.py` until green.
4. Update the row in [Solved Problems](#solved-problems): fill in Approach, Time, Space.
5. Commit on the problem branch and merge.

## Avoiding duplicates

Before picking a new challenge, check the "Solved Problems" tables in all three repos:

- This repo's [Solved Problems](#solved-problems)
- [JS repo](https://github.com/gusaiani/leetcode-js#solved-problems)
- [Rust repo](https://github.com/gusaiani/leetcode-rust#solved-problems)

Skip anything already solved in any of them.
