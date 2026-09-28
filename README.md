# py-archive — Python Utilities Archive

[![License](https://img.shields.io/badge/License-Unlicense-00b96b?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-9cf?style=for-the-badge)](<>)
[![Ruff](https://img.shields.io/badge/Code%20Style-Ruff-ff69b4?logo=ruff&logoColor=fff&style=for-the-badge)](https://docs.astral.sh/ruff)

**py-archive** is a curated collection of reusable Python utilities organized by category. Each module is standalone, well-documented, and ready to copy into your projects.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Requirements](#requirements)
- [Structure](#structure)
- [Available Modules](#available-modules)
  - [Customization](#customization)
    - [colors](#colors--ansi-terminal-colors)
  - [Optimization](#optimization)
    - [fast_funcs](#fast_funcs--high-performance-built-in-alternatives)
  - [File System](#file-system)
    - [pathlib_ng](#pathlib_ng--enhanced-path-implementation)
- [Philosophy](#philosophy)
- [Finding What You Need](#finding-what-you-need)
- [License & Acknowledgments](#license--acknowledgments)

---

## Quick Start

```bash
# Copy any module into your project
cp -r colors/ your-project/src/
cp -r fast_funcs/ your-project/src/
cp -r pathlib_ng/ your-project/src/
```

```python
# Import and use immediately
from colors import BOLD_RED, RESET
from colors.utils import success, error

from fast_funcs import types, numbers
from pathlib_ng import Path

# Start using
print(f"{BOLD_RED}Error:{RESET} Something went wrong")
success("Operation completed")
types.is_exact_type(42, int)  # True
numbers.square(5)  # 25
p = Path("projects") / "docs" / "readme.md"
```

---

## Requirements

| Module         | Minimum Python Version | License   |
| -------------- | ---------------------- | --------- |
| **colors**     | Python 3.0+            | Unlicense |
| **pathlib_ng** | Python 3.6+            | Unlicense |
| **fast_funcs** | Python 3.8+            | Unlicense |

> No external dependencies — All modules use only the Python standard library.

---

## Structure

```
py-archive/
├── colors/                    # ANSI color codes for terminal output
│   ├── colors/
│   │   ├── _constants.py      # 172 colors, 8 styles, all combinations
│   │   ├── utils.py           # styled, success, error, warning, info
│   │   └── __init__.py
│   ├── LICENSE
│   ├── pyproject.toml
│   └── README.md
├── fast_funcs/                # High-performance built-in alternatives
│   ├── fast_funcs/
│   │   ├── io.py              # echo, fast_input
│   │   ├── numbers.py         # sum_precise, square, fast_round
│   │   ├── types.py           # is_exact_type, is_one_of
│   │   └── __init__.py
│   ├── LICENSE
│   ├── pyproject.toml
│   └── README.md
├── pathlib_ng/                # Enhanced Path implementation
│   ├── pathlib_ng/
│   │   ├── __init__.py        # Package exports
│   │   └── path.py            # Path class implementation
│   ├── LICENSE
│   ├── pyproject.toml
│   └── README.md
├── LICENSE
└── README.md
```

---

## Available Modules

<details>
<summary><h3>🎨 Customization</h3></summary>

#### [colors](colors/) — ANSI Terminal Colors

Easily add colored output to your terminal applications with 172+ pre-defined color and style combinations.

**Features:**

- 16 colors (base + bright)
- 8 text styles (bold, italic, underline, etc.)
- Background colors
- Semantic helpers: `success()`, `error()`, `warning()`, `info()`, `hint()`
- Custom styling with `styled()`
- Zero dependencies — pure Python
- Copy & use — no installation required

**Requirements:** Python 3.0+

**License:** Unlicense — public domain, use freely

```python
from colors import BOLD_RED, RESET
from colors.utils import success, error

print(f"{BOLD_RED}Error:{RESET} Something went wrong")
success("Operation completed")
error("File not found")
```

**[→ Read more](colors/)**

</details>

<details>
<summary><h3>⚡ Optimization</h3></summary>

#### [fast_funcs](fast_funcs/) — High-performance built-in alternatives

Drop-in replacements for Python's built-in functions with up to 2x better performance.

**Features:**

- **types** — `is_exact_type()`, `is_one_of()` (~2x faster than `isinstance()`)
- **numbers** — `sum_precise()`, `square()` (~15% faster), `fast_round()` (~10% faster)
- **io** — `echo()`, `read()` with explicit buffering control
- Zero dependencies — pure Python
- Full type hints for better IDE integration
- Copy & use — no installation required

**Requirements:** Python 3.8+

**License:** Unlicense — public domain, use freely

```python
from fast_funcs import types, numbers

types.is_exact_type(42, int)  # True
numbers.square(5)  # 25 (15% faster than pow)
numbers.sum_precise([0.1, 0.2, 0.3])  # 0.6 (no float error)
```

**[→ Read more](fast_funcs/)**

</details>

<details>
<summary><h3>🗂️ File System</h3></summary>

#### [pathlib_ng](pathlib_ng/) — Enhanced Path implementation

A lightweight, drop-in replacement for `pathlib.Path` with enhanced features, better error messages, and zero external dependencies.

**Features:**

- **📁 Complete API** — All standard `pathlib.Path` methods implemented
- **🔗 Path Concatenation** — Overloaded `/` operator for intuitive path building
- **📝 File I/O** — `read_text()`, `write_text()`, `read_bytes()`, `write_bytes()`
- **📂 Directory Operations** — `mkdir()`, `rmdir()`, `iterdir()`
- **🔍 Glob Patterns** — `glob()` and `rglob()` for file matching
- **🧭 Path Resolution** — `resolve()`, `absolute()`, `expanduser()`
- **📊 File Metadata** — `stat()`, `exists()`, `is_file()`, `is_dir()`
- **📋 File Management** — `rename()`, `unlink()`, `touch()`
- **🖥️ Cross-Platform** — Works on Linux, macOS, and Windows
- **🧩 Zero Dependencies** — Pure Python with standard library only
- **💬 Enhanced Error Messages** — Clear, descriptive error messages
- **🔄 Drop-in Replacement** — Works with existing code using `pathlib.Path`

**Requirements:** Python 3.6+

**License:** Unlicense — public domain, use freely

```python
from pathlib_ng import Path

# Create paths with intuitive syntax
p = Path("projects") / "docs" / "readme.md"

# Read file content
if p.exists() and p.is_file():
    content = p.read_text()
    print(f"Content length: {len(content)} characters")
```

**[→ Read more](pathlib_ng/)**

</details>

---

## Philosophy

- **Copy, don't install** — Each module is designed to be copied directly into your project
- **Zero dependencies** — Only Python standard library (except where explicitly noted)
- **Self-documenting** — Clear function names and comprehensive docstrings
- **Single-purpose** — Each file does one thing well with no hidden couplings
- **Production-ready** — Tested utilities used in real applications
- **Unlicensed** — Use freely in open source and commercial projects

---

## Finding What You Need

1. **Browse by category**: Look through the available modules listed above
2. **Read the README** in each subfolder for detailed documentation
3. **Check the code** — functions have clear names and docstrings
4. **Look at examples** in the docstrings and README files

---

## License & Acknowledgments

**Unlicense** — All modules in this archive are released into the public domain under the [Unlicense](https://unlicense.org/). Use freely in open source and commercial projects without any restrictions.

Each module also contains its own `LICENSE` file with the full Unlicense text.

**Author:** [Fkernel653](https://github.com/Fkernel653)

**Repository:** [github.com/Fkernel653/py-archive](https://github.com/Fkernel653/py-archive)
