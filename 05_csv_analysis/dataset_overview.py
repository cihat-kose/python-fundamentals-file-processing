"""Reference for the original Norwegian library-loan CSV.

Source columns (retained to preserve compatibility with the supplied dataset):
    Fornavn: borrower first name
    Etternavn: borrower last name
    Boktittel: book title
    Sjanger: genre (Fiksjon=Fiction, Krim=Crime, Sakprosa=Nonfiction, Fantasy)
    Lånedato: loan date in day/month/year order
    Låneperiode: loan period in days
    Forlenget: extension in days
    Tilbakelevert: return flag (Ja=yes, Nei=no)

Each analysis uses the fields it needs, ignoring missing required values.
Numeric analyses skip invalid or negative values and print a diagnostic.
The average is truncated to whole days and returns None without valid rows.
The return flag alone does not establish whether a loan is overdue.
Names and book titles remain as supplied; their provenance is unverified.
"""
