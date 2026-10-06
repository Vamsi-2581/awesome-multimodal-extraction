"""Shared receipt prompt and strict JSON parser; intentionally dependency-free."""
import json
import re
from datetime import date
from decimal import Decimal, InvalidOperation

PROMPT = ('Read the receipt. Return only a JSON object with keys "vendor", '
          '"date" (YYYY-MM-DD), and "total" (non-negative decimal string). '
          'Use null when a field is not visible; never guess.')
FIELDS = {"vendor", "date", "total"}


def parse_receipt(response: str) -> dict:
    """Accept only a complete, explicitly typed receipt object; do not repair output."""
    try:
        value = json.loads(response, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
    except (TypeError, json.JSONDecodeError) as exc:
        raise ValueError("Model response is not a single JSON object") from exc
    if not isinstance(value, dict) or set(value) != FIELDS:
        raise ValueError("Model response must contain exactly vendor, date, total")
    vendor, day, total = (value[key] for key in ("vendor", "date", "total"))
    if vendor is not None and (not isinstance(vendor, str) or not vendor.strip()):
        raise ValueError("vendor must be a non-empty string or null")
    if day is not None:
        if not isinstance(day, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", day):
            raise ValueError("date must be YYYY-MM-DD or null")
        try:
            date.fromisoformat(day)
        except ValueError as exc:
            raise ValueError("date is not a calendar date") from exc
    if total is not None:
        if isinstance(total, bool) or not isinstance(total, (int, float, str)):
            raise ValueError("total must be a non-negative decimal or null")
        try:
            amount = Decimal(str(total))
        except InvalidOperation as exc:
            raise ValueError("total is not a decimal") from exc
        if not amount.is_finite() or amount < 0:
            raise ValueError("total must be a finite non-negative decimal")
    return value
