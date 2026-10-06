"""Gradio receipt inference demo. Model loads on first request, not import."""
from pathlib import Path

import gradio as gr

from backend import extract

HERE = Path(__file__).resolve().parent

with gr.Blocks(title="Receipt extraction: from image to fields") as demo:
    gr.Markdown("# Receipt extraction: from image to fields\n"
                "Try a **fictional, synthetic** receipt or upload a non-sensitive image. "
                "This demo uses SmolVLM to generate text, then validates its JSON. "
                "Fields can be wrong; verify against the image. "
                "[Source and evaluation](https://github.com/shivamnegi92/awesome-multimodal-extraction).")
    gr.Markdown("**Privacy:** Uploads are sent to Hugging Face for processing. "
                "Do not upload real receipts with payment details or personal data. "
                "This app does not intentionally persist images or predictions, but "
                "the hosting platform/Gradio may cache files and log requests. First inference "
                "may be slow while model weights download.")
    image = gr.Image(type="pil", label="Receipt image (synthetic examples below)",
                     sources=["upload"], image_mode="RGB")
    gr.Examples(examples=[[str(HERE / "samples" / "fictional-receipt.png")]],
                inputs=image, label="Synthetic sample; no private information")
    button = gr.Button("Extract receipt fields", variant="primary")
    fields = gr.JSON(label="Validated vendor, date, total")
    raw = gr.Textbox(label="Raw model output", interactive=False)
    status = gr.Textbox(label="Status and elapsed time", interactive=False)
    button.click(extract, inputs=image, outputs=[fields, raw, status], api_name=False)
    gr.Markdown("If parsing fails, the raw answer remains visible and fields remain empty. "
                "[Score your own labeled results offline](https://github.com/shivamnegi92/awesome-multimodal-extraction/tree/main/examples). "
                "The sample is not a model benchmark.")

if __name__ == "__main__":
    demo.launch()
