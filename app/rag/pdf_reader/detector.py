import fitz

def is_text_based_pdf(pdf_path, min_chars=50):
    doc = fitz.open(pdf_path)
    extracted = ""

    for page in doc:
        extracted += page.get_text()

    return len(extracted.strip()) >= min_chars
