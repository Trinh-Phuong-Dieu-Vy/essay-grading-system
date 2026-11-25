import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import streamlit as st
import pandas as pd
from services.rubric_service import RubricService
from services.assignment_service import AssignmentService

st.set_page_config(page_title="Thiết Lập Thang Điểm", page_icon="⚖️", layout="wide")
st.title("⚖️ Thiết Lập Thang Điểm & Trọng Số Từng Ý")

assign_service = AssignmentService()
rubric_service = RubricService()

assignments = assign_service.get_all_assignments()
if not assignments:
    st.warning("⚠️ Chưa có đề bài nào. Vui lòng tạo đề bài ở trang 3_De_Va_Dap_An trước!")
    st.stop()

options = {f"#{a['id']} - {a['title']}": a["id"] for a in assignments}
selected = st.selectbox("Chọn đề bài cần cấu hình thang điểm:", list(options.keys()))
assignment_id = options[selected]

existing = rubric_service.get_rubrics(assignment_id)
if existing:
    df_init = pd.DataFrame([
        {"Nội dung ý chấm": r["idea_content"], "Điểm tối đa": r["max_score"], "Trọng số (%)": r["weight_percent"]}
        for r in existing
    ])
else:
    df_init = pd.DataFrame([
        {"Nội dung ý chấm": "Ý 1: Nêu đúng khái niệm", "Điểm tối đa": 4.0, "Trọng số (%)": 40.0},
        {"Nội dung ý chấm": "Ý 2: Phân tích ví dụ minh họa", "Điểm tối đa": 6.0, "Trọng số (%)": 60.0},
    ])

st.write("💡 Bấm vào dấu **+** ở cuối bảng để thêm ý chấm mới:")
edited_df = st.data_editor(df_init, num_rows="dynamic", use_container_width=True)

if st.button("💾 Lưu cấu hình thang điểm", type="primary"):
    total_weight = edited_df["Trọng số (%)"].sum()
    if abs(total_weight - 100.0) > 0.01:
        st.error(f"❌ Tổng trọng số hiện tại là **{total_weight}%**. Vui lòng điều chỉnh để bằng đúng **100%**!")
    else:
        items = [
            {
                "idea_content": row["Nội dung ý chấm"],
                "max_score": float(row["Điểm tối đa"]),
                "weight_percent": float(row["Trọng số (%)"])
            }
            for _, row in edited_df.iterrows() if str(row["Nội dung ý chấm"]).strip()
        ]
        rubric_service.save_rubrics(assignment_id, items)
        st.success("✅ Đã lưu thang điểm và trọng số thành công!")
