# Colors — ANSI color codes for terminal output formatting

[![Python](https://img.shields.io/badge/Python-3+-3776AB?logo=python&logoColor=fff&style=for-the-badge)](https://python.org)
[![License](https://img.shields.io/badge/License-Unlicense-00b96b?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-9cf?style=for-the-badge)](<>)
[![Ruff](https://img.shields.io/badge/Code%20Style-Ruff-ff69b4?logo=ruff&logoColor=fff&style=for-the-badge)](https://docs.astral.sh/ruff)

A lightweight library providing ANSI escape codes for terminal text styling. Supports 16 colors, 8 text styles, background colors, and all combinations with zero dependencies.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Requirements](#requirements)
- [Features](#features)
- [Usage Examples](#usage-examples)
  - [Color Constants](#color-constants)
  - [Semantic Helpers](#semantic-helpers)
  - [Custom Styling](#custom-styling)
  - [Background Colors](#background-colors)
  - [Style Combinations](#style-combinations)
- [Available Constants](#available-constants)
  - [Base Colors](#base-colors)
  - [Bright Colors](#bright-colors)
  - [Text Styles](#text-styles)
  - [Background Colors](#background-colors-1)
- [Project Structure](#project-structure)
- [License](#license)

---

## Quick Start

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

## Requirements

- **Python 3+** — Standard Python features
- **No external dependencies** — Pure Python with standard library only

---

## Features

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

## Usage Examples

<details>
<summary>Color Constants</summary>

```python
from colors import RED, GREEN, YELLOW, BLUE, RESET

print(f"{RED}Error message{RESET}")
print(f"{GREEN}Success message{RESET}")
print(f"{YELLOW}Warning message{RESET}")
print(f"{BLUE}Info message{RESET}")
```

</details>

<details>
<summary>Semantic Helpers</summary>

```python
from colors.utils import success, error, warning, info, hint

success("Operation completed")     # Green output
error("Something went wrong")      # Red output
warning("Low disk space")          # Yellow output
info("Processing 3 files")         # Blue output
hint("Try using --help")           # Cyan output
```

</details>

<details>
<summary>Custom Styling</summary>

```python
from colors import BOLD_RED, BG_BLUE
from colors.utils import styled

# Combine style and background
print(styled("Hello World", BOLD_RED, BG_BLUE))

# Multiple styles
from colors import BOLD, ITALIC, UNDERLINE
print(f"{BOLD}{ITALIC}{UNDERLINE}Formatted text{RESET}")
```

</details>

<details>
<summary>Background Colors</summary>

```python
from colors import BG_RED, BG_GREEN, BG_BLUE, WHITE, RESET

print(f"{BG_RED}{WHITE}Error background{RESET}")
print(f"{BG_GREEN}{WHITE}Success background{RESET}")
print(f"{BG_BLUE}{WHITE}Info background{RESET}")
```

</details>

<details>
<summary>Style Combinations</summary>

```python
from colors import BOLD_RED, BOLD_GREEN, UNDERLINE_BLUE, ITALIC_YELLOW

print(f"{BOLD_RED}Bold red text{RESET}")
print(f"{BOLD_GREEN}Bold green text{RESET}")
print(f"{UNDERLINE_BLUE}Underlined blue text{RESET}")
print(f"{ITALIC_YELLOW}Italic yellow text{RESET}")
```

</details>

---

## Available Constants

### Base Colors

| Constant  | Description |
| --------- | ----------- |
| `BLACK`   | Black       |
| `RED`     | Red         |
| `GREEN`   | Green       |
| `YELLOW`  | Yellow      |
| `BLUE`    | Blue        |
| `MAGENTA` | Magenta     |
| `CYAN`    | Cyan        |
| `WHITE`   | White       |

### Bright Colors

| Constant         | Description    |
| ---------------- | -------------- |
| `BRIGHT_BLACK`   | Bright Black   |
| `BRIGHT_RED`     | Bright Red     |
| `BRIGHT_GREEN`   | Bright Green   |
| `BRIGHT_YELLOW`  | Bright Yellow  |
| `BRIGHT_BLUE`    | Bright Blue    |
| `BRIGHT_MAGENTA` | Bright Magenta |
| `BRIGHT_CYAN`    | Bright Cyan    |
| `BRIGHT_WHITE`   | Bright White   |

### Text Styles

| Constant        | Description     |
| --------------- | --------------- |
| `BOLD`          | Bold text       |
| `DIM`           | Dim text        |
| `ITALIC`        | Italic text     |
| `UNDERLINE`     | Underlined text |
| `BLINK`         | Blinking text   |
| `REVERSE`       | Reverse colors  |
| `HIDDEN`        | Hidden text     |
| `STRIKETHROUGH` | Struck text     |

### Background Colors

All base and bright colors are also available with the `BG_` prefix (e.g., `BG_RED`, `BG_BRIGHT_BLUE`).

---

## Project Structure

```
colors/
├── colors/
│   ├── __init__.py      # Package exports
│   ├── _constants.py    # 172+ color and style constants
│   └── utils.py         # Semantic helpers: styled, success, error, warning, info, hint
├── LICENSE              # Unlicense
├── pyproject.toml       # Project metadata
└── README.md            # This file
```

---

## License

Unlicense — Built with pure Python and standard library only. Use freely in open source and commercial projects.

**Author:** [Fkernel653](https://github.com/Fkernel653)

**Repository:** [github.com/Fkernel653/py-archive/tree/main/colors](https://github.com/Fkernel653/py-archive/tree/main/colors)
