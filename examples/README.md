# Runnable Examples

These examples use local files; do not upload private receipts or documents.
The VLM example needs a model download and optional GPU; the eval runs offline
with Python's standard library. Follow your organization's model-use policy.

| File | Approach | What it shows |
|------|----------|---------------|
| [vlm_extract.py](vlm_extract.py) | Vision-language model | Local image -> generated receipt fields with SmolVLM |
| [docling_extract.py](docling_extract.py) | Document AI | PDF -> clean Markdown/JSON for downstream extraction |
| [receipt_eval.py](receipt_eval.py) | Evaluation | JSONL predictions -> exact-match and per-field accuracy |

### Run the offline evaluation

From the repository root, without installing anything:

```sh
python3 examples/receipt_eval.py examples/sample_predictions.jsonl
python3 -m unittest discover -s examples -p 'test_*.py'
```

The two **synthetic** sample rows produce 50% exact match: they demonstrate
scoring, **not** real-world model performance. For actual measurements, prepare
consented, non-sensitive receipt images and ground-truth fields; run the VLM on
each image, review/parse its response into `predicted`, and write one JSONL row
per image with `id`, `expected`, and `predicted` objects. Each object has
`vendor`, `date` (ISO 8601), and `total` (decimal string or number); use JSON
`null` for genuinely absent values. Missing predicted fields count as errors.
Vendor comparisons ignore casing and repeated whitespace, totals compare as
decimals, and dates must match exactly. Validate output JSON yourself before
scoring: malformed model responses should be counted as failures, not silently
excluded. Don't commit private receipts or their extracted personal data.

For the full catalog of models, tools, and datasets, see the
[main list](../README.md).
