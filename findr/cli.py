"""Command-line interface for the project."""

from pathlib import Path
import sys
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from typing import NoReturn

from rich import print

from findr.consts import EXIT_FAILURE, PACKAGE
from findr.consts import __desc__ as DESC
from findr.consts import __version__ as VERSION


parser: ArgumentParser


def get_parsed_args() -> Namespace:
    """
    Parse and return command-line arguments.

    Returns:
        argparse.Namespace: The parsed arguments as a Namespace object.
    """
    global parser

    parser = ArgumentParser(
        description=DESC,  # Program description
        formatter_class=RawTextHelpFormatter,  # Custom formatter
        allow_abbrev=False,  # Disable abbreviations
        add_help=False,  # Disable default help
    )

    g_main = parser.add_argument_group("Main Options")

    # key argument
    g_main.add_argument(
        "key",
        type=str,
        help="The string to search for.",
    )
    # path argument
    default_path: Path = Path.cwd()
    g_main.add_argument(
        "--path",
        default=default_path,
        help=f"the path to search under (default: {default_path})",
    )
    # mode argument
    default_mode: str = "contents"
    g_main.add_argument(
        "--mode",
        type=str,
        choices=["contents", "filenames"],
        default=default_mode,
        help=f"The search mode. Default is '{default_mode}'.",
    )
    # max-depth argument
    g_main.add_argument(
        "--max-depth",
        type=int,
        default=999,
        help="maximum depth for recursive search",
    )
    # skip-dotfiles argument
    g_main.add_argument(
        "--skip-dotfiles",
        action="store_true",
        default=False,
        help="skip dotfiles",
    )

    g_misc = parser.add_argument_group("Miscellaneous Options")
    # Help
    g_misc.add_argument(
        "-h", "--help", action="help", help="Show this help message and exit."
    )
    # Verbose
    g_misc.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        default=False,
        help="Show log messages on screen. Default is False.",
    )
    # Debug
    g_misc.add_argument(
        "-d",
        "--debug",
        dest="debug",
        action="store_true",
        default=False,
        help="Activate debug logs. Default is False.",
    )
    g_misc.add_argument(
        "-V",
        "--version",
        action="version",
        help="Show version number and exit.",
        version=f"[argparse.prog]{PACKAGE}[/] version [i]{VERSION}[/]",
    )

    return parser.parse_args()


def print_parser_help() -> None:
    """Print the help message for the parser."""
    global parser

    parser.print_help()


def exit_session(exit_value: int) -> NoReturn:
    """
    Exit the program with the given exit value.

    Args:
        exit_value (int): The POSIX exit value to exit with.

    Returns:
        NoReturn: This function does not return anything
    """
    # Check if the exit_value is a valid POSIX exit value
    if not 0 <= exit_value <= 255:
        exit_value = EXIT_FAILURE

    if exit_value == EXIT_FAILURE:
        print(
            "\n[red]There were errors during the execution of the script.[/]",
        )

    # Exit the program with the given exit value
    sys.exit(exit_value)
