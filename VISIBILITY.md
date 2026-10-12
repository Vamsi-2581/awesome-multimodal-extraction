# Discovery and community plan

This is a practical plan for making **Awesome Multimodal Extraction** easier to find and more useful once people arrive. It favors durable search relevance, evidence, and real participation over manufactured activity. It does not promise a star count or ranking.

## Positioning

**One-line promise:** Find the right models, tools, datasets, and examples to turn images, documents, audio, and video into structured information.

The differentiator is the bridge between the multimodal-NER research lineage and today's VLM/document-AI workflows, with runnable examples and link-checked curation. Keep that promise consistent in the repository description, README opening, social posts, and contribution requests.

## What similar successful projects teach us

Projects such as [Docling](https://github.com/docling-project/docling), [Marker](https://github.com/datalab-to/marker), [olmOCR](https://github.com/allenai/olmocr), [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR), and [MinerU](https://github.com/opendatalab/MinerU) show repeatable *product patterns*, not a recipe for copying their size or claims:

- A clear input-to-output promise and a task-based README front door.
- Runnable quickstarts, visible outputs, and honest limitations.
- Documentation about integrations, formats, licenses, hardware, and evaluation.
- Maintenance signals that matter: releases, working links, responsive reviews, and reproducible tests.
- A specific use case often gets remembered more easily than an undifferentiated list.

These repositories are adjacent exemplars, not all direct competitors or live trend rankings. Stars change over time and reflect many factors; do not present them as evidence of quality. See [field and repo review](findings.md) for comparison context.

## Ethical discovery loop

1. **Be useful for real search intent.** Keep task language in headings and descriptions: PDF extraction, OCR, tables, charts, receipt fields, document layout, image-text entity extraction, audio transcription, and structured JSON. The task map belongs near the top of the README.
2. **Ship evidence, not hype.** Expand small offline examples and tests. If publishing comparisons, document data rights, model revision, prompt/configuration, hardware, sample size, metrics, and failure cases. Synthetic examples demonstrate mechanics only; do not market their scores as real performance.
3. **Earn referrals upstream.** Improve missing docs, examples, or broken links in projects before mentioning the list. Ask maintainers before using their name/brand in a promotional context.
4. **Publish substantive updates sparingly.** A curation release should explain actual changes—new categories, a useful comparison, a corrected guide, or removed stale projects. Do not create trivial commits just to look active.
5. **Ask for contributions with bounded issues.** Each request should define a small artifact, acceptance checks, and a friendly invitation. Good targets include a verified entry, a dead-link report, an evaluation dimension, or a tested example.
6. **Share in relevant spaces only when welcome.** Use project discussions, research/developer forums, or a relevant newsletter/community with its rules respected. Lead with the useful artifact, disclose that you maintain the repository, and avoid repetitive cross-posting.
7. **Use GitHub-native discovery honestly.** Keep topics accurate, enable Issues/Discussions when moderation capacity exists, respond thoughtfully, and make first contributions low-friction. Do not use star exchanges, bought engagement, mass mentions, fake accounts, or unrelated issue/PR drops.
8. **Pursue list indexes when eligible.** Once the age and quality requirements are met, submit to the upstream [Awesome index](https://github.com/sindresorhus/awesome) as documented in [SUBMISSION.md](SUBMISSION.md). Respect its review process; inclusion is not guaranteed.

## Public contribution campaign

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
