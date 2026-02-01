# Bracket Syntax Validator

A CLI tool that validates whether brackets `()`, `[]`, and `{}` in a string are correctly balanced and matched.

## Overview

The validator uses a **stack** to check that:

- Every opening bracket has a matching closing bracket
- Pairs are properly nested (e.g. `[()]` is valid; `[(])` is not)
- There are no unmatched opening or closing brackets

Only the characters `{`, `}`, `(`, `)`, `[`, and `]` are considered; all other characters in the input are ignored.

## Requirements

- Python 3.x
- The local `Stack` implementation from `Stack.Stack` (see `EASY/Stack/`)

## Usage

From the project root (or from `EASY/` with the right `PYTHONPATH`), run:

```bash
# Show help
python -m EASY.validator

# Validate a string
python -m EASY.validator validate "<your_syntax_string>"
```

Or from inside the `EASY` directory:

```bash
python validator.py validate "<your_syntax_string>"
```

### Examples

```bash
# Valid
python validator.py validate "[]"
# → valid

python validator.py validate "[({})]"
# → valid

python validator.py validate "hello [world] (test)"
# → valid  (non-bracket characters are ignored)

# Invalid
python validator.py validate "]["
# → Unclosed ] at index 1

python validator.py validate "[)"
# → Error: Expected ], found ) at index 1

python validator.py validate "(["
# → Error: unclosed opening -> ( at index 0
```

## Behavior

| Input situation              | Output |
|-----------------------------|--------|
| All brackets matched        | `valid` |
| Extra closing bracket       | `Unclosed <char> at index <i>` |
| Wrong closing bracket       | `Error: Expected <expected>, found <char> at index <i>` |
| Unclosed opening bracket(s) | `Error: unclosed opening -> <char> at index <i>` |

## Implementation

- **Stack**: Opening brackets are pushed onto a stack with their index. When a closing bracket is seen, the stack is popped and the type is checked. Any mismatch or leftover symbols is reported with the relevant index.
- **CLI**: Implemented with `argparse`; the only subcommand is `validate`, which takes a single positional argument `syntax` (the string to validate).

## File

- `validator.py` — Entry point and validation logic (uses `Stack.Stack`).












