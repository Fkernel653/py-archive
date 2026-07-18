# Colors — ANSI color codes for terminal output formatting

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-GPLv3-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macOS%20%7C%20windows-lightgrey)]()
[![Ruff](https://img.shields.io/badge/code%20style-ruff-261230?logo=ruff&logoColor=white)](https://docs.astral.sh/ruff)

A lightweight library providing ANSI escape codes for terminal text styling. Supports 16 colors, 8 text styles, background colors, and all combinations with zero dependencies.

---

## 🚀 Quick Start

### Copy into your project
```bash
cp -r colors/ your-project/src/
```

```python
from colors import RED, GREEN, RESET, BOLD_RED, BG_BLUE
from colors.utils import styled, success, error, warning, info, hint

# Use color constants directly
print(f"{BOLD_RED}Error:{RESET} Something went wrong")
print(f"{GREEN}Success!{RESET}")

# Use semantic helpers
success("Download complete")
error("File not found")
warning("Low disk space")
info("Processing 3 files")
hint("Try using --help for more options")

# Custom styling
print(styled("Hello World", BOLD_RED, BG_BLUE))
```

---

## ✨ Features

- **🎨 16 Colors** — 8 base + 8 bright colors
- **💪 8 Text Styles** — Bold, Dim, Italic, Underline, Blink, Reverse, Hidden, Strikethrough
- **🖍️ Background Colors** — All colors also available as backgrounds
- **🔗 Style Combinations** — Every style + color combination pre-defined (172+ constants)
- **🏷️ Semantic Helpers** — `success()`, `error()`, `warning()`, `info()`, `hint()`
- **🔧 Custom Styling** — `styled()` function for arbitrary combinations
- **🧩 Zero Dependencies** — Pure Python, only standard library
- **📦 Copy & Use** — No installation required, just copy the code
- **📖 Self-Documenting** — Clear constants names and comprehensive docstrings
- **🔌 Auto-Resets** — All styled strings include `RESET` for clean output

---

## 📁 Project Structure

```
colors/
├── colors/
│   ├── __init__.py      # Package exports
│   ├── _constants.py    # 172+ color and style constants
│   └── utils.py         # Semantic helpers: styled, success, error, warning, info, hint
├── LICENSE              # GPLv3 License
├── pyproject.toml       # Project metadata
└── README.md            # This file
```

---

## ⚙️ Requirements

- **Python 3.8+** — Standard Python features
- **No external dependencies** — Pure Python with standard library only

---

## 📄 License

GPLv3 License — Built with pure Python and standard library only. Use freely in open source and commercial projects.

**Author:** [Fkernel653](https://github.com/Fkernel653)

**Repository:** [github.com/Fkernel653/py-archive/tree/main/colors](https://github.com/Fkernel653/py-archive/tree/main/colors)
