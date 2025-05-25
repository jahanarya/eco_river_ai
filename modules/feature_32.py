# Feature 32.py implementation here

import streamlit as st

def app():
    st.header("📴 অফলাইন মোড অ্যাপ")

    st.markdown("""
    এই ফিচারটি ব্যবহারকারীদের অফলাইনে কিছু গুরুত্বপূর্ণ তথ্য ও ডেটা অ্যাক্সেস করার সুযোগ দেয়।
    যখন ইন্টারনেট সংযোগ না থাকে, তখনও কিছু ফাংশনালিটি চালানো যাবে।
    """)

    st.info("দ্রুত ডেমো: অফলাইনে কিছু ডেটা সংরক্ষণ এবং দেখানোর ব্যবস্থা")

    # সিম্পল ডেটা ক্যাশিং ডেমো (Session state ব্যবহার)
    if 'offline_data' not in st.session_state:
        st.session_state['offline_data'] = []

    new_data = st.text_input("নতুন তথ্য সংরক্ষণ করুন")

    if st.button("তথ্য সংরক্ষণ করুন"):
        if new_data:
            st.session_state['offline_data'].append(new_data)
            st.success("তথ্য সংরক্ষণ করা হয়েছে!")
        else:
            st.error("তথ্য ফাঁকা হতে পারে না!")

    st.subheader("সংরক্ষিত তথ্যসমূহ (অফলাইন)")

    if st.session_state['offline_data']:
        for idx, item in enumerate(st.session_state['offline_data'], 1):
            st.write(f"{idx}. {item}")
    else:
        st.write("কোন তথ্য সংরক্ষিত নেই।")

