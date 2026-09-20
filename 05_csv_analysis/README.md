# Library Loan CSV Analysis

The dataset represents library borrowing records, with one loan per row.
It provides practice in reading CSV files, filtering records, counting
categories, and calculating totals and averages with Python's standard library.

The current CSV is a **synthetic dataset** with fictional borrowers and loan
records prepared for this portfolio. The previous borrowing records were not
reused; their provenance could not be established. Keep using newly generated
fictional records for future public revisions.
It includes repeated titles for aggregation examples and a few deliberate
missing or invalid values so the validation paths can be demonstrated.

## Analyses in this directory

| Script | Analysis |
| --- | --- |
| `sum_loan_extensions.py` | Total valid extension days across loans |
| `count_loans_by_genre.py` | Number of loans in each recognized genre |
| `average_loan_period.py` | Average loan period including extensions, truncated to whole days (not rounded) |
| `list_unreturned_books.py` | Titles and borrower names for records marked as not returned |
| `most_borrowed_books.py` | Most frequently borrowed titles, including all ties in alphabetical order |

### Required fields by analysis

| Script | Required fields |
| --- | --- |
| `sum_loan_extensions.py` | `Forlenget` |
| `count_loans_by_genre.py` | `Sjanger` |
| `average_loan_period.py` | `Låneperiode`, `Forlenget` |
| `list_unreturned_books.py` | `Tilbakelevert`, `Fornavn`, `Etternavn`, `Boktittel` |
| `most_borrowed_books.py` | `Boktittel` |

Rows missing a required value are skipped. The CSV must still have a header
row so the scripts can identify these fields.

Run a script from the repository root, for example:

```bash
python 05_csv_analysis/most_borrowed_books.py
```

Scripts locate `library_loans.csv` beside their source files. Analysis functions
also accept an explicit CSV path.

## Expected schema

Use a comma-separated UTF-8 CSV with a header row. A UTF-8 byte-order mark is
also accepted. The current scripts expect the following exact Norwegian column
names; preserve these names when preparing compatible synthetic data.

| Column | Meaning |
| --- | --- |
| `Fornavn` | Borrower first name |
| `Etternavn` | Borrower last name |
| `Boktittel` | Book title |
| `Sjanger` | Genre: `Fiksjon` (Fiction), `Krim` (Crime), `Sakprosa` (Nonfiction), or `Fantasy` |
| `Lånedato` | Loan date in day/month/year order |
| `Låneperiode` | Non-negative integer loan period in days |
| `Forlenget` | Non-negative integer extension in days; use `0` for no extension |
| `Tilbakelevert` | Return flag: `Ja` (yes) or `Nei` (no) |

## Analysis behavior

Each analysis uses the fields it needs, ignoring missing required values.
Numeric analyses skip invalid or negative values and print a diagnostic.
The average is truncated to whole days rather than rounded; for example,
27 total days across 2 valid rows returns `13`. It returns `None` without
valid rows.
Unreturned-book listings require a title and both borrower names. Genre counts
use only the four listed genres. The loan date is retained as context and is
not parsed by these analyses.
An empty unreturned-book result means no qualifying records were found; it does
not prove that every book was returned. The return flag alone does not establish
whether a loan is overdue.
