"""Move supported files into extension folders without overwriting files."""

from pathlib import Path
import shutil

BASE_DIRECTORY = Path(__file__).resolve().parent


def sort_files_by_extension(source=BASE_DIRECTORY / "generated_files",
                            destination=BASE_DIRECTORY / "sorted_files"):
    """Move .txt, .csv and .log files; skip links, other types and collisions."""
    source = Path(source).resolve()
    destination = Path(destination).resolve()
    if not source.is_dir():
        raise FileNotFoundError(f"Source directory does not exist: {source}")
    if source == destination or source in destination.parents or destination in source.parents:
        raise ValueError("Source and destination must be separate directories")
    moved = []
    for path in sorted(source.iterdir()):
        extension = path.suffix.lower()
        if path.is_symlink() or not path.is_file() or extension not in {".txt", ".csv", ".log"}:
            continue
        folder = destination / extension[1:]
        if folder.is_symlink():
            raise ValueError(f"Destination subdirectory must not be a symlink: {folder}")
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / path.name
        if target.exists() or target.is_symlink():
            continue
        shutil.move(str(path), str(target))
        moved.append(target)
    return moved


if __name__ == "__main__":
    try:
        print(f"Moved {len(sort_files_by_extension())} files into sorted_files.")
    except (OSError, ValueError) as error:
        raise SystemExit(str(error))
