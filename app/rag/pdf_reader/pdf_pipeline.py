from app.rag.pdf_reader.detector import is_text_based_pdf
from app.rag.pdf_reader.text_loader import load_text_pdf
from app.rag.pdf_reader.ocr_loader import load_pdf_with_ocr

def load_pdf_auto(pdf_path):
    if is_text_based_pdf(pdf_path):
        print("PDF detected as TEXT-based")
        return load_text_pdf(pdf_path)
    else:
        print("PDF detected as SCANNED – using OCR")
        return load_pdf_with_ocr(pdf_path)
