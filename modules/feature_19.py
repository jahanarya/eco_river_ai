# Feature 19.py implementation here

import streamlit as st

def app():
    st.header("🚨 জরুরি লেভেল ট্যাগিং")
    st.markdown("""
    নদী বা পরিবেশের বিভিন্ন পরিস্থিতির জন্য জরুরি স্তর নির্ধারণ এবং ট্যাগিং করা হয়, যাতে দ্রুত সাড়া দেওয়া যায়।
    """)

    st.write("নিচে পরিস্থিতি বর্ণনা দিয়ে জরুরি লেভেল নির্ধারণ করুন:")

    situation = st.text_area("পরিস্থিতির বর্ণনা লিখুন")

    level = st.selectbox("জরুরি লেভেল নির্বাচন করুন", [
        "নিম্ন (Low)",
        "মধ্যম (Medium)",
        "উচ্চ (High)",
        "তাত্ক্ষণিক (Critical)"
    ])

    if st.button("লেভেল ট্যাগ করুন"):
        if not situation.strip():
            st.error("অনুগ্রহ করে পরিস্থিতির বর্ণনা দিন।")
        else:
            st.success(f"জরুরি লেভেল '{level}' সফলভাবে ট্যাগ করা হয়েছে!")
            st.write(f"পরিস্থিতি: {situation}")

