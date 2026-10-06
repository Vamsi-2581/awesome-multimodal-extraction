# Findings: receipt inference Space planning

- Current public repo on this machine is at main, two commits ahead of origin/main (4786f3c, 47d8d3a), with no live Space verified or deployed.
- `spaces/receipt-eval/` is a CPU-only Gradio scorer over synthetic JSONL. It does not accept images or run OCR/VLM. It has a publish script, smoke tests, and pinned Gradio version, but no network-backed launch verification.
- `examples/vlm_extract.py` uses HuggingFaceTB/SmolVLM-Instruct locally to generate text. It does not validate generated JSON, normalize fields, score ground truth, or report latency. Its model download, hardware requirements, license and exact deployment API have not been verified in this environment.
- `examples/receipt_eval.py` scores exact match and per-field accuracy with two synthetic samples and unit tests. These scores are examples, not empirical model performance.
- Previous session: huggingface.co DNS lookup failed. Do not claim that any Space builds, model card is approved, or model weights download successfully until verified on a reachable network.
- User policy: never use Chinese-origin models, including fallback/baseline/embedding choices. No personal or confidential receipt uploads to a public Space; test fixtures must be synthetic or explicitly licensed/consented and inspected before commit.
- The next product should be a separate public inference Space rather than quietly changing the evaluator's behavior or claiming popularity gains from an unpublished demo.
