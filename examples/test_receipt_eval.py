"""Unit tests for offline receipt-field scoring."""
import unittest

from receipt_eval import evaluate


class ReceiptEvalTests(unittest.TestCase):
    def test_normalization_and_partial_match(self):
        rows = [
            {"expected": {"vendor": "Corner Shop", "date": "2026-01-02", "total": "12.50"},
             "predicted": {"vendor": " corner  shop ", "date": "2026-01-02", "total": 12.5}},
            {"expected": {"vendor": "Market", "date": "2026-01-03", "total": "9.99"},
             "predicted": {"vendor": "Market", "date": "2026-01-03", "total": "8.99"}},
        ]
        self.assertEqual(evaluate(rows), {
            "count": 2, "exact_match": 0.5,
            "field_accuracy": {"vendor": 1.0, "date": 1.0, "total": 0.5},
        })

    def test_missing_prediction_is_wrong_even_for_null(self):
        result = evaluate([{"expected": {"vendor": None, "date": None, "total": None},
                            "predicted": {}}])
        self.assertEqual(result["exact_match"], 0)
        self.assertEqual(result["field_accuracy"]["vendor"], 0)

    def test_empty_and_invalid_rows(self):
        with self.assertRaises(ValueError):
            evaluate([])
        with self.assertRaises(ValueError):
            evaluate([{"expected": {}, "predicted": {}}])


if __name__ == "__main__":
    unittest.main()
