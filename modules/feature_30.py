# Feature 30.py implementation here
import streamlit as st

def app():
    st.header("📢 জনগণের রিপোর্ট সিস্টেম")
    st.markdown("""
    জনগণ নদীর অবস্থা, দূষণ, দখল বা অন্য যেকোনো সমস্যা রিপোর্ট করতে পারবেন এখানে।
    রিপোর্ট জমা হলে তা অ্যাডমিন প্যানেলে পর্যালোচনা করা যাবে।
    """)

    with st.form("report_form"):
        name = st.text_input("আপনার নাম")
        location = st.text_input("প্রতিবেদনের স্থান")
        issue_type = st.selectbox("সমস্যার ধরন", [
            "অবৈধ দখল",
            "দূষণ",
            "ভাসমান বর্জ্য",
            "নদী ভাঙ্গন",
            "অন্যান্য"
        ])
        description = st.text_area("বিস্তারিত বিবরণ")

        submitted = st.form_submit_button("রিপোর্ট জমা দিন")
        if submitted:
            if not name or not location or not description:
                st.error("সকল প্রয়োজনীয় তথ্য পূরণ করুন।")
            else:
                # ডেমো হিসেবে শুধু সফলতা দেখানো হচ্ছে
                st.success("আপনার রিপোর্ট সফলভাবে জমা হয়েছে। ধন্যবাদ!")
                # এখানে রিপোর্ট ডাটাবেজে সংরক্ষণ কোড যোগ করা যাবে

