import fitz

def load_text_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = []

    for page in doc:
        page_text = page.get_text().strip()
        if page_text:
            text.append(page_text)

    return "\n".join(text)
