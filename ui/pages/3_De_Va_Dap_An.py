import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import streamlit as st
from services.file_parser import extract_text_from_docx
from services.assignment_service import AssignmentService
from database.db_helper import DbHelper

st.set_page_config(page_title="Nộp Đề & Đáp Án Mẫu", page_icon="📝", layout="wide")
st.title("📝 Nộp Đề Bài Tự Luận & Đáp Án Mẫu")

service = AssignmentService()

# Lấy danh sách môn học/đợt chấm từ DB (nếu chưa có môn nào sẽ dùng ID mặc định = 1 để test)
def load_courses():
    try:
        conn = DbHelper().get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, course_code, course_name FROM courses")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception:
        return []

courses = load_courses()
course_options = {f"{c['course_code']} - {c['course_name']}": c["id"] for c in courses}

if not course_options:
    st.info("💡 Chưa có đợt chấm nào trong DB (SCRUM-13). Đang dùng tạm Mã đợt chấm = 1 để kiểm thử.")
    selected_course_id = 1
else:
    selected_label = st.selectbox("Chọn Đợt chấm / Môn học:", list(course_options.keys()))
    selected_course_id = course_options[selected_label]

title = st.text_input("Tiêu đề bài kiểm tra / đề thi:", placeholder="VD: Kiểm tra giữa kỳ - Công nghệ phần mềm")

input_method = st.radio(
    "Chọn hình thức nhập nội dung:",
    ["Tải lên file Word (.docx)", "Nhập văn bản trực tiếp"],
    horizontal=True
)

question_text = ""
sample_answer = ""

if input_method == "Tải lên file Word (.docx)":
    col1, col2 = st.columns(2)
    with col1:
        q_file = st.file_uploader("1. Tải file Đề bài (.docx)", type=["docx"], key="q_file")
        if q_file:
            question_text = extract_text_from_docx(q_file)
            st.text_area("Xem trước nội dung đề bài:", question_text, height=180, disabled=True)
    with col2:
        a_file = st.file_uploader("2. Tải file Đáp án mẫu (.docx)", type=["docx"], key="a_file")
        if a_file:
            sample_answer = extract_text_from_docx(a_file)
            st.text_area("Xem trước nội dung đáp án mẫu:", sample_answer, height=180, disabled=True)
else:
    col1, col2 = st.columns(2)
    with col1:
        question_text = st.text_area("Nhập nội dung Đề bài:", height=220)
    with col2:
        sample_answer = st.text_area("Nhập nội dung Đáp án mẫu:", height=220)

if st.button("💾 Lưu Đề bài & Đáp án mẫu", type="primary"):
    if not title.strip() or not question_text.strip() or not sample_answer.strip():
        st.error("⚠️ Vui lòng điền đầy đủ Tiêu đề, Đề bài và Đáp án mẫu!")
    else:
        try:
            new_id = service.create_assignment(selected_course_id, title.strip(), question_text.strip(), sample_answer.strip())
            st.success(f"✅ Đã lưu thành công Đề bài & Đáp án mẫu (ID = {new_id}) vào hệ thống!")
        except Exception as e:
            st.error(f"❌ Lỗi lưu dữ liệu: {e}")

st.divider()
st.subheader("📋 Danh sách Đề bài & Đáp án mẫu đã tải lên")
try:
    assignments = service.get_all_assignments()
    if assignments:
        for item in assignments:
            with st.expander(f"#{item['id']} - {item['title']}"):
                c1, c2 = st.columns(2)
                c1.markdown("**Đề bài:**")
                c1.write(item["question_text"])
                c2.markdown("**Đáp án mẫu:**")
                c2.write(item["sample_answer"])
    else:
        st.caption("Chưa có đề bài nào được lưu.")
except Exception as e:
    st.warning(f"Không thể tải danh sách: {e}")