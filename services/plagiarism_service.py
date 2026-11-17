class PlagiarismService:
    def check_plagiarism(self, student_text: str, sample_text: str) -> float:
        s_words = set(student_text.lower().split())
        sample_words = set(sample_text.lower().split())
        if not s_words or not sample_words:
            return 0.0
        common = s_words.intersection(sample_words)
        return round((len(common) / len(sample_words)) * 100, 2)