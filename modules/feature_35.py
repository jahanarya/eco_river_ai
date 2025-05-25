# Feature 35.py implementation here

import streamlit as st
import pandas as pd
import json

def app():
    st.header("🌐 ওপেন ডেটা এপিআই এক্সপোর্ট")

    st.markdown("""
    নদী ও পরিবেশ সংক্রান্ত তথ্যগুলোকে ওপেন ডেটা ফরম্যাটে (CSV, JSON) এক্সপোর্ট করে প্রদান করবে,
    যাতে অন্য অ্যাপ্লিকেশন বা প্ল্যাটফর্মে সহজে ব্যবহার করা যায়।
    """)

    # ডেমো ডেটাসেট (নদীর কিছু তথ্য)
    data = {
        "নদী": ["মেঘনা", "তিতাস", "পদ্মা", "যমুনা"],
        "দৈর্ঘ্য (কিমি)": [120, 98, 240, 150],
        "প্রবাহের হার (কিউবিক মিটার/সেকেন্ড)": [5000, 3200, 7000, 4500],
        "দূষণ মাত্রা": ["মাঝারি", "নিম্ন", "উচ্চ", "মাঝারি"],
    }

    df = pd.DataFrame(data)

    st.subheader("নদীর ডেটাসেট")

    st.dataframe(df)

    st.markdown("**এক্সপোর্ট ফরম্যাট নির্বাচন করুন:**")
    export_format = st.selectbox("", ["CSV", "JSON"])

    if st.button("ডাউনলোড প্রস্তুত করুন"):
        if export_format == "CSV":
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="CSV ডাউনলোড করুন",
                data=csv,
                file_name="river_data.csv",
                mime='text/csv',
            )
        else:
            json_str = df.to_json(orient='records', force_ascii=False)
            st.download_button(
                label="JSON ডাউনলোড করুন",
                data=json_str,
                file_name="river_data.json",
                mime='application/json',
            )


