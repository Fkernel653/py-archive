# py-archive — Python Utilities Archive

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Ruff](https://img.shields.io/badge/code%20style-ruff-261230?logo=ruff&logoColor=white)](https://docs.astral.sh/ruff/)

A collection of Python utilities designed for easy copying and use in your own projects.

---

## 📚 Table of Contents

- [About This Repository](#about-this-repository)
- [Fast Functions](#fast-functions)
  - [I/O Operations](#fast_funcsio--fast-io)
  - [Collections Processing](#fast_funcscollections--fast-data-processing)
  - [String Operations](#fast_funcsstrings--fast-text-operations)
  - [Numeric Operations](#fast_funcsnumbers--fast-math-operations)
  - [Attribute Access](#fast_funcsattr--fast-attribute-operations)
  - [Search Operations](#fast_funcssearch--fast-search--membership)
  - [Type Checking](#fast_funcstypes--fast-type-checking)
- [Terminal Styling (colors)](#terminal-styling-colors)
  - [Basic Colors & Styles](#basic-colors--styles)
  - [Style Combinations](#style-combinations)
  - [Utility Functions](#utility-functions)
- [Customization](#customization)
- [Optimization Tips](#optimization-tips)
- [License](#license)

---

## About This Repository

Python is an easy programming language, but deploying projects can still be cumbersome. The author created these utilities to simplify project deployment, but due to their bulkiness, they can introduce issues when used as full dependencies.

**Therefore, the best approach is to browse the source code and copy only what you need.**

- **Author:** [Fkernel653](https://github.com/Fkernel653)
- **Repository:** [github.com/Fkernel653/py-archive](https://github.com/Fkernel653/py-archive)

---

## Fast Functions

High-performance alternatives to Python built-in functions — up to 10x faster, with zero dependencies.

### `fast_funcs.io` — Fast I/O

| Function | Built-in Alternative | Speed-up |
|----------|---------------------|----------|
| `echo()` | `print()` in loops | 5-10x |
| `write_lines()` | multiple `print()` calls | 10-20x |
| `fast_input()` | `input()` | 1.5-2x |

```python
from fast_funcs.io import echo, write_lines, fast_input

# Instead of: for i in range(1000): print(i)
write_lines(range(1000))  # One system call

# Instead of: print("Hello", "World")
echo("Hello", "World", sep=" - ")

# Instead of: name = input("Enter name: ")
name = fast_input("Enter name: ")  # With prompt support
```

### `fast_funcs.collections` — Fast Data Processing

| Function | Built-in Alternative | Speed-up |
|----------|---------------------|----------|
| `filter_fast()` | `filter()` + lambda | 1.5-2x |
| `map_fast()` | `map()` + lambda | 1.5-2x |
| `reverse_copy()` | `reversed()` + `list()` | 1.3x |
| `sort_inplace()` | `sorted()` (when copy not needed) | 1.5x |
| `flatten()` | nested loops or `sum(list, [])` | 2-5x |

```python
from fast_funcs.collections import filter_fast, map_fast, reverse_copy, sort_inplace, flatten

# Instead of: list(filter(lambda x: x > 0, data))
positive = filter_fast(data, lambda x: x > 0)

# Instead of: list(map(lambda x: x * 2, data))
doubled = map_fast(data, lambda x: x * 2)

# Instead of: list(reversed(my_list))
reversed_list = reverse_copy(my_list)

# Instead of: sorted(my_list) (when you don't need original)
sort_inplace(my_list)

# Instead of: [item for sublist in nested for item in sublist]
flat = flatten([[1,2], [3,4], [5,6]])  # [1,2,3,4,5,6]
```

### `fast_funcs.strings` — Fast Text Operations

| Function | Built-in Alternative | Speed-up |
|----------|---------------------|----------|
| `join_strings()` | `+=` in loops | 10-100x |
| `buffer_join()` | `+=` in loops | 10-100x |
| `translate_replace()` | multiple `replace()` calls | 2-5x |
| `strip_newline()` | `strip()` (when only \n) | 1.5-2x |

```python
from fast_funcs.strings import join_strings, buffer_join, translate_replace, strip_newline

# Instead of: result = ""; for s in strings: result += s
result = join_strings(strings)

# Instead of: text.replace("a", "x").replace("b", "y")
result = translate_replace(text, {"a": "x", "b": "y"})

# Instead of: line.strip()  # removes all whitespace
line = strip_newline(line_with_nl)  # only removes \n

# Buffer building in loops
builder = []
for i in range(1000):
    builder.append(str(i))
result = buffer_join(builder, ",")
```

### `fast_funcs.numbers` — Fast Math Operations

| Function | Built-in Alternative | Speed-up |
|----------|---------------------|----------|
| `sum_precise()` | `sum()` for floats | More accurate + same speed |
| `square()` | `pow(x, 2)` or `x**2` | 1.3-1.5x |
| `fast_round()` | `round()` | 1.2-1.5x |

```python
from fast_funcs.numbers import sum_precise, square, fast_round

# Instead of: sum([0.1, 0.2, 0.3])  # 0.30000000000000004
total = sum_precise([0.1, 0.2, 0.3])  # 0.6

# Instead of: pow(5, 2) or 5**2
squared = square(5)  # 25

# Instead of: round(3.14159, 2)
rounded = fast_round(3.14159, 2)  # 3.14
```

### `fast_funcs.attr` — Fast Attribute Operations

| Function | Built-in Alternative | Speed-up |
|----------|---------------------|----------|
| `get_direct()` | `getattr()` | 1.5-2x |
| `has_direct()` | `hasattr()` | 1.5-2x |
| `set_direct()` | `setattr()` | 1.5-2x |
| `del_direct()` | `delattr()` | 1.5-2x |
| `repr_attrs()` | manual `__repr__` | Cleaner code |

```python
from fast_funcs.attr import get_direct, has_direct, set_direct, del_direct, repr_attrs

# Faster attribute access (bypasses MRO)
class User: pass
user = User()
set_direct(user, "name", "Alice")
set_direct(user, "age", 30)

print(has_direct(user, "name"))  # True
print(get_direct(user, "name", "Unknown"))  # "Alice"
print(repr_attrs(user, "name", "age"))  # User(name='Alice', age=30)

del_direct(user, "age")
print(has_direct(user, "age"))  # False
```

### `fast_funcs.search` — Fast Search & Membership

| Function | Built-in Alternative | Use Case |
|----------|---------------------|----------|
| `any_early()` | `any()` | Early exit control |
| `build_index_map()` | manual dict | O(1) lookups |
| `to_set()` | `set()` | Fast membership |

```python
from fast_funcs.search import build_index_map, to_set, any_early

# Build index for O(1) lookups
index = build_index_map(["a", "b", "c"])  # {"a":0, "b":1, "c":2}

# Convert once for repeated checks
unique_items = to_set(data)

# Early exit on first match
if any_early(items, lambda x: x > 100):
    print("Found large number")
```

### `fast_funcs.types` — Fast Type Checking

| Function | Built-in Alternative | Speed-up |
|----------|---------------------|----------|
| `is_exact_type()` | `isinstance()` | 1.5-2x |
| `is_one_of()` | `isinstance(x, tuple)` | 1.5-2x |

```python
from fast_funcs.types import is_exact_type, is_one_of

# Faster than isinstance() when inheritance not needed
if is_exact_type(value, int):
    print("Exactly an int, not a subclass")

# Check against multiple types
if is_one_of(value, (int, float, str)):
    print("Value is int, float, or str")
```

---

## Terminal Styling (colors)

ANSI escape codes for terminal output formatting. Supports 16 colors, 8 text styles, background colors, and all combinations.

### Basic Colors & Styles

```python
from colors import RED, GREEN, BLUE, BOLD, UNDERLINE, RESET

print(f"{BOLD}{RED}Error:{RESET} Something went wrong")
print(f"{GREEN}Success!{RESET}")
print(f"{UNDERLINE}{BLUE}Link{RESET}")
```

### Style Combinations

```python
from colors import BOLD_RED, ITALIC_BLUE, DIM_GREEN, BG_YELLOW

print(f"{BOLD_RED}Critical Error")
print(f"{ITALIC_BLUE}Note:")
print(f"{BG_YELLOW}{BOLD_BLACK}Warning{RESET}")
```

### Utility Functions

```python
from colors.utils import styled, success, error, warning, info

# Pre-formatted messages
print(error("File not found"))      # Error: File not found (bold red)
print(success("Download complete")) # Success: Download complete (bold green)
print(warning("Low disk space"))    # Warning: Low disk space (bold yellow)
print(info("Processing 3 files"))   # Info: Processing 3 files (bold cyan)

# Custom styling
print(styled("Custom text", BOLD, GREEN, BG_BLACK))
```

---

## Customization

Since this is a **copy-paste archive**, you should customize the code for your specific needs:

### Remove Unused Features

```python
# If you only need basic colors, delete all BOLD_*, ITALIC_*, etc.
# Keep only what you use:

# Before (full file)
BOLD_RED = "\033[1;31m"
ITALIC_BLUE = "\033[3;34m"
# ... hundreds of lines

# After (customized)
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"
# Just 3 lines!
```

### Disable Styling on Non-TTY

```python
import sys

# Auto-disable colors when output is piped or redirected
if not sys.stdout.isatty():
    RED = GREEN = BOLD = RESET = ""
else:
    RED = "\033[31m"
    GREEN = "\033[32m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
```

### Create Your Own Presets

```python
# Custom color scheme for your project
COLORS = {
    'debug': '\033[90m',    # gray
    'info': '\033[36m',     # cyan
    'warn': '\033[33m',     # yellow
    'error': '\033[31m',    # red
    'fatal': '\033[1;31m',  # bold red
    'reset': '\033[0m',
}

def log(level, msg):
    print(f"{COLORS[level]}[{level.upper()}]{COLORS['reset']} {msg}")
```

---

## Optimization Tips

### 1. Avoid Importing Unused Code

```python
# Bad - imports everything
from fast_funcs import *

# Good - import only what you need
from fast_funcs.strings import join_strings
from fast_funcs.numbers import sum_precise
```

### 2. Inline Small Functions

```python
# Instead of importing square()
from fast_funcs.numbers import square
result = square(x)

# Just inline it (same performance)
result = x * x
```

### 3. Use Local Variable Caching

```python
# When using the same function many times
join_strings = fast_funcs.strings.join_strings
for chunk in chunks:
    result = join_strings(chunk)  # Faster local lookup
```

### 4. Conditionally Import Based on Platform

```python
import sys

if sys.platform == "win32":
    # Windows doesn't support ANSI by default
    from fast_funcs.io_win import write_lines_fast
else:
    from fast_funcs.io import write_lines_fast
```

### 5. Copy Only What You Need

This is the **most important optimization** for this repository:

```python
# Instead of:
# from fast_funcs.collections import flatten

# Just copy the function into your code:
def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]

# Zero dependencies, fully under your control
```

### 6. Disable ANSI in Production Logs

```python
import os

# Check environment variables
NO_COLOR = os.environ.get('NO_COLOR', False)
CI = os.environ.get('CI', False)

if NO_COLOR or CI:
    # Disable all styling
    RED = GREEN = BOLD = RESET = ""
else:
    from colors import RED, GREEN, BOLD, RESET
```

---

## License

MIT License — see [LICENSE](LICENSE) file.

---

**Author:** [Fkernel653](https://github.com/Fkernel653)
**Repository:** [github.com/Fkernel653/py-archive](https://github.com/Fkernel653/py-archive)
