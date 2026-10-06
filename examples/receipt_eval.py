"""Offline receipt-field evaluation; no model download or third-party packages.

Input JSONL rows: {"id": "r1", "expected": {"vendor": ..., "date": ...,
"total": ...}, "predicted": {"vendor": ..., "date": ..., "total": ...}}.
Fields may be strings, numbers, or null. Missing fields count as incorrect.
"""
import argparse
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path

FIELDS = ("vendor", "date", "total")


def normalize(field: str, value: object) -> object:
    if value is None:
        return None
    if field == "total":
        try:
            return Decimal(str(value).strip())
        except InvalidOperation:
            return str(value).strip()
    if field == "vendor":
        return " ".join(str(value).casefold().split())
    return str(value).strip()


def evaluate(rows: list[dict]) -> dict:
    if not rows:
        raise ValueError("Provide at least one example")
    correct = {field: 0 for field in FIELDS}
    exact = 0
    for index, row in enumerate(rows, 1):
        if not isinstance(row, dict):
            raise ValueError(f"Row {index}: expected an object")
        expected, predicted = row.get("expected"), row.get("predicted")
        if not isinstance(expected, dict) or not isinstance(predicted, dict):
            raise ValueError(f"Row {index}: expected and predicted must be objects")
        if any(field not in expected for field in FIELDS):
            raise ValueError(f"Row {index}: expected must contain {', '.join(FIELDS)}")
        matches = []
        for field in FIELDS:
            matches.append(field in predicted and
                           normalize(field, expected[field]) == normalize(field, predicted[field]))
            correct[field] += matches[-1]
        exact += all(matches)
    count = len(rows)
    return {"count": count, "exact_match": exact / count,
            "field_accuracy": {field: correct[field] / count for field in FIELDS}}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jsonl", type=Path, help="Ground truth and predictions in JSONL")
    args = parser.parse_args()
    with args.jsonl.open(encoding="utf-8") as source:
        rows = [json.loads(line) for line in source if line.strip()]
    print(json.dumps(evaluate(rows), indent=2))


if __name__ == "__main__":
    main()
