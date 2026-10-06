# Image inference Space: verification gates

Status: **source prototype only**. This is separate from `spaces/receipt-eval/`,
which scores existing predictions. No image inference, HF build, hardware latency,
model license or public URL has been verified on this machine (HF DNS unavailable).
Do not advertise it as a working online demo before the gates below pass.

1. On a network with Hugging Face access, inspect the model card for
   `HuggingFaceTB/SmolVLM-Instruct`: license, origin, weights availability and
   intended inference API. Confirm the pinned versions in `requirements.txt`
   support the model/Space runtime; change them only after an actual install and
   synthetic-image run. No Chinese-origin models for fallbacks, tests or baselines.
2. For a local test: `uv venv` in this repo, then
   `uv pip install -r spaces/receipt-inference/requirements.txt --index-url https://pypi.ci.artifacts.walmart.com/artifactory/api/pypi/external-pypi/simple --allow-insecure-host pypi.ci.artifacts.walmart.com`.
   Run `python spaces/receipt-inference/app.py` from that venv. Click the synthetic
   example; record cold start, warm latency, memory and raw output. If free CPU
   is too slow or fails memory budget, do not deploy paid GPU without approval.
3. Run offline tests: `python3 -m unittest discover -s examples -p 'test_*.py'`
   and `python3 -m unittest discover -s spaces/receipt-inference -p 'test_*.py'`.
   Inspect keyboard focus, alt text, 320px-width usability and status text.
   Uploading private images is forbidden. The app does not intentionally persist
   inputs, but Gradio or the public host may cache uploads and log requests;
   do not promise zero retention.
4. Before publishing: check sample provenance, privacy wording, model revision,
   download size, licenses, rate/concurrency behavior, cold/warm runtime and cost;
   inspect staged files for secrets. Authentication and your choice of HF Space
   namespace are needed. Copy `app.py`, `backend.py`, `README.md`,
   `requirements.txt`, `samples/fictional-receipt.png` and
   `examples/receipt_inference.py` (as `receipt_inference.py`) into the Space root.
   Do not copy user documents or tests. Keep `HF_TOKEN` only in private secrets.
5. Once live: smoke test real model calls, malformed images and accessibility;
   only then add the verified URL to the main README. Measure real quality using
   separately licensed labeled data, not the synthetic sample. Track GitHub and
   HF engagement at launch, day 7 and day 30; state missing data honestly.
