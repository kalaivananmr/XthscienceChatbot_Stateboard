import pytesseract
from pdf2image import convert_from_path

def load_pdf_with_ocr(pdf_path, dpi=300):
    images = convert_from_path(pdf_path, dpi=dpi)
    text = []

    for i, img in enumerate(images):
        page_text = pytesseract.image_to_string(img, lang="eng")
        if page_text.strip():
            text.append(page_text)

    return "\n".join(text)
