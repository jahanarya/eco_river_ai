# Feature 23.py implementation here

import streamlit as st

def app():
    st.header("📄 স্মার্ট উচ্ছেদ নোটিশ তৈরি")
    st.markdown("""
    এই ফিচারে আপনি সহজেই উচ্ছেদ নোটিশ তৈরি করতে পারবেন, যা নদী দখলদারদের জন্য প্রেরণ করা হবে।
    """)

    # ব্যবহারকারীর ইনপুট নেওয়া
    name = st.text_input("দখলদারের নাম")
    location = st.text_input("অবৈধ দখলের স্থান")
    notice_date = st.date_input("নোটিশের তারিখ")
    deadline_date = st.date_input("উচ্ছেদের জন্য শেষ তারিখ")

    reason = st.text_area("উচ্ছেদ নোটিশের কারণ")

    if st.button("নোটিশ তৈরি করুন"):
        if not (name and location and reason):
            st.error("অনুগ্রহ করে সকল প্রয়োজনীয় তথ্য পূরণ করুন।")
        else:
            notice_text = f"""
            স্মার্ট উচ্ছেদ নোটিশ

            তারিখ: {notice_date.strftime('%Y-%m-%d')}

            প্রাপক: {name}

            বিষয়: {location} এলাকায় অবৈধ দখল সম্পর্কে উচ্ছেদ নোটিশ।

            সম্মানিত {name},

            আপনাকে জানানো যাচ্ছে যে, {location} এলাকায় আপনার অবৈধ দখল শনাক্ত করা হয়েছে। 
            নিম্নোক্ত কারণে, আপনাকে {deadline_date.strftime('%Y-%m-%d')} এর মধ্যে উচ্ছেদ কার্যক্রম সম্পন্ন করতে অনুরোধ করা হলো:

            কারণ: {reason}

            যদি নির্ধারিত সময়ের মধ্যে উচ্ছেদ না করা হয়, তবে আইনানুগ ব্যবস্থা নেওয়া হবে।

            ধন্যবাদান্তে,
            নদী সুরক্ষা কর্তৃপক্ষ
            """
            st.success("উচ্ছেদ নোটিশ সফলভাবে তৈরি হয়েছে!")
            st.code(notice_text)

