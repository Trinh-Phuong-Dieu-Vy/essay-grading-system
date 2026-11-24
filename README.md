# Dự án: Hệ thống Kiểm tra đạo văn và Chấm điểm tự luận tự động

## 1. Giới thiệu đề tài
Hệ thống hỗ trợ giảng viên tải lên bài làm tự luận và đáp án mẫu, tự động chuẩn hóa văn bản tiếng Việt, phát hiện tỷ lệ trùng lặp (đạo văn) và gợi ý chấm điểm tự luận dựa trên độ tương đồng ngữ nghĩa.

## 2. Công nghệ & Kiến trúc hệ thống
- **Ngôn ngữ & Backend:** Python 3.x
- **Cơ sở dữ liệu:** MySQL
- **Kiến trúc:** Layered Architecture (4 tầng: `ui/`, `services/`, `models/`, `database/`)

## 3. Danh sách thành viên nhóm (6 thành viên)

| STT | Họ và Tên | Mã Sinh Viên | Vai trò / Phụ trách chính | Tài khoản GitHub |
| :---: | :--- | :--- | :--- | :--- |
| 1 | Trịnh Phương Diệu Vy | 25S1020117 | Nhóm trưởng – Quản lý dự án & Lõi AI/CSDL | @Trinh-Phuong-Dieu-Vy |
| 2 | [Thành viên 1 điền tên] | [MSSV] | Kiến trúc hệ thống & Giao diện (`ui/`) | @[username] |
| 3 | Nguyễn Đăng Thanh Huyền | 25S1020048 | Xử lý Model & Dữ liệu (`models/`, `database/`) | @thanhhuyn106-pixel |
| 4 | [Thành viên 3 điền tên] | [MSSV] | Xử lý tải lên & đọc dữ liệu file hàng loạt `.docx`, `.pdf`, `.txt` (`services/`) | @[username] |
| 5 | Võ Thị Lam Phương | 25S1020083 | Thiết lập thang điểm, trọng số từ khóa & giải thích chi tiết điểm (`services/`) | @Lamphuong211 |
| 6 | Nguyễn Thị Thanh Hiền | 25S1020034 | Đăng ký, đăng nhập, quản lý tài khoản & Kiểm thử (`tests/`) | @Thanhhien07-th |
