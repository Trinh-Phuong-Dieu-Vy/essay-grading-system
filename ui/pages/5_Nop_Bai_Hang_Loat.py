import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import streamlit as st
from services.file_parser import extract_text_from_docx
from services.submission_service import SubmissionService
from services.assignment_service import AssignmentService

st.set_page_config(page_title="Tải Bài Làm Hàng Loạt", page_icon="📂", layout="wide")
st.title("📂 Tải Lên Hàng Loạt Bài Làm Tự Luận (.docx)")

assign_service = AssignmentService()
sub_service = SubmissionService()

assignments = assign_service.get_all_assignments()
if not assignments:
    st.warning("⚠️ Chưa có đề bài nào trong hệ thống!")
    st.stop()

options = {f"#{a['id']} - {a['title']}": a["id"] for a in assignments}
selected = st.selectbox("Chọn đề bài tương ứng:", list(options.keys()))
assignment_id = options[selected]

st.info("💡 Quy ước đặt tên file: `MaSV_HoTen.docx` (VD: `22T102001_NguyenVanA.docx`) để hệ thống tự tách thông tin sinh viên.")
uploaded_files = st.file_uploader("Chọn nhiều file bài làm (.docx) cùng lúc:", type=["docx"], accept_multiple_files=True)

if uploaded_files and st.button(f"🚀 Tải lên {len(uploaded_files)} bài làm", type="primary"):
    progress = st.progress(0)
    for idx, f in enumerate(uploaded_files):
        base_name = f.name.rsplit(".", 1)[0]
        parts = base_name.split("_", 1)
        student_code = parts[0]
        student_name = parts[1] if len(parts) > 1 else "Chưa rõ tên"
        
        content = extract_text_from_docx(f)
        sub_service.save_submission(assignment_id, student_code, student_name, f.name, content)
        progress.progress((idx + 1) / len(uploaded_files))
    st.success(f"✅ Đã tải lên và trích xuất thành công {len(uploaded_files)} bài làm!")

st.divider()
st.subheader("📋 Danh Sách Bài Làm Đã Nộp")
subs = sub_service.get_submissions(assignment_id)
if subs:
    st.dataframe(subs, use_container_width=True)
else:
    st.caption("Chưa có bài làm nào được tải lên cho đề bài này.")
