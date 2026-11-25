import streamlit as st

st.set_page_config(
    page_title="Hệ Thống Kiểm Tra Đạo Văn & Chấm Tự Luận",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Hệ Thống Kiểm Tra Đạo Văn & Chấm Điểm Tự Luận Tự Động")

if "user_id" in st.session_state:
    st.success(f"👋 Xin chào giảng viên: **{st.session_state['user_name']}**")
    st.info("👈 Vui lòng chọn các chức năng tương ứng ở thanh menu bên trái.")
else:
    st.warning("⚠️ Bạn chưa đăng nhập. Vui lòng chọn trang **1_Tai_Khoan** ở thanh menu bên trái để đăng nhập hoặc đăng ký!")
