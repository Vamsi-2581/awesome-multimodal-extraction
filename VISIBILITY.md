# Discovery and community plan

This is a practical plan for making **Awesome Multimodal Extraction** easier to find and more useful once people arrive. It favors durable search relevance, evidence, and real participation over manufactured activity. It does not promise a star count or ranking.

## Positioning

**One-line promise:** Find the right models, tools, datasets, and examples to turn images, documents, audio, and video into structured information.

The differentiator is the bridge between the multimodal-NER research lineage and today's VLM/document-AI workflows, with runnable examples and link-checked curation. Keep that promise consistent in the repository description, README opening, social posts, and contribution requests.

The repository currently has **2 stars, 0 forks, and no release tags** (checked 2026-10-11); these are a baseline snapshot, not success measures or proof of quality. It has link-check and offline-test workflows, runnable examples, and clear limits on its synthetic evaluation. The README task guide is a useful starting point. One conspicuous field gap: practical users still cannot quickly compare source evidence/coordinates, table and reading-order fidelity, multilingual/handwriting support, privacy and execution mode, or evaluation methodology across tools. The release improves guidance on those gaps; a validated per-tool matrix and failure gallery remain future work.

## What already works

- Breadth across OCR/document AI, VLMs, charts, audio/video, and multimodal NER.
- A task decision flowchart and local examples.
- Offline receipt evaluator with synthetic data clearly labeled as illustrative.
- Link and Awesome-style CI, plus contribution guidance.

These are useful foundations. Do not represent synthetic sample scores as model performance or claim a live inference demo when none is verified.

## What the field still needs—and what this repo could own

The repository is not missing yet another broad model inventory. A practitioner still has to open many projects to learn whether they produce page coordinates, preserve table structure and reading order, handle handwriting or multilingual text, run offline, or permit a given use. These are the biggest useful gaps to address:

1. **Evidence/provenance:** where did each extracted field come from? Surface page/frame, bounding box and coordinate convention, source text/crop, and whether confidence is calibrated. A value without evidence is hard to audit.
2. **Comparable metadata:** input and output formats, languages, table/formula/handwriting support, CPU/GPU, offline/hosted mode, license/weight terms, maintenance status, and source of each claim. Track only facts verified from official docs; unknown is a valid value.
3. **Evaluation beyond NER:** OCR text error, field correctness, table structure/cell quality, reading order, chart values, schema validity, evidence localization, latency/cost, and robustness. Metrics should not be collapsed into one “best tool” score.
4. **Privacy and hostile input:** dataset rights, remote processing/retention, PII/redaction, malicious files, and prompt injection in documents. Warn readers to sandbox untrusted files; do not collect or publish private examples.
5. **Task-specific workflows:** distinguish PDF-to-structure, document field extraction, tables-to-data, chart-to-data, image-text entities, and audio/video timelines. Keep non-document modalities only when the output is grounded and structured.
6. **Reproducible failures:** show missing-field hallucination, date/amount normalization mistakes, shifted table cells, wrong reading order, weak OCR, or incorrect citations—only using synthetic or properly licensed material, with expected vs. actual output and a documented test.

Adjacent projects worth learning from include [Docling](https://github.com/docling-project/docling) and [MinerU](https://github.com/opendatalab/MinerU) for structured, agent-ready document representations; [olmOCR](https://github.com/allenai/olmocr) for quality/cost/evaluation context; [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) for language and deployment breadth; and [MarkItDown](https://github.com/microsoft/markitdown) for format conversion and security caveats. They are adjacent exemplars, not direct rankings or a live trend chart.

The release adds links for [OmniDocBench](https://github.com/opendatalab/OmniDocBench), [XFUND](https://github.com/doc-analysis/XFUND), and [SROIE](https://github.com/zzzDavid/ICDAR-2019-SROIE), plus practical evaluation, provenance, and privacy guidance. These are reference resources—not scores for listed tools or proof that metrics are comparable.

## Ethical discovery loop

1. **Be useful for real search intent.** Keep task language in headings and descriptions: PDF extraction, OCR, tables, charts, receipt fields, document layout, image-text entity extraction, audio transcription, and structured JSON. The task map belongs near the top of the README.
2. **Ship evidence, not hype.** Expand small offline examples and tests. If publishing comparisons, document data rights, model revision, prompt/configuration, hardware, sample size, metrics, and failure cases. Synthetic examples demonstrate mechanics only; do not market their scores as real performance.
3. **Earn referrals upstream.** Improve missing docs, examples, or broken links in projects before mentioning the list. Ask maintainers before using their name/brand in a promotional context.
4. **Publish substantive updates sparingly.** A curation release should explain actual changes—new categories, a useful comparison, a corrected guide, or removed stale projects. Do not create trivial commits just to look active.
5. **Ask for contributions with bounded issues.** Each request should define a small artifact, acceptance checks, and a friendly invitation. Good targets include a verified entry, a dead-link report, an evaluation dimension, or a tested example.
6. **Share in relevant spaces only when welcome.** Use project discussions, research/developer forums, or a relevant newsletter/community with its rules respected. Lead with the useful artifact, disclose that you maintain the repository, and avoid repetitive cross-posting.
7. **Use GitHub-native discovery honestly.** Keep topics accurate, enable Issues/Discussions when moderation capacity exists, respond thoughtfully, and make first contributions low-friction. Do not use star exchanges, bought engagement, mass mentions, fake accounts, or unrelated issue/PR drops.
8. **Pursue list indexes when eligible.** Once the age and quality requirements are met, submit to the upstream [Awesome index](https://github.com/sindresorhus/awesome) as documented in [SUBMISSION.md](SUBMISSION.md). Respect its review process; inclusion is not guaranteed.

## Release plan

Do not tag a release until its contents are intentional and checks are green. For a first useful snapshot:

- Add a dated changelog and explicit snapshot limitations.
- Include practical field guidance on evidence/provenance, evaluation, and privacy/security.
- Add a citation file so users can cite the project and specific version.
- Point the README to release notes and the versioned citation.
- Run Awesome lint and the offline test suite. The link-check workflow is part of the trust signal; confirm its GitHub Actions result for the exact release commit before publishing.
- Create an annotated `v0.1.0` tag only on the reviewed release commit after checks pass; describe it as an initial curated snapshot, not an authoritative benchmark.
- Announce once with a concrete contribution ask (one verified gap/report/example). No star target, mass tagging, or engagement swaps.

After release, maintain a regular but sustainable cadence (for example, a meaningful quarterly curation snapshot), and publish changes when they are useful—not to manufacture activity. See [SUBMISSION.md](SUBMISSION.md) for the upstream Awesome-index gate.

Once the tagged release exists, announce it with one bounded ask for a verified resource, stale-link report, or evidence-backed example. Do not promise visibility, set a star target, mass-tag maintainers, or arrange engagement swaps.

Invite contributors to pick a **single small task** rather than asking vaguely for stars. Suggested sequence:

- **Now:** verify a candidate link or suggest a task missing from the catalog.
- **Next:** improve one example or add an offline test, with synthetic/licensed fixtures only.
- **Then:** help review a category for duplicates, stale projects, and unsupported descriptions.
- **Later:** propose an evidence-based mini-comparison with reproducible inputs and known limitations.

Use the public [help-wanted issue search](https://github.com/shivamnegi92/awesome-multimodal-extraction/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22), or open a focused issue with explicit acceptance criteria. Thank contributors in the merged PR/release notes; don't imply endorsement by projects listed here.

## 30-day operating plan

| Window | Work | Check for success |
|---|---|---|
| Days 1–3 | Confirm repository description/topics and issue templates; publish a bounded help-wanted task; link this plan from README. | A newcomer can find a task and understand how to submit it. |
| Week 1 | Ask 2–3 technically knowledgeable peers for private/read-only feedback; fix factual issues they identify. | Useful review notes and resulting corrections, not a star target. |
| Week 2 | Publish one small tutorial/comparison only if it is reproducible and permissions are clear; share once in a relevant venue that allows it. | Readers can reproduce it; feedback identifies gaps. |
| Week 3 | Review one category with community input; close or update stale entries and document decisions. | Fewer confusing/stale links; clear curation history. |
| Week 4 | Check available GitHub traffic/referral data, issue/PR activity, and example usage signals; record a baseline and choose the next change. | Evidence of what brought useful visitors or contributions; state when data is unavailable. |

## Measurement and guardrails

Record a baseline before promotion and review weekly/monthly, where GitHub exposes data:

- Repository unique visitors and clones, by date (limited retention/availability).
- Referrers and popular content when visible.
- Issues opened with reproducible suggestions, PRs opened/merged, and time to first maintainer response.
- Example test success and documented reproduction issues.
- Optional release/newsletter referrals, using aggregate counts only.

Do not scrape individual users, add tracking pixels, collect uploads, or infer success from stars alone. Never invent baseline numbers; note missing metrics explicitly. Prioritize repeat visitors, accurate reports, reproducibility, and healthy contributor experience. Revisit scope if maintenance workload exceeds maintainer capacity.

## Stop doing

- No purchased stars/followers, engagement pods, or star-for-star asks.
- No bulk tagging, spam comments, unrelated PRs/issues, or repetitive cross-posts.
- No competitor-description copying, unverified entries, or keyword stuffing.
- No unlicensed/private benchmark data, fabricated performance claims, or promises of visibility.
- No misleading implication that a scorer is a hosted inference demo.
