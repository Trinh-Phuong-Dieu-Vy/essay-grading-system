import docx

def extract_text_from_docx(uploaded_file) -> str:
    """Đọc toàn bộ đoạn văn bản từ file .docx tải lên"""
    doc = docx.Document(uploaded_file)
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    return "\n".join(paragraphs)