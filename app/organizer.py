"""
Organize files in a directory according to their extension.
"""

from pathlib import Path


def organize_files(path: Path) -> int:
    """
    Organize files in a directory according to their extension.

    Args:
        path (Path): The path to the directory to organize.
    """
    organized_files = 0

    for file in path.iterdir():
        if file.is_file() and file.suffix:
            destination = path / file.suffix[1:]
            destination.mkdir(exist_ok=True)
            file.rename(destination / file.name)

            organized_files += 1

    return organized_files
