# Fast-Funcs — High-performance alternatives to Python built-in functions

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=fff&style=for-the-badge)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-00b96b?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-9cf?style=for-the-badge)]()
[![Ruff](https://img.shields.io/badge/Code%20Style-Ruff-ff69b4?logo=ruff&logoColor=fff&style=for-the-badge)](https://docs.astral.sh/ruff)

Drop-in replacements for Python's built-in functions with better performance, lower overhead, and specialized optimizations.

---

## 🚀 Quick Start

### Copy into your project
```bash
cp -r fast_funcs/ your-project/src/
```

```python
from fast_funcs import types, numbers, io

# Start using immediately
types.is_exact_type(42, int)  # True
numbers.square(5)  # 25
io.echo("Hello", "World")  # Hello World
```

---

## ✨ Features

- **⚡ Performance Optimized** — Up to 2x faster than built-in functions
- **🎯 Exact Type Checking** — Faster alternative to `isinstance()` that ignores inheritance
- **🔢 Precise Math** — Error-compensated float summation with `math.fsum()`
- **📐 Fast Squaring** — 15% faster than `pow(x, 2)` using simple multiplication
- **🔄 Optimized Rounding** — Integer-based rounding that outperforms `round()`
- **📝 Streamlined I/O** — Print with explicit buffering control
- **⌨️ Clean Input** — Input without automatic trailing spaces
- **🧩 Zero Dependencies** — Pure Python, only standard library
- **📦 Copy & Use** — No installation required, just copy the code
- **🔍 Type Hints** — Full typing support for better IDE integration
- **📖 Self-Documenting** — Clear function names and comprehensive docstrings

---

## 📁 Project Structure

```
fast_funcs/
├── fast_funcs/
│   ├── __init__.py      # Package exports
│   ├── io.py            # I/O operations: echo, read
│   ├── numbers.py       # Numeric operations: sum_precise, square, fast_round
│   └── types.py         # Type checking: is_exact_type, is_one_of
├── LICENSE              # MIT License
├── pyproject.toml       # Project metadata
└── README.md            # This file
```

---

## ⚙️ Requirements

- **Python 3.10+** — Type hint support and modern Python features
- **No external dependencies** — Pure Python with standard library only

---

## 📄 License

MIT License — Built with pure Python and standard library only. Use freely in open source and commercial projects.

**Author:** [Fkernel653](https://github.com/Fkernel653)

**Repository:** [github.com/Fkernel653/py-archive/tree/main/fast_funcs](https://github.com/Fkernel653/py-archive/tree/main/fast_funcs)
