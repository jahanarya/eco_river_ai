

import streamlit as st
from modules import (
    feature_01, feature_02, feature_03, feature_04, feature_05, feature_06, feature_07, feature_08, feature_09, feature_10,
    feature_11, feature_12, feature_13, feature_14, feature_15, feature_16, feature_17, feature_18, feature_19, feature_20,
    feature_21, feature_22, feature_23, feature_24, feature_25, feature_26, feature_27, feature_28, feature_29, feature_30,
    feature_31, feature_32, feature_33, feature_34, feature_35
)

# Page config
st.set_page_config(page_title="Eco River AI", layout="wide", page_icon="🌊")

# Custom CSS Styles
st.markdown(
    """
    <style>
    .main-header {
        font-size: 40px;
        font-weight: bold;
        color: #0077b6;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 18px;
        color: #023e8a;
        text-align: center;
        margin-top: 0;
        margin-bottom: 30px;
        font-style: italic;
    }
    .feature-box {
        background-color: #caf0f8;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #90e0ef;
        margin-bottom: 20px;
        font-size: 18px;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0077b6;
        color: white;
        text-align: center;
        padding: 10px 0;
        font-size: 14px;
        z-index: 999;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown('<h1 class="main-header">Eco River AI - নদী নিরাপত্তা ও পরিবেশ পর্যবেক্ষণ</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">"Saving Every Drop, Protecting Every River"</p>', unsafe_allow_html=True)

# Feature list
feature_list = [
    "1. অবৈধ দখল শনাক্তকরণ",
    "2. নদীর গতিপথ বিশ্লেষণ",
    "3. AI দ্বারা জমি শ্রেণি সনাক্তকরণ",
    "4. পানি দূষণ বিশ্লেষণ",
    "5. উপগ্রহ চিত্র কালেকশন",
    "6. রিয়েল-টাইম রিপোর্ট তৈরি",
    "7. জলবায়ু প্রভাব বিশ্লেষণ",
    "8. নদী প্রবাহ মডেলিং",
    "9. রিভার-ম্যাপ জেনারেশন",
    "10. AI মডেল ভিত্তিক দখল শনাক্তকরণ",
    "11. ম্যানুয়াল মডেল আপলোড",
    "12. ML কনফিডেন্স স্কোরিং",
    "13. চিত্র থেকে জিও-কোর্ডিনেট বের করা",
    "14. রিভার বাউন্ডারি ওভারলে",
    "15. রিপোর্ট PDF ডাউনলোড",
    "16. প্রতিক্রিয়া ফর্ম",
    "17. পূর্ববর্তী রেকর্ড বিশ্লেষণ",
    "18. ডেটা টাইমলাইন চার্ট",
    "19. নদী দখল heatmap",
    "20. ইমেজ হাইলাইট মোড",
    "21. স্যাটেলাইট ক্যামেরা লাইভ ফিড (ডেমো)",
    "22. জরুরী সতর্কতা বাটন",
    "23. সেন্সর ডেটা ইন্টিগ্রেশন",
    "24. সরকারী তথ্য সংযুক্তি",
    "25. ব্যবহারকারী রিপোর্ট জমা",
    "26. স্বয়ংক্রিয় সতর্ক বার্তা",
    "27. বহুভাষিক ইন্টারফেস",
    "28. অডিও সতর্কতা সিস্টেম",
    "29. জিও-ফেন্স এলার্ম",
    "30. মডেল পারফরম্যান্স এনালাইসিস",
    "31. ইন-অ্যাপ নির্দেশনা (Guided walkthrough)",
    "32. রিভার সেভার র‍্যাঙ্কিং সিস্টেম",
    "33. অফলাইন মোডে ব্যবহারের অপশন",
    "34. এনক্রিপটেড রিপোর্টিং চ্যানেল",
    "35. ওপেন ডেটা এপিআই এক্সপোর্ট"
]

# Sidebar
choice = st.sidebar.selectbox("ফিচার নির্বাচন করুন", feature_list, index=0)

# Selected feature banner
st.markdown(f'<div class="feature-box"><strong>নির্বাচিত ফিচার:</strong> {choice}</div>', unsafe_allow_html=True)

st.info("এই ফিচারটি বর্তমানে ডেমো সংস্করণে প্রদর্শিত হচ্ছে।")

# Load feature with spinner
with st.spinner(f"{choice} লোড হচ্ছে... অনুগ্রহ করে অপেক্ষা করুন"):
    if choice == "1. অবৈধ দখল শনাক্তকরণ":
        feature_01.app()
    elif choice == "2. নদীর গতিপথ বিশ্লেষণ":
        feature_02.app()
    elif choice == "3. AI দ্বারা জমি শ্রেণি সনাক্তকরণ":
        feature_03.app()
    elif choice == "4. পানি দূষণ বিশ্লেষণ":
        feature_04.app()
    elif choice == "5. উপগ্রহ চিত্র কালেকশন":
        feature_05.app()
    elif choice == "6. রিয়েল-টাইম রিপোর্ট তৈরি":
        feature_06.app()
    elif choice == "7. জলবায়ু প্রভাব বিশ্লেষণ":
        feature_07.app()
    elif choice == "8. নদী প্রবাহ মডেলিং":
        feature_08.app()
    elif choice == "9. রিভার-ম্যাপ জেনারেশন":
        feature_09.app()
    elif choice == "10. AI মডেল ভিত্তিক দখল শনাক্তকরণ":
        feature_10.app()
    elif choice == "11. ম্যানুয়াল মডেল আপলোড":
        feature_11.app()
    elif choice == "12. ML কনফিডেন্স স্কোরিং":
        feature_12.app()
    elif choice == "13. চিত্র থেকে জিও-কোর্ডিনেট বের করা":
        feature_13.app()
    elif choice == "14. রিভার বাউন্ডারি ওভারলে":
        feature_14.app()
    elif choice == "15. রিপোর্ট PDF ডাউনলোড":
        feature_15.app()
    elif choice == "16. প্রতিক্রিয়া ফর্ম":
        feature_16.app()
    elif choice == "17. পূর্ববর্তী রেকর্ড বিশ্লেষণ":
        feature_17.app()
    elif choice == "18. ডেটা টাইমলাইন চার্ট":
        feature_18.app()
    elif choice == "19. নদী দখল heatmap":
        feature_19.app()
    elif choice == "20. ইমেজ হাইলাইট মোড":
        feature_20.app()
    elif choice == "21. স্যাটেলাইট ক্যামেরা লাইভ ফিড (ডেমো)":
        feature_21.app()
    elif choice == "22. জরুরী সতর্কতা বাটন":
        feature_22.app()
    elif choice == "23. সেন্সর ডেটা ইন্টিগ্রেশন":
        feature_23.app()
    elif choice == "24. সরকারী তথ্য সংযুক্তি":
        feature_24.app()
    elif choice == "25. ব্যবহারকারী রিপোর্ট জমা":
        feature_25.app()
    elif choice == "26. স্বয়ংক্রিয় সতর্ক বার্তা":
        feature_26.app()
    elif choice == "27. বহুভাষিক ইন্টারফেস":
        feature_27.app()
    elif choice == "28. অডিও সতর্কতা সিস্টেম":
        feature_28.app()
    elif choice == "29. জিও-ফেন্স এলার্ম":
        feature_29.app()
    elif choice == "30. মডেল পারফরম্যান্স এনালাইসিস":
        feature_30.app()
    elif choice == "31. ইন-অ্যাপ নির্দেশনা (Guided walkthrough)":
        feature_31.app()
    elif choice == "32. রিভার সেভার র‍্যাঙ্কিং সিস্টেম":
        feature_32.app()
    elif choice == "33. অফলাইন মোডে ব্যবহারের অপশন":
        feature_33.app()
    elif choice == "34. এনক্রিপটেড রিপোর্টিং চ্যানেল":
        feature_34.app()
    elif choice == "35. ওপেন ডেটা এপিআই এক্সপোর্ট":
        feature_35.app()

# Footer
st.markdown(
    """
    <div class="footer">
        © 2025 Eco River AI | Developed by Mimtaj, Tasfia Aminul Mimi & Tanvir Ahmed Khan
    </div>
    """,
    unsafe_allow_html=True
)

   


  
