import base64
from io import BytesIO


def process_image(image_file):
    """Converts uploaded PIL image to Base64 string for the API."""

    # ---------------------------------------------------------
    # FIX: Convert RGBA (PNG/Screenshot) to RGB (Standard JPEG)
    # ---------------------------------------------------------
    if image_file.mode in ("RGBA", "P"):
        image_file = image_file.convert("RGB")
    # ---------------------------------------------------------

    buffered = BytesIO()
    image_file.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{img_str}"