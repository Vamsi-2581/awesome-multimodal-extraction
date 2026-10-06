"""Space smoke checks using a lightweight Gradio stub (no network needed)."""
import importlib.util
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import patch


class Component:
    def __init__(self, *args, **kwargs):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def click(self, *args, **kwargs):
        pass


class SpaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        gradio = types.SimpleNamespace(**{name: Component for name in
            ("Blocks", "Markdown", "Textbox", "Button", "JSON")})
        path = Path(__file__).with_name("app.py")
        spec = importlib.util.spec_from_file_location("receipt_space", path)
        module = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {"gradio": gradio}):
            spec.loader.exec_module(module)
        cls.score = staticmethod(module.score)

    def test_sample_metrics(self):
        sample = Path(__file__).parents[2] / "examples" / "sample_predictions.jsonl"
        metrics, _ = self.score(sample.read_text(encoding="utf-8"))
        self.assertEqual(metrics["exact_match"], 0.5)

    def test_bad_input(self):
        for payload in ("", "not JSON", "x" * 32_001, '{}'):
            with self.subTest(payload=payload[:15]):
                metrics, message = self.score(payload)
                self.assertEqual(metrics, {})
                self.assertTrue(message)


if __name__ == "__main__":
    unittest.main()
