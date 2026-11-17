import re

class TextProcessor:
    def preprocess_text(self, text: str) -> list:
        clean = re.sub(r'[^\w\s]', '', text.lower())
        return clean.split()