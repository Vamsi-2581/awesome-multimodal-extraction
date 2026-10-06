# Deploying the receipt evaluation Space

This is an interactive scorer, **not** an OCR/VLM inference demo. It needs no GPU,
model weights, secrets, or uploaded documents. The input box contains only
synthetic predictions. A public Space sends visitor text to Hugging Face; do not
submit sensitive receipts or personal data.

1. On a network with Hugging Face access, sign in to your own account. Install
   `huggingface_hub` through your approved package index if needed, then run
   `hf auth login` locally (never commit a token).
2. From the repository root, run
   `bash spaces/receipt-eval/publish.sh YOUR_USERNAME/receipt-extraction-eval`.
   The script publishes this folder plus the shared scorer and synthetic fixture
   to a public Gradio Space; inspect the staged files before publishing. If you
   don't want the CLI, create a Gradio Space in the web UI and upload `app.py`,
   `requirements.txt`, and `README.md` from this folder along with
   `examples/receipt_eval.py` and `examples/sample_predictions.jsonl` in the
   Space root. Do not upload `test_app.py` or any private data.
3. Check the Space build logs, click Score predictions, and verify that the
   synthetic example reports 0.5 exact match and 0.5 total accuracy. If the
   pinned Gradio release is unavailable, update both `sdk_version` in this
   folder's README and `requirements.txt` to the same tested release.
4. Only after the URL resolves and the smoke check passes, add it to the main
   repository README and share a short demo with the link. Ask for specific
   extraction failure cases and contributors rather than claiming benchmark
   performance. More visitors do not automatically mean useful adoption.

The deployment command requires an authenticated account and network access;
no deployment or public URL is assumed by this repository.
