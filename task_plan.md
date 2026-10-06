# Plan: image-to-fields Hugging Face Space and adoption loop

Status: planning complete; implementation and publication not started. Owner: Shivam. Scope: a **new** image inference Space that complements the existing offline evaluator, not a replacement for it. No Space URL, model-quality result, or visitor growth is claimed yet.

## Product promise and boundaries

A visitor selects a **synthetic sample receipt** or uploads their own non-sensitive image and sees the image, machine-generated raw answer, parsed `vendor` / `date` / `total`, inference time, and a frank warning when parsing or extraction fails. A second panel explains scoring against labeled synthetic examples and links back to the repository. No login, API key, personal-data collection, or unapproved model. Do not use Chinese-origin models (including baselines or fallback). Do not retain uploads or enable public examples from user uploads.

### Phase 0 — Verify feasibility before building

- On a reachable network, verify Hugging Face Space Gradio config, SDK and model card, provenance, license, download terms, exact transformers/processor API, pinned dependencies and CPU hardware limits. Candidate: HuggingFaceTB/SmolVLM-Instruct (used in `examples/vlm_extract.py`); investigate a smaller, non-Chinese-origin alternative only if necessary. Do not assume performance or free-tier fit.
- Run the candidate on one **synthetic, locally generated** receipt on a machine similar to the intended Space; record cold start, warm latency, RAM, output and approximate dependency/model size. Define a target: warm inference <= 20 seconds and memory comfortably under selected Space limit; these are launch gates, not measured results. If free CPU cannot meet the budget, prototype a GPU Space only after pricing and spend approval; otherwise ship just the scorer Space without mislabeling it as inference.
- Decide whether Shivam wants a public Space under his Hugging Face account and approves any paid hardware. Publishing requires account authentication and network access. Keep tokens outside git.

### Phase 1 — Make the real demo (local only first)

- Add a separate `spaces/receipt-inference/` Gradio app; share an import-safe inference/parse helper with `examples/vlm_extract.py` rather than duplicating prompt and schema rules. Lazy-load one pinned permitted model once per process; bound image dimensions/file size, generation length and concurrency. Use deterministic decoding, a timeout where feasible, and clear overload/cold-start messaging.
- Parse only a JSON object with keys `vendor`, `date`, `total`. Validate types and ISO date, decimal total, missing/null fields; show raw model response and parse errors instead of inventing values or silently accepting trailing text. Warn that generated results need human verification. Do not infer confidence scores from prose.
- Use 2–3 synthetic sample images with non-sensitive, plainly fictional data, including one hard example; label them synthetic. Upload policy: display a clear public-host privacy warning, no storage, no logging of pixels/field values, no analytics on raw inputs, no gallery of user uploads, no exposed Gradio prediction API unless explicitly approved. A public upload *still reaches Hugging Face*; do not promise local-only processing.
- WCAG 2.2 AA: explicit control labels, keyboard path, readable contrast, descriptive status/error text, image alt descriptions and non-color-only result indicators. Test on mobile-width and keyboard navigation.

### Phase 2 — Evidence before claims

- Create a small openly distributable, licensed or generated labeled test set; document image provenance, schema, split, field definitions, missing/null cases and potential generator leakage. Start with synthetic test fixtures for correctness, then add separately consented/appropriately licensed realistic images for any real-world claim. Never check in receipts containing personal data.
- Make a reproducible batch runner that saves predictions and elapsed time as JSONL and calls `examples/receipt_eval.py`; report sample count, exact-match and per-field accuracy plus latency distribution (median and p95), device, model revision, dependency versions, and failed/invalid-response rate. Include failure images only if rights permit; otherwise aggregate errors. Publish **no accuracy headline** from the existing two synthetic scorer rows.
- Tests planned: prompt/output parsing and malicious/malformed JSON; missing/null fields, Unicode vendor, currency/decimal errors and date validity; upload limits and corrupted images; no raw inputs in logs; deterministic batch evaluation; Gradio app render/smoke and keyboard/manual accessibility checks. CI runs lightweight mocked tests; a separate opt-in integration check downloads the model and runs one synthetic receipt. Model downloads must not run on every PR.

### Phase 3 — Release gate and distribution

- Review license, model origin, files copied to the Space, tokens, privacy copy and example image provenance; deploy to the chosen HF namespace only with Shivam's approval. Verify Space build logs, cold/warm calls, upload error states, and mobile/keyboard behavior; roll back to a previously verified revision if the Space fails. Keep the CPU-only scorer as a fallback **scoring tool**, never as a fake inference fallback.
- After the live URL passes smoke checks, add a prominent "Try a synthetic receipt" link and short clip to the GitHub README, link the GitHub repo from the Space, and provide a quick-start with expected output and honest limitations. Submit to relevant HF community pages only when appropriate; invite concrete issue reports and contributor fixes, not stars-for-stars or inflated metrics.
- Record baseline GitHub stars, unique visitors/clones, issue/PR contributions and HF Space likes/traffic if available. Compare at launch, day 7 and day 30. Qualitative success: users can complete the demo unaided, at least 3 actionable failure reports/PRs and a measurable increase in repo-to-Space engagement; if unavailable, state unavailable rather than guessing. Iterate on first-run failures before building another demo.

## Execution order and stop conditions

1. Feasibility approval (license, origin, performance, cost). **Stop** if model/card terms, hardware fit or network access cannot be verified.
2. Small runnable demo and synthetic fixtures; no publication until privacy and accessibility review pass.
3. Measured eval and smoke tests; label synthetic-only evidence appropriately.
4. Authenticated public deploy (only with approval), live verification, then promotion and metrics review.

Estimated effort **after feasibility**: 1–2 days for minimal image demo, 1–2 days for tests/fixtures and measurement, half a day for deployment/launch checks; hardware and network availability are the main unknowns. Avoid promising growth: a Space improves tryability, while a useful demo, honest evidence and consistent distribution drive adoption.

## Known blockers / errors

- Earlier attempt to reach `huggingface.co` from this machine failed DNS lookup; model/API/runtime/license cannot be verified here yet. Recheck on approved network before implementation or deployment.
- Current branch has local unpushed commits for the evaluator and CPU-only scorer Space; deploy only after reviewed code is pushed and verified.
