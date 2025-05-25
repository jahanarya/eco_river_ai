# Feature 14.py implementation here

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def app():
    st.header("☔ বৃষ্টিপাত বিশ্লেষণ")
    st.markdown("""
    নদীর আশপাশের এলাকার বৃষ্টিপাতের পরিমাণ ও প্রবণতা বিশ্লেষণ।
    """)

    # ডেমো বৃষ্টিপাত ডেটা (মাসিক, মিলিমিটার)
    months = ['জানুয়ারি', 'ফেব্রুয়ারি', 'মার্চ', 'এপ্রিল', 'মে', 'জুন',
              'জুলাই', 'আগস্ট', 'সেপ্টেম্বর', 'অক্টোবর', 'নভেম্বর', 'ডিসেম্বর']

    rainfall_mm = [78, 60, 75, 95, 120, 150, 200, 250, 180, 100, 80, 70]

    df = pd.DataFrame({
        'মাস': months,
        'বৃষ্টিপাত (মিমি)': rainfall_mm
    })

    st.subheader("মাসিক বৃষ্টিপাত পরিমাণ")
    st.bar_chart(df.set_index('মাস'))

    # বৃষ্টিপাতের গড় ও সর্বোচ্চ
    avg_rainfall = np.mean(rainfall_mm)
    max_rainfall = np.max(rainfall_mm)
    max_month = months[rainfall_mm.index(max_rainfall)]

    st.write(f"গড় মাসিক বৃষ্টিপাত: **{avg_rainfall:.2f} মিমি**")
    st.write(f"সর্বোচ্চ বৃষ্টিপাত: **{max_rainfall} মিমি** (মাস: {max_month})")

    st.info("⚠️ প্রকৃত বিশ্লেষণের জন্য স্থানীয় বৃষ্টিপাত ডেটা ব্যবহার করুন।")

