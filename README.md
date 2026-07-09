# py-archive — Python Utilities Archive

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A collection of Python utilities designed for easy copying and use in your own projects. Browse the folders, find what you need, copy it.

---

## Structure

```
py-archive/
├── fast_funcs/          # High-performance alternatives to built-in functions
│   ├── io.py            #   echo, fast_input
│   ├── numbers.py       #   sum_precise, square, fast_round
│   └── types.py         #   is_exact_type, is_one_of
├── colors/              # ANSI terminal styling
│   ├── _constants.py    #   172 colors, 8 styles, all combinations
│   └── utils.py         #   styled, success, error, warning, info
├── LICENSE
└── README.md
```

---

## Usage

**1. Find what you need**

Look through the folders. Function names and docstrings are self-explanatory.

**2. Copy it**

```python
# Copy the function you need directly into your project
def echo(
    *args,
    file: TextIO = sys.stdout,
    flush: bool = False,
    sep: str = " ",
    end: str = "\n",
) -> None:
    file.write(sep.join([str(arg) for arg in args]) + end)
    if flush:
        file.flush()
```

**3. Or import if you cloned the repo**

```python
from fast_funcs.strings import join_strings
from colors import RED, BOLD, RESET
```

---

## Philosophy

- **No installation required** — just copy what you need
- **Zero dependencies** — only Python standard library
- **Self-documenting** — function names and docstrings tell you everything
- **Single-purpose** — each file does one thing, no hidden couplings

---

## License

MIT — see [LICENSE](LICENSE) file.

**Author:** [Fkernel653](https://github.com/Fkernel653)
**Repository:** [github.com/Fkernel653/py-archive](https://github.com/Fkernel653/py-archive)
