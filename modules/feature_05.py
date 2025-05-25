# Feature 05.py implementation here

import streamlit as st

def app():
    st.header("♻️ ভাসমান প্লাস্টিক/বর্জ্য শনাক্তকরণ")
    st.markdown("""
    এই ফিচারটির মাধ্যমে নদীতে ভাসমান প্লাস্টিক ও বর্জ্য শনাক্ত করা যাবে।

    📸 ছবি বা ভিডিও আপলোড করুন, তারপর AI মডেল তা বিশ্লেষণ করবে।
    """)

    uploaded_file = st.file_uploader("📤 নদীর ছবি বা ভিডিও আপলোড করুন", type=["jpg", "png", "mp4", "mov"])

    if uploaded_file:
        st.success("✅ ফাইল আপলোড সফল হয়েছে।")

        # ছবি হলে দেখানো
        if uploaded_file.type.startswith("image/"):
            st.image(uploaded_file, caption="আপলোডকৃত ছবি", use_column_width=True)
        
        # ভিডিও হলে প্লে বাটন দেখানো (Streamlit 1.10+)
        elif uploaded_file.type.startswith("video/"):
            st.video(uploaded_file)

        st.info("🚧 AI মডেল দ্বারা প্লাস্টিক/বর্জ্য শনাক্তকরণ চলছে (ডেমো)।")
        st.warning("⚠️ সম্ভাব্য প্লাস্টিক বর্জ্য অবস্থান: নদীর পূর্ব পার্শ্ব")

