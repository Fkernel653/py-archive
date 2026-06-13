# py-archive — Python Utilities Archive

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A collection of Python utilities designed for easy copying and use in your own projects. Browse the folders, find what you need, copy it.

---

## Structure

```
py-archive/
├── fast_funcs/          # High-performance alternatives to built-in functions
│   ├── attr.py          #   get_direct, has_direct, set_direct, del_direct, repr_attrs
│   ├── collections.py   #   filter_fast, map_fast, reverse_copy, sort_inplace, flatten
│   ├── io.py            #   echo, write_lines, fast_input
│   ├── numbers.py       #   sum_precise, square, fast_round
│   ├── search.py        #   any_early, build_index_map, to_set
│   ├── strings.py       #   join_strings, buffer_join, translate_replace, strip_newline
│   └── types.py         #   is_exact_type, is_one_of
├── regex_utils/         # Regex helpers with compilation, caching, and batch processing
│   ├── customization/   #   compile, extract, replace, split, validate
│   ├── performance/     #   batch, benchmark, cache
│   └── utils/           #   search
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
def find_all_matches(pattern, text, flags=0):
    import re
    return re.findall(pattern, text, flags)
```

**3. Or import if you cloned the repo**

```python
from fast_funcs.strings import join_strings
from regex_utils.performance.cache import cached_search
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
