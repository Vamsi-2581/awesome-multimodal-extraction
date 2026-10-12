# Contributing to Awesome Multimodal Extraction

Thanks for helping keep this a useful, current map of multimodal extraction—not a link dump. **A small, well-supported contribution is great.** First-time contributors are welcome.

## Good first contributions

Pick a small, verifiable improvement:

- Add one relevant, maintained model, tool, dataset, benchmark, paper, or tutorial.
- Fix a dead or redirected link, or flag an entry whose project is archived.
- Improve a description so it says what the project actually extracts or outputs.
- Add a missing task category or correct a misplaced entry.
- Improve an offline example or test without requiring private data or model downloads.
- Report a missing evaluation dimension or a reproducible failure case.

Browse [open help-wanted issues](https://github.com/shivamnegi92/awesome-multimodal-extraction/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22). If you plan a larger change, comment first so two people don't do the same work.

## The rules

1. **On topic and findable.** Tie the entry to an extraction task and use the right section. Pure text-only tools belong in the sibling [Awesome Entity Extraction](https://github.com/shivamnegi92/awesome-entity-extraction).
2. **Real, verifiable, and accurately described.** Link to the canonical project, model, dataset, or paper page. Say what it does; don't repeat unsupported marketing or “best/SOTA” claims.
3. **One concise line.** Format: `` - [Name](https://link) - What it does. ``
4. **Quality over quantity.** Don't add duplicates, abandoned projects without clear historical value, or links just for keyword coverage. CI checks link reachability; it cannot verify relevance or quality.
5. **Respect privacy and rights.** Never submit private documents, personal data, or benchmark images without permission. Don't imply a demo is live unless it has been tested.

We don't require a star threshold, and won't accept star exchanges, automated activity, or promotional entries. Popularity is not a quality metric.

## How to add an entry

1. Fork the repository and edit `README.md`.
2. Add a one-line entry under the section a reader would expect. Link to an official source where possible.
3. Run `python3 scripts/check-links.py` if you can; network restrictions may cause false negatives. CI runs the check on pull requests.
4. Open a pull request with one or two sentences explaining the use case and why the entry fits. If a tool's status or license is unclear, say so rather than guessing.

For code/examples, include an offline test where practical, document dependencies and limitations, and use only synthetic, consented, or properly licensed fixtures. Keep optional model/network tests out of the default unit-test path.

## Review and response

Maintainers aim to acknowledge contributions within seven days. That's a goal, not a guarantee; if there is no response after 14 days, leave a polite comment on the PR. Reviews prioritize fit, factual accuracy, accessibility, and maintainability—not stars or social reach. Please keep discussion kind and focused on the work.
