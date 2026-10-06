"""Offline tests for image limits and model response handling (no weights download)."""
import sys
from pathlib import Path
import unittest
from unittest.mock import Mock

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from backend import extract, prepare_image


class ImageTests(unittest.TestCase):
    def test_resizes_rgb_and_checks_pixel_limit(self):
        image = Image.new("RGBA", (1800, 900), "white")
        prepared = prepare_image(image)
        self.assertEqual(prepared.mode, "RGB")
        self.assertLessEqual(max(prepared.size), 1024)
        with self.assertRaises(ValueError):
            prepare_image(Image.new("RGB", (6000, 6000)))

    def test_rejects_missing_and_broken_images(self):
        for image in (None, "bad"):
            with self.subTest(image=image), self.assertRaises(ValueError):
                prepare_image(image)

    def test_parses_success_without_logging_pixels(self):
        image = Image.new("RGB", (80, 40), "white")
        run_model = Mock(return_value='{"vendor":"Fictional Shop","date":"2026-01-02","total":"4.50"}')
        fields, raw, status = extract(image, run_model)
        self.assertEqual(fields["vendor"], "Fictional Shop")
        self.assertIn("Fictional Shop", raw)
        self.assertIn("seconds", status)
        run_model.assert_called_once()

    def test_invalid_response_and_model_failure_are_visible(self):
        image = Image.new("RGB", (80, 40), "white")
        fields, raw, status = extract(image, lambda _: "not json")
        self.assertEqual(fields, {})
        self.assertEqual(raw, "not json")
        self.assertIn("invalid", status.lower())
        fields, raw, status = extract(image, Mock(side_effect=RuntimeError("private input")))
        self.assertEqual(fields, {})
        self.assertEqual(raw, "")
        self.assertNotIn("private input", status)
        _, _, status = extract(image, Mock(side_effect=ValueError("private receipt")))
        self.assertNotIn("private receipt", status)


if __name__ == "__main__":
    unittest.main()
