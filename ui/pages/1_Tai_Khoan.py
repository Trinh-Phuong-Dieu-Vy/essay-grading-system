import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import streamlit as st
from services.auth_service import AuthService

st.set_page_config(page_title="Quản Lý Tài Khoản", page_icon="🔐")
st.title("🔐 Quản Lý Tài Khoản Giảng Viên")

auth = AuthService()

if "user_id" in st.session_state:
    st.success(f"Đang đăng nhập: **{st.session_state['user_name']}** ({st.session_state['user_email']})")
    with st.form("update_form"):
        st.subheader("Cập nhật thông tin cá nhân")
        new_name = st.text_input("Họ và tên mới:", value=st.session_state["user_name"])
        new_pass = st.text_input("Mật khẩu mới (bỏ trống nếu không đổi):", type="password")
        if st.form_submit_button("💾 Lưu thay đổi"):
            auth.update_profile(st.session_state["user_id"], new_name, new_pass)
            st.session_state["user_name"] = new_name
            st.success("✅ Cập nhật thành công!")
    if st.button("🚪 Đăng xuất"):
        st.session_state.clear()
        st.rerun()
else:
    tab1, tab2 = st.tabs(["Đăng nhập", "Đăng ký tài khoản mới"])
    with tab1:
        email = st.text_input("Email:", key="login_email")
        password = st.text_input("Mật khẩu:", type="password", key="login_pass")
        if st.button("Đăng nhập", type="primary"):
            user = auth.login(email, password)
            if user:
                st.session_state["user_id"] = user["id"]
                st.session_state["user_name"] = user["full_name"]
                st.session_state["user_email"] = user["email"]
                st.success("✅ Đăng nhập thành công!")
                st.rerun()
            else:
                st.error("❌ Sai email hoặc mật khẩu!")
    with tab2:
        name = st.text_input("Họ và tên:")
        reg_email = st.text_input("Email:")
        reg_pass = st.text_input("Mật khẩu:", type="password")
        if st.button("Đăng ký"):
            if name and reg_email and reg_pass:
                if auth.register(name, reg_email, reg_pass):
                    st.success("✅ Đăng ký thành công! Vui lòng chuyển sang tab Đăng nhập.")
                else:
                    st.error("❌ Email này đã tồn tại!")
            else:
                st.warning("⚠️ Vui lòng điền đầy đủ thông tin!")
