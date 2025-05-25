# Feature 10.py implementation here

import streamlit as st
from fpdf import FPDF
import io

def app():
    st.header("📄 পিডিএফ প্রতিবেদন তৈরি")
    st.markdown("""
    ব্যবহারকারীর ইনপুট ডেটা থেকে সহজে পিডিএফ প্রতিবেদন তৈরি করুন।
    """)

    # ইউজার ইনপুট
    report_title = st.text_input("প্রতিবেদনের শিরোনাম", "Eco River AI প্রতিবেদন")
    river_name = st.text_input("নদীর নাম", "পদ্মা")
    observations = st.text_area("পর্যবেক্ষণ", "এখানে নদীর অবস্থা লিখুন...")
    recommendations = st.text_area("প্রস্তাবনা", "এখানে সুপারিশ লিখুন...")

    if st.button("পিডিএফ তৈরি করুন"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, report_title, ln=True, align="C")

        pdf.set_font("Arial", '', 12)
        pdf.ln(10)
        pdf.cell(0, 10, f"নদীর নাম: {river_name}", ln=True)
        pdf.ln(5)
        pdf.multi_cell(0, 10, f"পর্যবেক্ষণ:\n{observations}")
        pdf.ln(5)
        pdf.multi_cell(0, 10, f"প্রস্তাবনা:\n{recommendations}")

        # PDF বাফার তৈরি
        pdf_output = io.BytesIO()
        pdf.output(pdf_output)
        pdf_output.seek(0)

        st.success("পিডিএফ তৈরি হয়েছে!")
        st.download_button(
            label="পিডিএফ ডাউনলোড করুন",
            data=pdf_output,
            file_name="eco_river_report.pdf",
            mime="application/pdf"
        )

