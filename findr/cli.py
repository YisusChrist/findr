"""Command-line interface for the project."""

from argparse import ArgumentParser, Namespace, RawTextHelpFormatter

from findr.consts import PACKAGE
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
    # mode argument
    g_main.add_argument(
        "--mode",
        type=str,
        choices=["contents", "filenames"],
        default="contents",
        help="The search mode. Default is 'contents'.",
    )
    g_main.add_argument(
        "--max-depth",
        type=int,
        default=999,
        help="maximum depth for recursive search",
    )
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
    global parser

    """
    Usage: findr [key] [flags]
        Flags:
        --mode=contents|filenames
        --max-depth=999
        --skip-dotfiles=False
    """

    parser.print_help()
