"""Offline tests for the NL and CA importers (fixtures only, never published)."""
import unittest

from nl_sponsors import parse as nl_parse
from ca_lmia import latest_resource, parse_rows


class NlTests(unittest.TestCase):
    def test_table_rows_and_date(self):
        html = ("<p>The overview was last updated on 5 October 2026.</p><table>"
                "<tr><th>Organisation</th><th>KvK number</th></tr>"
                "<tr><td>Beta B.V.</td><td>12345678</td></tr>"
                "<tr><td>Alpha N.V.</td><td>87654321</td></tr>"
                "<tr><td>Alpha N.V.</td><td>87654321</td></tr></table>")
        rows, updated = nl_parse(html)
        self.assertEqual(rows, [["Alpha N.V.", "87654321"], ["Beta B.V.", "12345678"]])
        self.assertEqual(updated, "2026-10-05")


class CaTests(unittest.TestCase):
    def test_latest_quarter(self):
        pkg = {"result": {"resources": [
            {"url": "https://open.canada.ca/x/tfwp_2025q4_pos_en.xlsx"},
            {"url": "https://open.canada.ca/x/tfwp_2026q1_pos_en.xlsx"},
            {"url": "https://open.canada.ca/x/tfwp_2026q1_pos_fr.xlsx"}]}}
        url, period = latest_resource(pkg)
        self.assertTrue(url.endswith("2026q1_pos_en.xlsx"))
        self.assertEqual(period, "2026-Q1")

    def test_rows(self):
        rows = [
            ["Positive LMIA employers, Q1 2026", None, None],
            [],
            ["Province/Territory", "Program Stream", "Employer", "Address", "Occupation", "Incorporate Status", "Approved LMIAs", "Approved Positions"],
            ["Ontario", "High-wage", "Acme Inc.", "Toronto, ON M5V", "21231-Software engineers", "Yes", 1, 2],
            ["Ontario", "High-wage", "Acme Inc.", "Toronto, ON M5V", "21231-Software engineers", "Yes", 1, 2],
            ["Alberta", "Agricultural stream", "Farm Ltd", "Red Deer, AB", "85100-Livestock labourers", "Yes", 1, "3"],
            ["Notes: something", None, None],
        ]
        out = parse_rows(rows)
        self.assertEqual(len(out), 3 - 1)
        self.assertEqual(out[0][0], "Acme Inc.")
        self.assertEqual(out[1][5], 3)

    def test_bad_header(self):
        with self.assertRaises(RuntimeError):
            parse_rows([["a", "b"], ["c", "d"]])


if __name__ == "__main__":
    unittest.main()
