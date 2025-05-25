# Feature 16.py implementation here

import streamlit as st
import random

def app():
    st.header("🤖 মডেলের আত্মবিশ্বাস স্কোর")
    st.markdown("""
    এটি মডেলের পূর্বাভাসের আত্মবিশ্বাস স্তর প্রদর্শন করে। 
    উচ্চ স্কোর মানে মডেল পূর্বাভাসে বেশি নিশ্চিত।
    """)

    st.write("নিচে মডেলের কিছু উদাহরণ পূর্বাভাস এবং তাদের আত্মবিশ্বাস স্কোর দেখানো হয়েছে।")

    # ডেমো: মডেলের কিছু ফিচার এবং তাদের আত্মবিশ্বাস স্কোর (0-100%)
    predictions = [
        {"ফিচার": "অবৈধ দখল", "confidence": random.uniform(75, 99)},
        {"ফিচার": "নদীপ্রস্থ হ্রাস", "confidence": random.uniform(60, 95)},
        {"ফিচার": "নদীভাঙ্গন", "confidence": random.uniform(50, 90)},
        {"ফিচার": "দূষণ", "confidence": random.uniform(70, 98)},
        {"ফিচার": "ভাসমান বর্জ্য", "confidence": random.uniform(80, 99)},
    ]

    for pred in predictions:
        st.write(f"**{pred['ফিচার']}**: আত্মবিশ্বাস স্কোর: {pred['confidence']:.2f}%")
        st.progress(int(pred['confidence']))

    st.info("⚠️ বাস্তব প্রয়োগে, মডেলের বাস্তব confidence স্কোর ব্যবহার করুন।")

