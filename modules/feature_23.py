import streamlit as st
from typing import Dict, Any

def generate_eviction_notice(occupation_info: Dict[str, Any], template: str = None) -> str:
    """
    Create a smart eviction notice based on occupation info.
    Args:
        occupation_info: Dict with details on illegal occupation
        template: Optional string template for notice; use placeholders like {name}, {location}
    Returns:
        Formatted eviction notice string
    """
    if not template:
        template = ("Notice: {name}, you are illegally occupying river land at {location}. "
                    "You are required to vacate the premises within 7 days or face legal action.")
    return template.format(
        name=occupation_info.get("occupant_name", "Unknown"),
        location=occupation_info.get("location", "Unknown Location")
    )

def feature_23_func():
    st.header("📄 স্মার্ট উচ্ছেদ নোটিশ তৈরি")
    st.markdown(
        "এই ফিচারে আপনি সহজেই উচ্ছেদ নোটিশ তৈরি করতে পারবেন, যা নদী দখলদারদের জন্য প্রেরণ করা হবে।"
    )

    name = st.text_input("দখলদারের নাম")
    location = st.text_input("অবৈধ দখলের স্থান")
    notice_date = st.date_input("নোটিশের তারিখ")
    deadline_date = st.date_input("উচ্ছেদের জন্য শেষ তারিখ")
    reason = st.text_area("উচ্ছেদ নোটিশের কারণ")

    if st.button("নোটিশ তৈরি করুন"):
        if not (name and location and reason):
            st.error("অনুগ্রহ করে সকল প্রয়োজনীয় তথ্য পূরণ করুন।")
        else:
            notice_info = {
                "occupant_name": name,
                "location": location,
                "notice_date": str(notice_date),
                "deadline_date": str(deadline_date),
                "reason": reason,
            }
            notice_text = generate_eviction_notice(notice_info)
            st.success("নোটিশ সফলভাবে তৈরি হয়েছে!")
            st.code(notice_text, language="markdown")
    return "Feature 23 executed!"
