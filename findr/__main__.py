"""Main module for the project."""

from contextlib import suppress
from os import getcwd, listdir
from os.path import isdir as path_isdir
from os.path import isfile as path_isfile
from os.path import join as path_join
from sys import exit as sys_exit
from typing import Callable

from argsdict import args  # type: ignore

HIGHLIGHT_MAX_LEN = 40
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"


def readlines(filename: str) -> list[str]:
    """
    Reads a file and returns its contents as a list of lines.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list[str]: The contents of the file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.readlines()


def print_match_in_file(fname: str, buffer: str) -> None:
    """
    Used to print a match found in a file.

    Args:
        fname (str): Name of file where match was found
        buffer (str): Buffer to print containing the match itself
    """
    print(f"{YELLOW}{fname}{RESET}\n{buffer}", flush=True)


def print_match_in_filename(_: str, buffer: str) -> None:
    """
    Used to print a match found in a filename.

    Args:
        _ (str): Name of file where match was found (not used)
        buffer (str): Buffer to print containing the match itself
    """
    print(buffer, flush=True)


def rec_find(
    fname: str,
    key: str,
    max_depth: int,
    *,
    search_fun: Callable[[str, str], tuple[str, bool]],
    print_fun: Callable[[str, str], None],
    no_dotfiles: bool = False,
) -> None:
    """
    Recursively search for key in file or directory.
    Calls search_fun for each file or directory found and print_fun
    for each match found.

    Args:
        fname (str): File or directory name
        key (str): Key to search
        max_depth (int): Maximum depth to search
        search_fun (Callable[[str, str], tuple[str, bool]]): Function to search for key
        print_fun (Callable[[str, str], None]): Function to print results
        no_dotfiles (bool, optional): Skip dotfiles (default: False)
    """
    if max_depth <= 0:
        return

    if no_dotfiles and fname.split("/")[-1].startswith("."):
        return

    if path_isfile(fname):
        with suppress(Exception):
            buffer, found = search_fun(fname, key)
            if found:
                print_fun(fname, buffer)

    elif path_isdir(fname):
        for file in listdir(fname):
            rec_find(
                path_join(fname, file),
                key,
                max_depth=max_depth - 1,
                search_fun=search_fun,
                print_fun=print_fun,
                no_dotfiles=no_dotfiles,
            )


def search_in_filename(fname: str, key: str) -> tuple[str, bool]:
    """
    Search for key in filename and return results

    Args:
        fname (str): File or directory name
        key (str): Key to search

    Returns:
        tuple[str, bool]: Buffer to store results, True if key is found
    """
    if key not in fname:
        return "", False

    start_idx = fname.index(key)
    end_idx = start_idx + len(key)
    buffer = (
        f"{fname[:start_idx]}{GREEN}{fname[start_idx:end_idx]}"
        f"{RESET}{fname[end_idx:]}"
    )

    return buffer, True


def search_in_file(fname: str, key: str) -> tuple[str, bool]:
    """
    Search for key in file and store results in buffer

    Args:
        fname (str): File or directory name
        key (str): Key to search

    Returns:
        tuple[str, bool]: Buffer to store results, True if key is found
    """
    buffer = []
    for line_num, line in enumerate(readlines(fname)):

        if key not in line:
            continue

        key_text = f"{GREEN}{key}{RESET}"
        higlight = line.strip().replace(key, key_text)

        if higlight.index(key) > 20:
            higlight = higlight[higlight.index(key) - 20 :]

        location_text = (
            f"{BLUE}Line {line_num + 1}, "
            f"Column {line.find(key) + 1}:{RESET} "
            f"{higlight[:HIGHLIGHT_MAX_LEN]}"
        )

        if location_text[-1] != "\n":
            location_text = f"{location_text}\n"

        buffer.append(location_text)

    return "".join(buffer), len(buffer) > 0


def main() -> int:
    """
    Main function

    Returns:
        int: 0 if successful, 1 if cancelled
    """
    arg = args(["key"])

    query = arg.get("key", None)
    mode = arg.get("--mode", "contents")
    depth = arg.get("--max-depth", 999)
    no_dotfiles = bool(arg.get("--skip-dotfiles", False))

    if not query or "--help" in arg:
        print("\nUsage: findr [key] [flags]")
        print("Flags:")
        print("--mode=contents|filenames")
        print("--max-depth=999")
        print("--skip-dotfiles=False\n")
        return 0

    if mode == "contents":
        print(f"\n{GREEN}Searching contents...{RESET}")
        search_fun = search_in_file
        print_fun = print_match_in_file

    elif mode == "filenames":
        print(f"\n{GREEN}Searching filenames...{RESET}")
        search_fun = search_in_filename
        print_fun = print_match_in_filename

    else:
        print("\nUsage: findr [key] [flags]")
        print("Flags:")
        print("--mode=contents|filenames")
        print("--max-depth=999")
        print("--skip-dotfiles=False\n")
        return 0

    files = listdir(getcwd())

    print()

    try:
        for fname in files:
            with suppress(Exception):
                rec_find(
                    fname,
                    query,
                    max_depth=int(depth),
                    search_fun=search_fun,
                    print_fun=print_fun,
                    no_dotfiles=no_dotfiles,
                )

        if mode == "filenames":
            print()

        sys_exit(0)

    except KeyboardInterrupt:
        print(f"\n{RED}Cancelled{RESET}\n")

        sys_exit(1)


if __name__ == "__main__":
    main()
