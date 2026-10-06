"""Interactive, CPU-only demo of the repository's receipt-field evaluator."""
import json
from pathlib import Path
import sys

import gradio as gr

# The Space copies the shared scorer beside app.py; a checkout uses examples/.
ROOT = Path(__file__).resolve().parent
EXAMPLES = ROOT if (ROOT / "receipt_eval.py").exists() else ROOT.parents[1] / "examples"
sys.path.insert(0, str(EXAMPLES))
from receipt_eval import evaluate  # noqa: E402

SAMPLE = EXAMPLES / "sample_predictions.jsonl"


def score(text: str) -> tuple[dict, str]:
    """Parse a bounded JSONL payload and return metrics or a safe error."""
    if len(text) > 32_000:
        return {}, "Input is too large (limit: 32,000 characters)."
    lines = [line for line in text.splitlines() if line.strip()]
    if not 1 <= len(lines) <= 100:
        return {}, "Provide between 1 and 100 non-empty JSONL rows."
    try:
        rows = [json.loads(line) for line in lines]
        result = evaluate(rows)
    except (ValueError, TypeError, KeyError):
        return {}, "Invalid JSONL or missing expected/predicted fields. See the format below."
    return result, "Synthetic sample metrics are not a benchmark. Use your own labeled data to evaluate a model."


with gr.Blocks(title="Receipt Extraction: Measure It") as demo:
    gr.Markdown("# Receipt extraction: measure it\n"
                "A live, **CPU-only evaluation demo** from the "
                "[Awesome Multimodal Extraction](https://github.com/shivamnegi92/awesome-multimodal-extraction) "
                "repository. This scores predictions; **it does not run a vision model**.")
    gr.Markdown("Paste one JSON object per line with `expected` and `predicted` "
                "objects containing `vendor`, `date` (YYYY-MM-DD), and `total`. "
                "The preloaded rows are synthetic. Do not enter receipts or personal data. "
                "Your inputs are sent to this public Space for processing.")
    data = gr.Textbox(value=SAMPLE.read_text(encoding="utf-8"), lines=9,
                      label="Synthetic example: edit the predictions", max_lines=20)
    run = gr.Button("Score predictions", variant="primary")
    metrics = gr.JSON(label="Exact match and per-field accuracy")
    note = gr.Textbox(label="Status", interactive=False)
    run.click(score, inputs=data, outputs=[metrics, note], api_name=False)
    gr.Markdown("**Method:** vendor ignores casing and repeated whitespace; "
                "totals compare as decimals; dates must match exactly. "
                "Missing predictions count as wrong, even for null ground truth. "
                "[See the scorer, tests, and limitations](https://github.com/shivamnegi92/awesome-multimodal-extraction/tree/main/examples). "
                "Run an actual model locally with the linked example; model quality "
                "cannot be inferred from this synthetic dataset.")


if __name__ == "__main__":
    demo.launch()
