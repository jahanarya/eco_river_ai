# Feature 21.py implementation here

import streamlit as st

def app():
    st.header("🎯 প্রাসঙ্গিকতা ভিত্তিক অগ্রাধিকার নির্ধারণ")
    st.markdown("""
    এই ফিচারে আমরা বিভিন্ন রিপোর্ট বা সমস্যার গুরুত্ব বা অগ্রাধিকার নির্ধারণ করব, যাতে প্রাসঙ্গিক সমস্যাগুলো আগে সমাধান হয়।
    """)

    # উদাহরণ: কিছু সমস্যা ও তাদের প্রাসঙ্গিকতা স্কোর
    problems = {
        "অবৈধ দখল": 8,
        "নদীপ্রস্থ হ্রাস": 7,
        "দূষণ": 9,
        "ভাসমান বর্জ্য": 5,
        "বন্যা ঝুঁকি": 10,
    }

    st.write("নিচে সমস্যাগুলোর প্রাসঙ্গিকতা স্কোর দেওয়া হলো (১০ হলো সর্বোচ্চ):")

    for problem, score in problems.items():
        st.write(f"- {problem}: {score}")

    # ব্যবহারকারীর কাছে নতুন সমস্যা এবং স্কোর নেওয়া
    st.subheader("নতুন সমস্যা যুক্ত করুন এবং অগ্রাধিকার দিন")

    new_problem = st.text_input("সমস্যার নাম")
    new_score = st.slider("অগ্রাধিকার (১ থেকে ১০)", min_value=1, max_value=10, value=5)

    if st.button("অগ্রাধিকার যোগ করুন"):
        if new_problem.strip() == "":
            st.error("অনুগ্রহ করে সমস্যার নাম লিখুন।")
        else:
            problems[new_problem] = new_score
            st.success(f"সমস্যা '{new_problem}' সফলভাবে অগ্রাধিকার সহ যোগ করা হয়েছে।")
            st.write("আপডেটেড সমস্যা তালিকা:")
            for problem, score in problems.items():
                st.write(f"- {problem}: {score}")
