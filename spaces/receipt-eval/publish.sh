#!/usr/bin/env bash
# Publish this folder as a public Hugging Face Space after authenticating.
set -euo pipefail

repo="${1:?Usage: bash spaces/receipt-eval/publish.sh HF_USERNAME/SPACE_NAME}"
if [[ ! "$repo" =~ ^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$ ]]; then
  echo "Expected HF_USERNAME/SPACE_NAME" >&2
  exit 2
fi
root="$(cd "$(dirname "$0")/../.." && pwd)"
space="$root/spaces/receipt-eval"
# Copies keep scorer and sample in sync with the source repo.
archive="$(mktemp -d)"
trap 'rm -rf "$archive"' EXIT
cp "$space/app.py" "$space/README.md" "$space/requirements.txt" "$archive/"
cp "$root/examples/receipt_eval.py" "$root/examples/sample_predictions.jsonl" "$archive/"
export UV_INDEX_URL="https://pypi.ci.artifacts.walmart.com/artifactory/api/pypi/external-pypi/simple"
export UV_INSECURE_HOST="pypi.ci.artifacts.walmart.com"
uvx --from huggingface_hub hf repo create "$repo" --repo-type space --space-sdk gradio --exist-ok
uvx --from huggingface_hub hf upload "$repo" "$archive" . --repo-type space
printf 'Check build logs and app at https://huggingface.co/spaces/%s\n' "$repo"
