import pdfplumber
import re
import os

def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n\n"
    return clean_text(text)

def clean_text(text):
    # remove page numbers like "12" or "Page 12"
    text = re.sub(r"\bPage\s*\d+\b", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^\s*\d+\s*$", "", text, flags=re.MULTILINE)

    # collapse extra spaces
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()

def chunk_text(text, chunk_size=400):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

def process_pdf(path, chunk_size=400):
    raw = extract_text_from_pdf(path)
    chunks = chunk_text(raw, chunk_size)
    return chunks

# #checks if the file exists (prolly a good idea to have this here or make it into try-except itf)
# path = r"D:\Github\rag-enhanced-llm-quizgen\3.0 - Overview of Game Design.pdf"
# print(os.path.exists(path))

# chunks = process_pdf(r"D:\Github\rag-enhanced-llm-quizgen\3.0 - Overview of Game Design.pdf")

# print("Total chunks:", len(chunks))
# print(chunks[2])   # preview the chunk idk man

