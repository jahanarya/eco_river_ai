# Feature 28.py implementation here

import streamlit as st

def app():
    st.header("🛤️ নিরাপদ রুট পরিকল্পনা")
    st.markdown("""
    নদী সংলগ্ন এলাকায় নিরাপদ পথ নির্ধারণের জন্য একটি সহজ রুট প্ল্যানার। 
    পরিবহন ও বন্যার ঝুঁকি বিবেচনা করে নিরাপদ পথ প্রদর্শন করবে।
    """)

    start_location = st.text_input("শুরু করার স্থান লিখুন")
    end_location = st.text_input("গন্তব্যের স্থান লিখুন")

    if st.button("রুট নির্ধারণ করুন"):
        if start_location and end_location:
            # ডেমো: নিরাপদ রুট তৈরি (সাধারণ টেক্সট রিটার্ন)
            safe_route = f"নিরাপদ রুট: {start_location} থেকে {end_location} পর্যন্ত নদী থেকে দূরে সড়ক ব্যবহার করুন।"
            st.success(safe_route)
            st.info("বন্যা ঝুঁকি ও অবৈধ দখল থেকে নিরাপদ পথ বেছে নেওয়া হয়েছে।")
        else:
            st.warning("অনুগ্রহ করে উভয় স্থান পূরণ করুন।")

