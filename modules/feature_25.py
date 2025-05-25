# Feature 25.py implementation here

import streamlit as st

def app():
    st.header("🏅 নদী রেটিং সিস্টেম (A-F)")
    st.markdown("""
    নদীর স্বাস্থ্য ও নিরাপত্তা মূল্যায়ন করে একটি রেটিং (A থেকে F) প্রদান করুন।
    """)

    # নদীর বিভিন্ন মাপকাঠি ইনপুট
    water_quality = st.slider("পানির মান (Water Quality)", 0, 100, 70)
    pollution_level = st.slider("দূষণের মাত্রা (Pollution Level)", 0, 100, 30)
    encroachment_level = st.slider("অবৈধ দখলের মাত্রা (Encroachment Level)", 0, 100, 20)
    biodiversity = st.slider("জীববৈচিত্র্য (Biodiversity)", 0, 100, 60)
    flood_risk = st.slider("বন্যার ঝুঁকি (Flood Risk)", 0, 100, 40)

    # রেটিং হিসাবের জন্য একটি ফাংশন
    def calculate_rating():
        score = (water_quality * 0.3) + ((100 - pollution_level) * 0.25) + ((100 - encroachment_level) * 0.2) + (biodiversity * 0.15) + ((100 - flood_risk) * 0.1)
        if score >= 85:
            return 'A'
        elif score >= 70:
            return 'B'
        elif score >= 55:
            return 'C'
        elif score >= 40:
            return 'D'
        elif score >= 25:
            return 'E'
        else:
            return 'F'

    rating = calculate_rating()

    st.markdown(f"### নদীর মোট রেটিং: **{rating}**")
    st.info("""
    - A: উৎকৃষ্ট
    - B: ভালো
    - C: সন্তোষজনক
    - D: দরিদ্র
    - E: খুব দরিদ্র
    - F: বিপজ্জনক
    """)

