# Nghiên cứu Thuật toán Kiểm tra Đạo văn Tiếng Việt (SCRUM-26)

## 1. Luồng xử lý tích hợp vào thư mục `services/`
1. **Đọc dữ liệu bài nộp (`docx_reader.py`):** Dùng thư viện `python-docx` trích xuất toàn bộ đoạn văn bản từ file `.docx` lưu trong hệ thống.
2. **Tiền xử lý ngôn ngữ tiếng Việt:**
   - Tách câu bằng `underthesea.sent_tokenize`.
   - Tách từ ghép tiếng Việt bằng `underthesea.word_tokenize(text, format="text")` (VD: `"kiểm tra đạo văn"` -> `"kiểm_tra đạo_văn"`).
   - Chuyển về chữ thường, loại bỏ dấu câu và từ dừng (*stopwords* tiếng Việt).
3. **So khớp độ tương đồng (`plagiarism_service.py`):**
   - Sử dụng **`TfidfVectorizer`** kết hợp **`cosine_similarity`** (thư viện `scikit-learn`) để tính ma trận tương đồng giữa từng câu của bài hiện tại với tất cả câu của các bài nộp khác trong cùng đợt chấm.
   - **Ngưỡng phát hiện:** Câu có độ tương đồng **>= 0.75** được đánh dấu trùng lặp, lưu vị trí câu + ID bài nguồn vào bảng kết quả trong MySQL để giao diện trong `ui/` bôi đỏ (`SCRUM-16`).
