import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import streamlit as st
from services.compare_service import CompareService

st.set_page_config(page_title="Đối Chiếu Đạo Văn Chi Tiết", page_icon="🔍", layout="wide")
st.title("🔍 Giao Diện Đối Chiếu Chi Tiết Đoạn Trùng Lặp")

service = CompareService()
pairs = service.get_mock_comparisons()
selected_pair = st.selectbox("Chọn cặp bài làm cần đối chiếu:", [p["pair_name"] for p in pairs])
data = next(p for p in pairs if p["pair_name"] == selected_pair)

st.metric(
    "Tỷ lệ tương đồng phát hiện",
    f"{data['rate']}%",
    delta="Cảnh báo trùng lặp" if data["rate"] > 50 else "Mức trung bình",
    delta_color="inverse"
)

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.subheader(f"📄 {data['student_1']}")
        st.markdown(service.highlight_text(data["text_1"], data["matched_segments"]), unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        st.subheader(f"📄 {data['student_2']}")
        st.markdown(service.highlight_text(data["text_2"], data["matched_segments"]), unsafe_allow_html=True)