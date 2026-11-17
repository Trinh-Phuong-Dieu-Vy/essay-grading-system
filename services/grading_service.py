class GradingService:
    def calculate_final_score(self, raw_score: float, plagiarism_rate: float) -> float:
        if plagiarism_rate >= 80.0:
            return 0.0
        if plagiarism_rate > 20.0:
            return round(raw_score * 0.5, 2)
        return round(raw_score, 2)