# Review rules

Flag as a high-severity finding:

1. Hardcoded secrets: API keys, tokens, passwords or private keys in source files.
2. Any new function in `src/` that has no matching test in `tests/`.
3. Use of `eval()` or `exec()`.
4. `print()` debugging left in `src/` (only `if __name__ == "__main__"` output is allowed).
