# Library Loan CSV Analysis

These exercises analyze the original Norwegian library-loan CSV. Source
column names are retained for compatibility with the supplied dataset.

## Source fields

| Column | Meaning |
| --- | --- |
| `Fornavn` | Borrower first name |
| `Etternavn` | Borrower last name |
| `Boktittel` | Book title |
| `Sjanger` | Genre: `Fiksjon` (Fiction), `Krim` (Crime), `Sakprosa` (Nonfiction), or `Fantasy` |
| `Lånedato` | Loan date in day/month/year order |
| `Låneperiode` | Loan period in days |
| `Forlenget` | Extension in days |
| `Tilbakelevert` | Return flag: `Ja` (yes) or `Nei` (no) |

## Analysis behavior

Each analysis uses the fields it needs, ignoring missing required values.
Numeric analyses skip invalid or negative values and print a diagnostic.
The average is truncated to whole days and returns `None` without valid rows.
The return flag alone does not establish whether a loan is overdue.

Names and book titles remain as supplied; their provenance is unverified.
