"""Contract tests for the shared receipt response parser."""
import unittest

from receipt_inference import PROMPT, parse_receipt


class ParseTests(unittest.TestCase):
    def test_exact_object(self):
        self.assertEqual(parse_receipt('{"vendor":"Cafe", "date":"2026-02-01", "total":"12.50"}'),
                         {"vendor": "Cafe", "date": "2026-02-01", "total": "12.50"})

    def test_explicit_nulls(self):
        self.assertEqual(parse_receipt('{"vendor":null,"date":null,"total":null}'),
                         {"vendor": None, "date": None, "total": None})

    def test_rejects_malformed_fields_and_extra_text(self):
        bad = [
            'Sure: {"vendor":"Cafe","date":"2026-02-01","total":"12.50"}',
            '{"vendor":"Cafe","date":"2026-02-01","total":"12.50"} thanks',
            '{"vendor":"Cafe","date":"2026-02-01"}',
            '{"vendor":"Cafe","date":"2026-02-01","total":"12.50","extra":1}',
            '{"vendor":"Cafe","date":"2026-02-30","total":"12.50"}',
            '{"vendor":"Cafe","date":"02/01/26","total":"12.50"}',
            '{"vendor":"Cafe","date":"2026-02-01","total":"$12.50"}',
            '{"vendor":"Cafe","date":"2026-02-01","total":-3}',
            '{"vendor":true,"date":"2026-02-01","total":"12.50"}',
            '{}',
        ]
        for response in bad:
            with self.subTest(response=response), self.assertRaises(ValueError):
                parse_receipt(response)

    def test_prompt_is_explicit(self):
        for field in ("vendor", "date", "total", "null"):
            self.assertIn(field, PROMPT)


if __name__ == "__main__":
    unittest.main()
