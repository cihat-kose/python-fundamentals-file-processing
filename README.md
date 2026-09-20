# Python Fundamentals, File Processing & CSV Analysis

Small, runnable Python programs exploring control flow, data structures,
reusable functions, file organization, and CSV analysis. This is a learning
portfolio, with straightforward standard-library implementations.

## Run a script

Use Python 3.10 or newer. No third-party packages are required. Verified with
Python 3.13.

From the repository root:

```bash
python 01_python_basics/sum_number_range.py
python 03_functions/rgb_to_hex.py
python 05_csv_analysis/most_borrowed_books.py
```

The first command prompts for input. RGB conversion prints `#CD5C5C`,
`#000000`, and `#FFFFFF`. Each script runs independently; importing a script
neither prompts for input nor runs its demonstration.

## Project structure and progression

| Directory | Topics |
| --- | --- |
| `01_python_basics/` | Input, conditionals, loops, inclusive ranges, list indices, calendar validation, and formatted multiplication tables |
| `02_data_structures/` | List transformations, dictionaries, records, and sorting |
| `03_functions/` | IPv4 parsing, date differences, RGB conversion, and higher-order functions |
| `04_file_processing/` | Unique file generation, paths, directory iteration, and extension-based moves |
| `05_csv_analysis/` | CSV reading, filtering, counters, totals, averages, and ties |
| `tests/` | Regression tests for validation, malformed CSV rows, imports, and file preservation |
| `docs/` | Private archive material kept outside the learning sequence |

The sequence moves from Python basics to data-structure transformations, then
to reusable functions. It applies those foundations to file-system operations
before combining them in CSV analysis, where parsing, validation, aggregation,
and edge-case handling are practiced together.

Code identifiers, explanations, prompts, and messages are in English. The CSV
uses a human-name-free English schema with synthetic borrower IDs and fictional
book titles.

## Behavior and boundaries

- Integer programs report invalid numeric input. Range sums require a positive
  integer; multiplication grids require start <= end. Keep grids small enough
  to read in a terminal. List swapping accepts non-negative indices only.
- Date utilities accept day/month/year strings and apply leap-year validation.
  Single-digit days and months are accepted. Invalid dates return `False` in
  the validator and raise `ValueError` in the difference function.
- IPv4 validation accepts four ASCII decimal octets from 0 to 255, each one to
  three digits. Leading zeroes are accepted by the validator.
- `rgb_to_hex(red, green, blue)` returns uppercase `#RRGGBB`. It raises
  `TypeError` for non-integers (including booleans) and `ValueError` for values
  outside 0–255.
- `check_function_result(function, arguments, expected_result)` compares the
  return value using equality. Exceptions from the supplied function propagate.

## File organization

```bash
python 04_file_processing/generate_random_files.py
python 04_file_processing/sort_files_by_extension.py
```

Paths are relative to the scripts, so these commands also work when launched
by absolute path from another directory. Each generator run adds 30 empty
files with unique random names and `.txt`, `.csv`, or `.log` extensions.
Existing files are preserved. The sorter moves supported regular files into
`sorted_files/txt/`, `sorted_files/csv/`, and `sorted_files/log/`; it skips
unsupported files, symbolic links, and destination-name collisions. A skipped
collision remains in the source directory. Missing source directories produce
an error. These utilities are intended for local, sequential practice runs.

The functions also accept explicit directory paths, as demonstrated by the
tests using temporary directories. All generated and sorted files are
runtime-only output and are ignored by Git; they are never part of the source
archive.

## CSV analysis

The scripts locate `05_csv_analysis/library_loans.csv` beside their source
files. Their functions accept a different CSV path for experimentation.
[CSV analysis documentation](05_csv_analysis/README.md) documents the
human-name-free English schema and the synthetic data-quality examples used by
the analysis scripts.

Each analysis requires only the fields it uses. Missing values are skipped;
invalid or negative numeric values produce diagnostics and are skipped.
Unreturned-book listings require a title and borrower ID. Genre counts recognize
Fiction, Crime, Nonfiction, and Fantasy. The average includes extension days
and truncates to whole days using integer division; it returns `None` when
there are no valid rows.
Most-borrowed results include every title tied for first, sorted by title.
The return flag does not by itself establish whether a loan is overdue.

## Verification

```bash
python -m unittest discover -s tests -v
```

Tests cover leap years, malformed IPv4 octets, RGB types and ranges, silent
imports, file collisions and preservation, incomplete CSV rows, invalid
numeric values, empty results, and tied borrowing counts.

## Repository status

This repository remains the **private development and archive repository**.
A future public portfolio will use a separate repository with clean history.
The bundled source materials remain private archive content. The working-tree
CSV is synthetic and uses fictional records; the previous named borrowing
records were not reused because their provenance could not be established.
