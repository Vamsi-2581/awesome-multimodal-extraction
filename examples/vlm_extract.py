"""Extract receipt fields with Hugging Face's SmolVLM (local inference).

Setup (CPU is possible but slow; a GPU is recommended):
    uv pip install transformers torch pillow accelerate

Run:
    python examples/vlm_extract.py path/to/receipt.jpg

Review model output before using it: a VLM can hallucinate fields. The output is
not guaranteed to be valid JSON; use the offline eval for measured accuracy.
"""
import argparse

from PIL import Image
from transformers import AutoModelForImageTextToText, AutoProcessor

MODEL_ID = "HuggingFaceTB/SmolVLM-Instruct"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", help="Path to a local receipt image")
    args = parser.parse_args()

    model = AutoModelForImageTextToText.from_pretrained(MODEL_ID, device_map="auto")
    processor = AutoProcessor.from_pretrained(MODEL_ID)
    with Image.open(args.image) as source:
        image = source.convert("RGB")
    messages = [{"role": "user", "content": [
        {"type": "image"},
        {"type": "text", "text": (
            'Read this receipt. Return only a JSON object with keys "vendor", '
            '"date" (YYYY-MM-DD), and "total" (decimal string, no currency symbol). '
            "Use null when a field is not visible; do not guess."
        )},
    ]}]
    prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
    inputs = processor(text=prompt, images=[image], return_tensors="pt").to(model.device)
    output = model.generate(**inputs, max_new_tokens=128, do_sample=False)
    generated = output[:, inputs["input_ids"].shape[-1]:]
    print(processor.batch_decode(generated, skip_special_tokens=True)[0])


if __name__ == "__main__":
    main()
