# Library Loan CSV Analysis

The dataset represents library borrowing records, with one loan per row.
It provides practice in reading CSV files, filtering records, counting
categories, and calculating totals and averages with Python's standard library.

The library-loan dataset was provided as part of the original coursework and
is used solely for educational and portfolio purposes. It is not presented as
a record of actual library activity. It includes repeated titles for
aggregation examples and a few deliberate missing or invalid values so the
validation paths can be demonstrated.

## Analyses in this directory

| Script | Analysis |
| --- | --- |
| `sum_loan_extensions.py` | Total valid extension days across loans |
| `count_loans_by_genre.py` | Number of loans in each recognized genre |
| `average_loan_period.py` | Average loan period including extensions, truncated to whole days (not rounded) |
| `list_unreturned_books.py` | Titles and borrower IDs for records marked as not returned |
| `most_borrowed_books.py` | Most frequently borrowed titles, including all ties in alphabetical order |

### Required fields by analysis

| Script | Required fields |
| --- | --- |
| `sum_loan_extensions.py` | `extension_days` |
| `count_loans_by_genre.py` | `genre` |
| `average_loan_period.py` | `loan_period_days`, `extension_days` |
| `list_unreturned_books.py` | `returned`, `borrower_id`, `book_title` |
| `most_borrowed_books.py` | `book_title` |

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
also accepted. The current scripts expect the following exact English column
names.

| Column | Meaning |
| --- | --- |
| `borrower_id` | Borrower identifier; no personal names are stored |
| `book_title` | Book title |
| `genre` | `Fiction`, `Crime`, `Nonfiction`, or `Fantasy` |
| `loan_date` | Loan date in `YYYY-MM-DD` order |
| `loan_period_days` | Non-negative integer loan period in days |
| `extension_days` | Non-negative integer extension in days; use `0` for no extension |
| `returned` | Return flag: `Yes` or `No` |

## Analysis behavior

Each analysis uses the fields it needs, ignoring missing required values.
Numeric analyses skip invalid or negative values and print a diagnostic.
The average is truncated to whole days rather than rounded; for example,
27 total days across 2 valid rows returns `13`. It returns `None` without
valid rows.
Unreturned-book listings require a title and borrower ID. Genre counts use only
the four listed genres. The loan date is retained as context and is not parsed
by these analyses.
An empty unreturned-book result means no qualifying records were found; it does
not prove that every book was returned. The return flag alone does not establish
whether a loan is overdue.
