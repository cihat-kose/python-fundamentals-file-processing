"""Regression tests for validation, CSV edge cases and safe file operations."""

import contextlib
import csv
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load(relative):
    spec = importlib.util.spec_from_file_location(Path(relative).stem, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ValidationTests(unittest.TestCase):
    def test_imports_have_no_side_effects(self):
        output = io.StringIO()
        with patch("builtins.input", side_effect=AssertionError("input on import")):
            with contextlib.redirect_stdout(output):
                for path in ROOT.glob("0*/*.py"):
                    load(path.relative_to(ROOT))
        self.assertEqual(output.getvalue(), "")

    def test_ipv4_boundaries(self):
        validate = load("03_functions/ipv4_validator.py").is_valid_ipv4_address
        for value in ("0.0.0.0", "255.255.255.255", "192.168.0.01"):
            result = validate(value)
            self.assertIsInstance(result, bool)
            self.assertTrue(result)
        for value in ("256.0.0.1", "1.2.3", "1.2.3.²", "1.2.3.１２", "١.٢.٣.٤", "1.2.3.-1", "1.2.3.0000", None):
            result = validate(value)
            self.assertIsInstance(result, bool)
            self.assertFalse(result)

    def test_dates(self):
        validate = load("01_python_basics/validate_date.py").is_valid_date
        self.assertTrue(validate("29/02/2000"))
        for value in ("29/02/1900", "31/04/2024", "hello", "1/2/0", None, 2024):
            self.assertFalse(validate(value))
        difference = load("03_functions/date_difference.py").days_between_dates
        self.assertEqual(difference("21/11/2024", "01/01/2024"), 325)
        self.assertEqual(difference("01/01/2024", "21/11/2024"), 325)
        self.assertEqual(difference("01/01/2024", "01/01/2024"), 0)

    def test_rgb(self):
        convert = load("03_functions/rgb_to_hex.py").rgb_to_hex
        self.assertEqual(convert(205, 92, 92), "#CD5C5C")
        self.assertEqual(convert(0, 0, 0), "#000000")
        for value in (-1, 256):
            with self.assertRaises(ValueError):
                convert(value, 0, 0)
        for value in (1.5, True, "5"):
            with self.assertRaises(TypeError):
                convert(value, 0, 0)


class FileTests(unittest.TestCase):
    def test_generation_sorting_and_collision_preserve_content(self):
        generate = load("04_file_processing/generate_random_files.py").generate_random_files
        sort = load("04_file_processing/sort_files_by_extension.py").sort_files_by_extension
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source"
            destination = Path(directory) / "destination"
            created = generate(source, 30)
            self.assertEqual(len(set(created)), 30)
            self.assertTrue(all(5 <= len(path.stem) <= 10 for path in created))
            self.assertTrue(all(path.stat().st_size == 0 for path in created))
            (source / "keep.bin").write_text("keep", encoding="utf-8")
            collision = created[0]
            target = destination / collision.suffix[1:] / collision.name
            target.parent.mkdir(parents=True)
            target.write_text("original", encoding="utf-8")
            self.assertEqual(len(sort(source, destination)), 29)
            self.assertTrue(collision.exists())
            self.assertEqual(target.read_text(encoding="utf-8"), "original")
            self.assertTrue((source / "keep.bin").exists())
            self.assertEqual(sort(source, destination), [])
            generate(source, 1)
            self.assertTrue(collision.exists())
            with self.assertRaises(ValueError):
                sort(source, source / "nested")


class CsvTests(unittest.TestCase):
    def test_missing_invalid_and_tied_rows(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "loans.csv"
            with path.open("w", encoding="utf-8-sig", newline="") as stream:
                writer = csv.writer(stream)
                writer.writerow(["Boktittel", "Låneperiode", "Forlenget", "Sjanger", "Tilbakelevert", "Fornavn", "Etternavn"])
                writer.writerows([
                    ["Beta", "14", "3", "Fantasy", "Nei", "A", "B"],
                    ["Alpha", "10", "0", "Krim", "Ja", "C", "D"],
                    ["Beta", "bad", "-1", "Unknown", "Nei", "", ""],
                    ["Alpha"],
                    ["", "", "²", "", "", "", ""],
                ])
            def call(name):
                return getattr(load(f"05_csv_analysis/{name}.py"), name)(path)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(call("sum_loan_extensions"), 3)
                self.assertEqual(call("average_loan_period"), 13)
                self.assertEqual(call("count_loans_by_genre"), {"Fantasy": 1, "Krim": 1})
                self.assertEqual(call("list_unreturned_books"), [("Beta", "A B")])
                self.assertEqual(call("most_borrowed_books"), [("Alpha", 2), ("Beta", 2)])
                path.write_text("Boktittel,Låneperiode,Forlenget\n", encoding="utf-8")
                self.assertIsNone(call("average_loan_period"))
                self.assertEqual(call("most_borrowed_books"), [])
                path.write_text("Unrelated\nvalue\n", encoding="utf-8")
                self.assertEqual(call("sum_loan_extensions"), 0)
                self.assertEqual(call("count_loans_by_genre"), {})
                self.assertEqual(call("list_unreturned_books"), [])
                self.assertEqual(call("most_borrowed_books"), [])


if __name__ == "__main__":
    unittest.main()
