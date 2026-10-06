"""Image preparation and receipt extraction. Importing never downloads weights."""
from functools import lru_cache
from pathlib import Path
import sys
from time import monotonic

from PIL import Image

ROOT = Path(__file__).resolve().parent
EXAMPLES = ROOT if (ROOT / "receipt_inference.py").exists() else ROOT.parents[1] / "examples"
sys.path.insert(0, str(EXAMPLES))
from receipt_inference import PROMPT, parse_receipt  # noqa: E402

MODEL_ID = "HuggingFaceTB/SmolVLM-Instruct"
MAX_PIXELS = 16_000_000
MAX_SIDE = 1024


def prepare_image(image: Image.Image | None) -> Image.Image:
    if not isinstance(image, Image.Image):
        raise ValueError("Select a valid image before extracting.")
    if not image.width or not image.height or image.width * image.height > MAX_PIXELS:
        raise ValueError("Image is too large (limit: 16 million pixels).")
    try:
        result = image.convert("RGB")
        result.thumbnail((MAX_SIDE, MAX_SIDE))
        return result
    except (ValueError, OSError) as exc:
        raise ValueError("Could not read this image.") from exc


@lru_cache(maxsize=1)
def load_model():
    from transformers import AutoModelForImageTextToText, AutoProcessor
    model = AutoModelForImageTextToText.from_pretrained(MODEL_ID, device_map="auto")
    processor = AutoProcessor.from_pretrained(MODEL_ID)
    return model, processor


def run_model(image: Image.Image) -> str:
    model, processor = load_model()
    messages = [{"role": "user", "content": [
        {"type": "image"}, {"type": "text", "text": PROMPT},
    ]}]
    prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
    inputs = processor(text=prompt, images=[image], return_tensors="pt").to(model.device)
    output = model.generate(**inputs, max_new_tokens=128, do_sample=False)
    return processor.batch_decode(output[:, inputs["input_ids"].shape[-1]:],
                                  skip_special_tokens=True)[0]


def extract(image: Image.Image | None, inference=run_model) -> tuple[dict, str, str]:
    """Return parsed fields, raw text and human-readable status; never echo exceptions."""
    started = monotonic()
    try:
        image = prepare_image(image)
    except ValueError:
        return {}, "", "Select a valid image under 16 million pixels."
    try:
        raw = inference(image)
    except Exception:  # Model backend can fail for many reasons; never leak internals.
        return {}, "", "Model unavailable. Please retry later or use the offline evaluator."
    elapsed = monotonic() - started
    try:
        return parse_receipt(raw), raw, f"Generated in {elapsed:.2f} seconds. Verify every field."
    except ValueError:
        return {}, raw, f"Output invalid after {elapsed:.2f} seconds. No fields were inferred."
