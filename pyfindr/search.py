"""Search functions for the project."""

from contextlib import suppress
from pathlib import Path
from typing import Callable

from rich import print

from pyfindr.consts import HIGHLIGHT_MAX_LEN


def readlines(file: str | Path) -> list[str]:
    """
    Reads a file and returns its contents as a list of lines.

    Args:
        file (str | Path): The name of the file to read.

    Returns:
        list[str]: The contents of the file.
    """
    with open(file, "r", encoding="utf-8") as f:
        return f.readlines()


def print_match_in_file(fname: str, buffer: str) -> None:
    """
    Used to print a match found in a file.

    Args:
        fname (str): Name of file where match was found
        buffer (str): Buffer to print containing the match itself
    """
    print(f"[yellow]{fname}[/]\n{buffer}", flush=True)


def print_match_in_filename(_: str, buffer: str) -> None:
    """
    Used to print a match found in a filename.

    Args:
        _ (str): Name of file where match was found (not used)
        buffer (str): Buffer to print containing the match itself
    """
    print(buffer, flush=True)


def rec_find(  # pylint: disable=too-many-arguments
    path: Path,
    key: str,
    max_depth: int = 999,
    *,
    search_fun: Callable[[Path, str], tuple[str, bool]],
    print_fun: Callable[[str, str], None],
    no_dotfiles: bool = False,
) -> None:
    """
    Recursively search for key in file or directory.
    Calls search_fun for each file or directory found and print_fun
    for each match found.

    Args:
        path (Path): File or directory name
        key (str): Key to search
        max_depth (int, optional): Maximum depth to search (default: 999)
        search_fun (Callable[[Path, str], tuple[str, bool]]): Function to search for key
        print_fun (Callable[[str, str], None]): Function to print results
        no_dotfiles (bool, optional): Skip dotfiles (default: False)
    """
    if max_depth <= 0:
        return

    if no_dotfiles and path.name.startswith("."):
        return

    if path.is_file():
        with suppress(Exception):
            buffer, found = search_fun(path, key)
            if found:
                # Get the relative path
                relative_path = path.relative_to(Path.cwd())
                print_fun(str(relative_path), buffer)

    elif path.is_dir():
        for file in path.iterdir():
            rec_find(
                path=file,
                key=key,
                max_depth=max_depth - 1,
                search_fun=search_fun,
                print_fun=print_fun,
                no_dotfiles=no_dotfiles,
            )


def search_in_filename(path: Path, key: str) -> tuple[str, bool]:
    """
    Search for key in filename and return results

    Args:
        path (Path): File or directory name
        key (str): Key to search

    Returns:
        tuple[str, bool]: Buffer to store results, True if key is found
    """
    fname: str = path.name
    if key not in fname:
        return "", False

    start_idx = fname.index(key)
    end_idx = start_idx + len(key)
    buffer = (
        f"{fname[:start_idx]}[green]{fname[start_idx:end_idx]}" f"[/]{fname[end_idx:]}"
    )

    return buffer, True


def search_in_file(path: Path, key: str) -> tuple[str, bool]:
    """
    Search for key in file and store results in buffer

    Args:
        path (Path): File or directory name
        key (str): Key to search

    Returns:
        tuple[str, bool]: Buffer to store results, True if key is found
    """
    buffer = []
    for line_num, line in enumerate(readlines(path)):

        if key not in line:
            continue

        key_text = f"[green]{key}[/]"
        higlight = line.strip().replace(key, key_text)

        if higlight.index(key) > 20:
            higlight = higlight[higlight.index(key) - 20 :]

        location_text = (
            f"[blue]Line {line_num + 1}, "
            f"Column {line.find(key) + 1}:[/] "
            f"{higlight[:HIGHLIGHT_MAX_LEN]}"
        )

        if location_text[-1] != "\n":
            location_text = f"{location_text}\n"

        buffer.append(location_text)

    return "".join(buffer), len(buffer) > 0
