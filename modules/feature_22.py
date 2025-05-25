# Feature 22.py implementation here

import streamlit as st
from datetime import datetime, timedelta

def app():
    st.header("⏰ নির্ধারিত সময়ে ব্যবস্থা না নিলে অ্যালার্ট বৃদ্ধি")
    st.markdown("""
    এখানে আপনি নির্ধারিত সময়ের মধ্যে যদি ব্যবস্থা না নেন, তাহলে অ্যালার্ট স্বয়ংক্রিয়ভাবে বৃদ্ধি পাবে।
    """)

    st.write("অ্যালার্ট ইভেন্টের বিবরণ দিন:")

    event_description = st.text_area("অ্যালার্ট ইভেন্ট বর্ণনা")

    deadline = st.date_input("নির্ধারিত সময়সীমা নির্বাচন করুন")

    current_time = datetime.now()

    if st.button("অ্যালার্ট চেক করুন"):
        if not event_description.strip():
            st.error("অনুগ্রহ করে অ্যালার্ট ইভেন্টের বিবরণ দিন।")
        else:
            st.write(f"বর্তমান সময়: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
            st.write(f"নির্ধারিত সময়সীমা: {deadline.strftime('%Y-%m-%d')}")
            
            if current_time.date() > deadline:
                st.warning("⚠️ নির্ধারিত সময়সীমা অতিক্রান্ত! অ্যালার্টের তীব্রতা বৃদ্ধি করুন।")
            else:
                st.success("নির্ধারিত সময়সীমার মধ্যে অ্যালার্ট। ব্যবস্থা নেওয়ার সময় বাকি।")

