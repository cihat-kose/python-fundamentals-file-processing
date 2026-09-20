"""Create empty sample files without deleting existing files."""

from pathlib import Path
import random
import string

DEFAULT_DIRECTORY = Path(__file__).resolve().parent / "generated_files"


def generate_random_string(length):
    return "".join(random.choice(string.ascii_letters + string.digits)
                   for _ in range(length))


def generate_random_files(directory=DEFAULT_DIRECTORY, count=30):
    """Add count unique files; existing files are preserved."""
    if type(count) is not int or count < 0:
        raise ValueError("count must be a non-negative integer")
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    created = []
    while len(created) < count:
        name = generate_random_string(random.randint(5, 10))
        path = directory / (name + random.choice((".txt", ".csv", ".log")))
        try:
            with path.open("x", encoding="utf-8"):
                pass
        except FileExistsError:
            continue
        created.append(path)
    return created


if __name__ == "__main__":
    created = generate_random_files()
    print(f"Created {len(created)} files in {DEFAULT_DIRECTORY}")
    for path in sorted(created):
        print(f"|-- {path.name}")
