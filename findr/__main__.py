"""Main module for the project."""

import time
from argparse import Namespace
from contextlib import suppress
from pathlib import Path
from typing import Callable

from rich import print

from findr.cli import exit_session, get_parsed_args, print_parser_help
from findr.consts import EXIT_FAILURE, EXIT_SUCCESS
from findr.search import (
    print_match_in_file,
    print_match_in_filename,
    rec_find,
    search_in_file,
    search_in_filename,
)


def main() -> None:
    """Main function"""
    args: Namespace = get_parsed_args()

    if args.mode == "contents":
        print("\n[green]Searching contents...[/]")
        search_fun: Callable[[Path, str], tuple[str, bool]] = search_in_file
        print_fun: Callable[[str, str], None] = print_match_in_file

    elif args.mode == "filenames":
        print("\n[green]Searching filenames...[/]")
        search_fun = search_in_filename
        print_fun = print_match_in_filename

    else:
        print_parser_help()
        exit_session(EXIT_SUCCESS)

    search_dir: Path = Path(args.path).resolve()

    print()

    try:
        start_time: float = time.time()
        for fname in search_dir.iterdir():
            with suppress(Exception):
                rec_find(
                    path=fname,
                    key=args.key,
                    max_depth=args.max_depth,
                    search_fun=search_fun,
                    print_fun=print_fun,
                    no_dotfiles=args.skip_dotfiles,
                )

        if args.mode == "filenames":
            print()

        end_time: float = time.time()
        print(f"[green]Search completed in {end_time - start_time:.5f} seconds[/]")

        exit_session(EXIT_SUCCESS)

    except KeyboardInterrupt:
        print("\n[red]Cancelled[/]")

        exit_session(EXIT_FAILURE)


if __name__ == "__main__":
    main()
