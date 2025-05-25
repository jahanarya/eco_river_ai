# Feature 11.py implementation here

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def app():
    st.header("📊 বার্ষিক নদী স্বাস্থ্যের তুলনা")
    st.markdown("""
    নদীর স্বাস্থ্যের বিভিন্ন সূচক যেমন পানির গুণগত মান, দূষণ, প্রবাহ ইত্যাদির বার্ষিক পরিবর্তন বিশ্লেষণ করা হবে।
    """)

    # ডেমো ডেটা তৈরি (বার্ষিক তথ্য)
    years = [2019, 2020, 2021, 2022, 2023]
    water_quality_index = [65, 70, 68, 75, 80]  # 0-100 scale
    pollution_level = [40, 38, 35, 30, 25]      # কম হলে ভালো
    flow_rate = [500, 520, 480, 530, 550]       # কিউবিক মিটার/সেকেন্ড

    df = pd.DataFrame({
        "Year": years,
        "Water Quality Index": water_quality_index,
        "Pollution Level": pollution_level,
        "Flow Rate (m³/s)": flow_rate
    })

    st.subheader("বার্ষিক নদী স্বাস্থ্য সূচকসমূহ")
    st.dataframe(df)

    # প্লট তৈরি
    fig, ax1 = plt.subplots(figsize=(8, 4))

    ax1.plot(df["Year"], df["Water Quality Index"], color='green', marker='o', label="Water Quality Index")
    ax1.set_ylabel('Water Quality Index', color='green')
    ax1.tick_params(axis='y', labelcolor='green')
    ax1.set_ylim(0, 100)

    ax2 = ax1.twinx()
    ax2.plot(df["Year"], df["Pollution Level"], color='red', marker='x', label="Pollution Level")
    ax2.set_ylabel('Pollution Level', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    ax2.set_ylim(0, 100)

    plt.title("বার্ষিক নদী স্বাস্থ্য সূচকের তুলনা")
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    st.pyplot(fig)

    st.write("**Flow Rate:**", ", ".join([f"{v} m³/s" for v in flow_rate]))

    st.info("⚠️ বাস্তব প্রয়োগে সঠিক পরিমাপের ডেটা প্রয়োজন।")

