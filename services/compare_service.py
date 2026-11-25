class CompareService:
    def get_mock_comparisons(self):
        return [
            {
                "pair_name": "22T102001 - Nguyễn Văn A  VS  22T102005 - Trần Thị B",
                "rate": 68.5,
                "student_1": "Nguyễn Văn A (22T102001)",
                "student_2": "Trần Thị B (22T102005)",
                "text_1": "Scrum là một khung làm việc Agile giúp các nhóm phát triển sản phẩm phức tạp. Trong Scrum, Product Backlog là danh sách tất cả các tính năng cần làm được sắp xếp theo độ ưu tiên từ cao xuống thấp.",
                "text_2": "Theo lý thuyết môn học, Product Backlog là danh sách tất cả các tính năng cần làm được sắp xếp theo độ ưu tiên từ cao xuống thấp. Nhóm sẽ chọn các mục này đưa vào Sprint Backlog.",
                "matched_segments": [
                    "Product Backlog là danh sách tất cả các tính năng cần làm được sắp xếp theo độ ưu tiên từ cao xuống thấp"
                ]
            },
            {
                "pair_name": "22T102003 - Lê Văn C  VS  Đáp án mẫu",
                "rate": 42.0,
                "student_1": "Lê Văn C (22T102003)",
                "student_2": "Đáp án mẫu của giảng viên",
                "text_1": "Kiểm thử hộp đen tập trung vào đầu vào và đầu ra của phần mềm mà không cần quan tâm đến cấu trúc mã nguồn bên trong.",
                "text_2": "Kiểm thử hộp đen tập trung vào đầu vào và đầu ra của phần mềm mà không cần quan tâm đến cấu trúc mã nguồn bên trong chương trình.",
                "matched_segments": [
                    "Kiểm thử hộp đen tập trung vào đầu vào và đầu ra của phần mềm mà không cần quan tâm đến cấu trúc mã nguồn bên trong"
                ]
            }
        ]

    def highlight_text(self, full_text: str, segments: list) -> str:
        result = full_text
        for seg in segments:
            result = result.replace(
                seg,
                f'<mark style="background-color: #ffcccc; color: #990000; font-weight: bold; padding: 2px 4px; border-radius: 4px;">{seg}</mark>'
            )
        return result