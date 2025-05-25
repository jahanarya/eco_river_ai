# Feature 17.py implementation here

import streamlit as st

def app():
    st.header("📝 জনগণের ফিডব্যাক সংযোজন")
    st.markdown("""
    ব্যবহারকারীরা নদী ও পরিবেশ সংক্রান্ত সমস্যাগুলো সম্পর্কে ফিডব্যাক প্রদান করতে পারবেন।
    """)

    with st.form("feedback_form"):
        name = st.text_input("আপনার নাম")
        email = st.text_input("আপনার ইমেইল (ঐচ্ছিক)")
        location = st.text_input("আপনার লোকেশন (অঞ্চল/গ্রাম/শহর)")
        feedback = st.text_area("আপনার ফিডব্যাক লিখুন")

        submitted = st.form_submit_button("ফিডব্যাক পাঠান")

        if submitted:
            if not feedback.strip():
                st.error("ফিডব্যাক অবশ্যই দিতে হবে।")
            else:
                # এখানে ফিডব্যাক ডাটাবেজ বা ফাইল সংরক্ষণ কোড হবে (ডেমোতে শুধু ধন্যবাদ বার্তা)
                st.success("আপনার ফিডব্যাকের জন্য ধন্যবাদ! আমরা আপনার বক্তব্য গুরুত্বসহকারে বিবেচনা করবো।")

                # ডেমো হিসেবে ফিডব্যাক প্রিন্ট করা হচ্ছে (প্রকৃত ব্যবহারে সংরক্ষণ করতে হবে)
                st.write("আপনার ফিডব্যাক ছিল:")
                st.write(f"- নাম: {name}")
                st.write(f"- ইমেইল: {email}")
                st.write(f"- লোকেশন: {location}")
                st.write(f"- মন্তব্য: {feedback}")

