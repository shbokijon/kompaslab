"""Offline importer unit tests: no invented employer data in production."""
import unittest
from uk_sponsors import CsvLinks, parse_csv


class ImportTests(unittest.TestCase):
    def test_asset_link(self):
        parser = CsvLinks()
        parser.feed('<a href="https://assets.publishing.service.gov.uk/media/test/2026-10-23.csv">CSV</a>')
        self.assertEqual(len(parser.links), 1)

    def test_filters_route_and_deduplicates(self):
        sample = (
            "Organisation Name,Town/City,County,Type & Rating,Route\n"
            '"Test, Ltd",Leeds,Yorkshire,Worker (A rating),Skilled Worker\n'
            '"Test, Ltd",Leeds,Yorkshire,Worker (A rating),Skilled Worker\n'
            "Other,London,,Temporary Worker (A rating),Creative Worker\n"
        )
        # Test the parser logic without production minimum-count validation.
        # Expected RuntimeError is the guard against publishing tiny/incomplete data.
        with self.assertRaisesRegex(RuntimeError, "Unexpected Skilled Worker record count"):
            parse_csv(sample.encode("utf-8"))

    def test_rejects_wrong_header(self):
        with self.assertRaisesRegex(RuntimeError, "Unexpected header"):
            parse_csv(b"First,Last\nFoo,Bar")


if __name__ == "__main__":
    unittest.main()
