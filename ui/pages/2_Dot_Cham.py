import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import streamlit as st
from services.course_service import CourseService

st.set_page_config(page_title="Quản Lý Đợt Chấm", page_icon="📚", layout="wide")
st.title("📚 Quản Lý Môn Học / Đợt Chấm Riêng Biệt")
lecturer_id = st.session_state.get("user_id", 1)
service = CourseService()

with st.form("create_course_form"):
    st.subheader("➕ Tạo Đợt Chấm / Môn Học Mới")
    c1, c2, c3 = st.columns(3)
    code = c1.text_input("Mã môn học:", placeholder="VD: CNPM2026")
    name = c2.text_input("Tên môn / Đợt chấm:", placeholder="VD: Công nghệ phần mềm - Nhóm 1")
    semester = c3.text_input("Học kỳ:", placeholder="VD: HK1 2026-2027")
    if st.form_submit_button("Tạo đợt chấm", type="primary"):
        if code.strip() and name.strip():
            service.create_course(lecturer_id, code.strip(), name.strip(), semester.strip())
            st.success("✅ Đã tạo đợt chấm mới thành công!")
        else:
            st.error("⚠️ Vui lòng nhập Mã môn và Tên môn học!")

st.divider()
st.subheader("📋 Danh Sách Các Đợt Chấm Đã Tạo")
courses = service.get_courses(lecturer_id)
if courses:
    for c in courses:
        col1, col2 = st.columns([5, 1])
        col1.info(f"**[{c['course_code']}] {c['course_name']}** — Học kỳ: {c['semester']}")
        if col2.button("🗑️ Xóa", key=f"del_{c['id']}"):
            service.delete_course(c["id"])
            st.rerun()
else:
    st.caption("Chưa có đợt chấm nào.")
    