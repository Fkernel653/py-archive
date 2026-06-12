from ._constants import BOLD_CYAN, BOLD_GREEN, BOLD_RED, BOLD_YELLOW, RESET

# Severity prefixes
ERROR_PREFIX = BOLD_RED + "Error: " + RESET
SUCCESS_PREFIX = BOLD_GREEN + "Success: " + RESET
WARNING_PREFIX = BOLD_YELLOW + "Warning: " + RESET
INFO_PREFIX = BOLD_CYAN + "Info: " + RESET


def styled(text: str, *styles: str) -> str:
    """
    Apply multiple ANSI styles to text and auto-reset.

    Args:
        text: The text to style.
        *styles: One or more ANSI style codes (e.g., BOLD_RED, BG_BLUE).

    Returns:
        Styled string with RESET appended.

    Example:
        >>> styled("Hello", BOLD_RED)
        '\\033[1;31mHello\\033[0m'
    """
    return "".join(styles) + text + RESET


def error(text: str) -> str:
    """
    Format an error message with BOLD_red "Error:" prefix.

    Args:
        text: The error message text.

    Returns:
        Formatted string: "Error: {text}" in BOLD_red.

    Example:
        >>> error("File not found")
        '\\033[1;31mError:\\033[0m File not found'
    """
    return ERROR_PREFIX + text


def success(text: str) -> str:
    """
    Format a success message with BOLD_green "Success:" prefix.

    Args:
        text: The success message text.

    Returns:
        Formatted string: "Success: {text}" in BOLD_green.

    Example:
        >>> success("Download complete")
        '\\033[1;32mSuccess:\\033[0m Download complete'
    """
    return SUCCESS_PREFIX + text


def warning(text: str) -> str:
    """
    Format a warning message with BOLD_yellow "Warning:" prefix.

    Args:
        text: The warning message text.

    Returns:
        Formatted string: "Warning: {text}" in BOLD_yellow.

    Example:
        >>> warning("Low disk space")
        '\\033[1;33mWarning:\\033[0m Low disk space'
    """
    return WARNING_PREFIX + text


def info(text: str) -> str:
    """
    Format an info message with BOLD_cyan "Info:" prefix.

    Args:
        text: The info message text.

    Returns:
        Formatted string: "Info: {text}" in BOLD_cyan.

    Example:
        >>> info("Processing 3 files")
        '\\033[1;36mInfo:\\033[0m Processing 3 files'
    """
    return INFO_PREFIX + text
