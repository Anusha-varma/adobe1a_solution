import fitz  # PyMuPDF
import os
import json
from utils import extract_outline

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def process_pdf(file_path, output_path):
    doc = fitz.open(file_path)
    outline_json = extract_outline(doc)
    with open(output_path, "w") as f:
        json.dump(outline_json, f, indent=2)

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            input_pdf = os.path.join(INPUT_DIR, filename)
            output_json = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))
            process_pdf(input_pdf, output_json)

if __name__ == "__main__":
    main()