# Python Fundamentals, File Processing & CSV Analysis

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-Data%20Processing-2E8B57?style=for-the-badge)
![File Handling](https://img.shields.io/badge/File-Handling-5A67D8?style=for-the-badge)

Practical Python exercises covering core programming concepts, data structures, reusable functions, file organization, and CSV analysis.

## Highlights

- Interactive exercises using input, conditionals, loops, and formatted output
- List and dictionary transformations, sorting, and validation
- Reusable functions for focused calculations and value checking
- File-system operations using Python's standard library
- CSV parsing, counting, filtering, and aggregation
- Small library-loan analyses based on the included dataset

## Project Structure

| Directory | Concepts demonstrated |
| --- | --- |
| `01_python_basics/` | Fundamental control flow, user input, arithmetic, string comparison, list indexing, and multiplication tables. |
| `02_data_structures/` | Date validation and transformations between flat lists, dictionaries, sorted values, and lists of records. |
| `03_functions/` | Reusable functions for IPv4 checks, date differences, RGB-to-HEX conversion, and result comparison. |
| `04_file_processing/` | Random file generation plus directory creation, deletion, listing, and extension-based file organization. |
| `05_csv_analysis/` | Standard-library CSV processing for totals, category counts, loan periods, return status, and borrowing frequency. |

## Featured Components

- **IPv4 validation:** Splits an address into four numeric parts and checks that each value is between `0` and `255`; digit strings with leading zeroes are accepted.
- **RGB to HEX conversion:** Converts three values in the inclusive `0`–`255` range to an uppercase six-digit HEX color and returns a Norwegian error message when a value is outside that range.
- **Function-result checking:** Accepts a callable, a list of arguments, and an expected value, then compares the function's result using equality.
- **Generated file organization:** Creates 30 empty files with random names and `.txt`, `.csv`, or `.log` extensions, then moves them into extension-specific directories. The scripts recreate `generated_files/` and `sorted_files/` when run.
- **CSV aggregation:** Totals extension days, counts loans in four recognized genres, and identifies entries marked as not returned.
- **Loan analysis:** Adds the loan period and extension for rows containing non-negative integers, then returns the integer quotient of total days divided by valid rows. A separate analysis finds all titles tied for the highest loan count and sorts ties alphabetically.

## Getting Started

The exercises use only modules from the Python standard library.

```bash
git clone https://github.com/cihat-kose/gokstadakademiet-arbeidskrav1.git
cd gokstadakademiet-arbeidskrav1
```

Run an individual script from the repository root, for example:

```bash
python 03_functions/ipv4_validator.py
```

Several exercises in `01_python_basics/` and `02_data_structures/` prompt for terminal input.

### File-organization exercises

Run these scripts from `04_file_processing/` so their relative `generated_files/` and `sorted_files/` paths are created there:

```bash
cd 04_file_processing
python generate_random_files.py
python sort_files_by_extension.py
```

> **Note:** Each script removes and recreates its target directory. Do not store files you want to keep in `generated_files/` or `sorted_files/` before running it.

### CSV analysis exercises

The analysis scripts expect `library_loans.csv` in the current working directory. Run them from `05_csv_analysis/`, for example:

```bash
cd 05_csv_analysis
python most_borrowed_books.py
```

## Academic Context

This repository began as a Python learning assignment at Gokstad Akademiet. The original task specification is retained in `docs/original-assignment.pdf`, while the repository is presented here as a compact record of the programming concepts practiced. AI tools were used during the learning process to clarify tasks, explore alternative approaches, and support the organization of the work and documentation.
