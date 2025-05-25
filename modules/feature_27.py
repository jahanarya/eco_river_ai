# Feature 27.py implementation here

import streamlit as st
import random

def app():
    st.header("🌊 বন্যা ঝুঁকি বিশ্লেষণ")
    st.markdown("""
    এই মডিউল নদীর আশপাশের এলাকায় বন্যার সম্ভাব্য ঝুঁকি বিশ্লেষণ করে রিপোর্ট তৈরি করে।
    """)

    # কিছু ফিক্সড এলাকা উদাহরণ স্বরূপ
    areas = ["কুমিল্লা", "ঢাকা", "চট্টগ্রাম", "রাজশাহী", "বরিশাল"]
    selected_area = st.selectbox("এলাকা নির্বাচন করুন", areas)

    # বৃষ্টিপাত এবং নদীর পানি উচ্চতার ডামি ডেটা (ডেমো)
    rainfall = st.slider("বৃষ্টিপাতের পরিমাণ (মিমি)", 0, 500, 150)
    river_level = st.slider("নদীর পানি উচ্চতা (মিটার)", 0.0, 20.0, 5.0)

    # ঝুঁকি মূল্যায়ন
    def calculate_flood_risk(rainfall, river_level):
        score = rainfall * 0.6 + river_level * 20
        if score > 200:
            return "উচ্চ ঝুঁকি"
        elif score > 100:
            return "মধ্যম ঝুঁকি"
        else:
            return "কম ঝুঁকি"

    risk = calculate_flood_risk(rainfall, river_level)

    st.subheader(f"{selected_area} এলাকার বন্যা ঝুঁকি: {risk}")

    # ঝুঁকি অনুযায়ী পরামর্শ
    if risk == "উচ্চ ঝুঁকি":
        st.error("সতর্কতা! বন্যার সম্ভাবনা বেশি। প্রস্তুতি নিন।")
    elif risk == "মধ্যম ঝুঁকি":
        st.warning("মধ্যম ঝুঁকি। মনোযোগ দিন।")
    else:
        st.success("ঝুঁকি কম। নিরাপদ।")


