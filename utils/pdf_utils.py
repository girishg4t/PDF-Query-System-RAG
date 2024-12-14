from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path):
    try:
        # Pass the SpooledTemporaryFile to PdfReader
        pdf_reader = PdfReader(pdf_path)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        # Splitting based on lines or customize as needed
        sentences = text.split("\n")
        sentences = [sentence.strip()
                     for sentence in sentences if sentence.strip()]
        return sentences
    except Exception as e:
        return None
