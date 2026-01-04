import re

def extract_chemical_equations(text):
    pattern = r"[A-Z][a-z]?\d*(?:\+[A-Z][a-z]?\d*)*→[A-Z][a-z]?\d*"
    return re.findall(pattern, text)
