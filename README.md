# py-archive — Python Utilities Archive

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A curated collection of reusable Python utilities organized by category. Each module is standalone, well-documented, and ready to copy into your projects.

---

## 📑 Table of Contents

- [📂 Structure](#-structure)
- [📦 Available Modules](#-available-modules)
  - [🎨 Customization](#-customization)
    - [colors](#colors--ansi-terminal-colors)
  - [⚡ Optimization](#-optimization)
    - [fast_funcs](#fast_funcs--high-performance-built-in-alternatives)
- [🎯 Philosophy](#-philosophy)
- [🔍 Finding What You Need](#-finding-what-you-need)
- [📄 License & Acknowledgments](#-license--acknowledgments)

---

## 📂 Structure

```
py-archive/
├── colors/                 # ANSI color codes for terminal output
│   ├── colors/
│   │   ├── _constants.py    # 172 colors, 8 styles, all combinations
│   │   ├── utils.py         # styled, success, error, warning, info
│   │   └── __init__.py
│   ├── LICENSE
│   ├── pyproject.toml
│   └── README.md
│
├── fast_funcs/             # High-performance built-in alternatives
│   ├── fast_funcs/
│   │   ├── io.py           # echo, fast_input
│   │   ├── numbers.py      # sum_precise, square, fast_round
│   │   ├── types.py        # is_exact_type, is_one_of
│   │   └── __init__.py
│   ├── LICENSE
│   ├── pyproject.toml
│   └── README.md
│
├── LICENSE
├── pyproject.toml
└── README.md
```

---

## 📦 Available Modules

### 🎨 Customization

#### [colors](colors/) — ANSI Terminal Colors
Easily add colored output to your terminal applications with 172+ pre-defined color and style combinations.

**Features:**
- 16 colors (base + bright)
- 8 text styles (bold, italic, underline, etc.)
- Background colors
- Semantic helpers: `success()`, `error()`, `warning()`, `info()`
- Custom styling with `styled()`

```python
from colors import BOLD_RED, RESET
from colors.utils import success, error

print(f"{BOLD_RED}Error:{RESET} Something went wrong")
success("Operation completed")
```

**PyPI:** [colors](https://pypi.org/project/colors-terminal/)

**[→ Read more](colors/)**

---

### ⚡ Optimization

#### [fast_funcs](fast_funcs/) — High-performance built-in alternatives
Drop-in replacements for Python's built-in functions with up to 2x better performance.

**Features:**
- **types** — `is_exact_type()`, `is_one_of()` (~2x faster than `isinstance()`)
- **numbers** — `sum_precise()`, `square()` (~15% faster), `fast_round()` (~10% faster)
- **io** — `echo()`, `fast_input()` with explicit buffering control

```python
from fast_funcs import types, numbers

types.is_exact_type(42, int)  # True
numbers.square(5)             # 25 (15% faster than pow)
```

**PyPI:** [fast-funcs](https://pypi.org/project/fast-funcs/)

**[→ Read more](fast_funcs/)**

---

## 🎯 Philosophy

- **Copy, don't install** — Each module is designed to be copied directly into your project
- **Zero dependencies** — Only Python standard library (except where explicitly noted)
- **Self-documenting** — Clear function names and comprehensive docstrings
- **Single-purpose** — Each file does one thing well with no hidden couplings
- **Production-ready** — Tested utilities used in real applications
- **MIT licensed** — Use freely in open source and commercial projects

---

## 🔍 Finding What You Need

1. **Browse by category**: Look through the available modules listed above
2. **Read the README** in each subfolder for detailed documentation
3. **Check the code** — functions have clear names and docstrings
4. **Look at examples** in the docstrings and README files

---

## 📄 License & Acknowledgments

MIT License — Use freely in open source and commercial projects.

**Author:** [Fkernel653](https://github.com/Fkernel653)

**Repository:** [github.com/Fkernel653/py-archive](https://github.com/Fkernel653/py-archive)
