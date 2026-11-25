# Nghiên cứu Mô hình Chấm điểm Tự luận Tự động (SCRUM-27)

## 1. Phương pháp chấm điểm kết hợp (`grading_service.py`)
Hệ thống so sánh bài làm sinh viên với đáp án mẫu của giảng viên trong MySQL dựa trên 2 thành phần:

### A. Chấm điểm từ khóa (Keyword Matching)
- **Thư viện:** `underthesea` + `rapidfuzz` (so khớp mờ để chấp nhận sai sót chính tả nhỏ).
- **Cách tính:** Tách danh sách từ khóa trọng tâm từ đáp án mẫu -> tính tỷ lệ số từ khóa xuất hiện đúng trong bài làm sinh viên (`Score_KW` thuộc `[0, 1]`).

### B. Chấm điểm ngữ nghĩa (Semantic Similarity)
- **Thư viện & Mô hình:** `sentence-transformers` sử dụng mô hình tiếng Việt **`keepitreal/vietnamese-sbert`**.
- **Cách tính:** Chuyển đoạn trả lời của sinh viên và đáp án mẫu thành vector đặc trưng -> tính `Cosine Similarity` để đánh giá độ trùng khớp về mặt ý nghĩa ngay cả khi sinh viên diễn đạt khác câu chữ (`Score_Sem` thuộc `[0, 1]`).

## 2. Công thức tính điểm & Xuất giải thích chi tiết (Phục vụ SCRUM-15, SCRUM-17)
- **Công thức tổng hợp:**
  `Điểm_câu = Thang_điểm_tối_đa * (W_kw * Score_KW + W_sem * Score_Sem)`
  *(Với `W_kw` và `W_sem` là trọng số do giảng viên thiết lập ở màn hình cấu hình)*.
- **Dữ liệu trả về cho `ui/`:** Xuất danh sách từ khóa **Đạt**, từ khóa **Thiếu** và **% tương đồng ý nghĩa** giúp giảng viên dễ dàng theo dõi và điều chỉnh điểm thủ công.
