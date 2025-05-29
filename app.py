import streamlit as st
from modules import (
    feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10,
    feature11, feature12, feature13, feature14, feature15, feature16, feature17, feature18, feature19, feature20,
    feature21, feature22, feature23, feature24, feature25, feature26, feature27, feature28, feature29, feature30,
    feature31, feature32, feature33, feature34, feature35
)

st.set_page_config(page_title="Eco River AI", layout="wide")

st.sidebar.title("Eco River AI Features")

feature_list = [
    "1. অবৈধ দখল শনাক্তকরণ",
    "2. নদীর প্রস্থ কমে যাওয়া পর্যবেক্ষণ",
    "3. নদীভাঙ্গন পূর্বাভাস",
    "4. দূষণের উৎস শনাক্তকরণ",
    "5. ভাসমান প্লাস্টিক/বর্জ্য শনাক্তকরণ",
    "6. লাইভ এআই ম্যাপ",
    "7. জিপিএস লোকেশন এক্সট্রাকশন",
    "8. নদী এলাকা শ্রেণিবিভাগ",
    "9. ক্যাচমেন্ট এরিয়া বিশ্লেষণ",
    "10. পিডিএফ প্রতিবেদন তৈরি",
    "11. বার্ষিক নদী স্বাস্থ্যের তুলনা",
    "12. পানিপ্রবাহ সিমুলেশন",
    "13. দখলের হিটম্যাপ",
    "14. বৃষ্টিপাত বিশ্লেষণ",
    "15. স্থানীয় ছবি দিয়ে এআই পুনঃপ্রশিক্ষণ",
    "16. মডেলের আত্মবিশ্বাস স্কোর",
    "17. জনগণের ফিডব্যাক সংযোজন",
    "18. ভুল রিপোর্ট চিহ্নিতকরণ",
    "19. জরুরি লেভেল ট্যাগিং",
    "20. দৃশ্যমানতা সেটিংস",
    "21. প্রাসঙ্গিকতা ভিত্তিক অগ্রাধিকার",
    "22. নির্ধারিত সময়ে ব্যবস্থা না নিলে অ্যালার্ট বৃদ্ধি",
    "23. স্মার্ট উচ্ছেদ নোটিশ তৈরি",
    "24. আইনগত ট্র্যাকিং সিস্টেম",
    "25. নদী রেটিং সিস্টেম (A-F)",
    "26. প্রশাসনিক কন্ট্রোল প্যানেল",
    "27. বন্যা ঝুঁকি বিশ্লেষণ",
    "28. নিরাপদ রুট পরিকল্পনা",
    "29. এমার্জেন্সি অ্যালার্ট সাউন্ড",
    "30. জনগণের রিপোর্ট সিস্টেম",
    "31. শিক্ষামূলক ইন্টারঅ্যাকটিভ মডিউল",
    "32. অফলাইন মোড অ্যাপ",
    "33. হুমকির গোয়েন্দা প্রতিবেদন",
    "34. জিও-ফেন্সিং অ্যালার্ট",
    "35. ওপেন ডেটা এপিআই এক্সপোর্ট"
]

choice = st.sidebar.selectbox("ফিচার নির্বাচন করুন", feature_list)

st.title("Eco River AI - নদী নিরাপত্তা ও পরিবেশ পর্যবেক্ষণ")

st.write("নির্বাচিত ফিচার:", choice)
st.info("ডেমো সংস্করণ")

# ফিচার অনুযায়ী মডিউল কল
if choice == "1. অবৈধ দখল শনাক্তকরণ":
    feature1.app()
elif choice == "2. নদীর প্রস্থ কমে যাওয়া পর্যবেক্ষণ":
    feature2.app()
elif choice == "3. নদীভাঙ্গন পূর্বাভাস":
    feature3.app()
elif choice == "4. দূষণের উৎস শনাক্তকরণ":
    feature4.app()
elif choice == "5. ভাসমান প্লাস্টিক/বর্জ্য শনাক্তকরণ":
    feature5.app()
elif choice == "6. লাইভ এআই ম্যাপ":
    feature6.app()
elif choice == "7. জিপিএস লোকেশন এক্সট্রাকশন":
    feature7.app()
elif choice == "8. নদী এলাকা শ্রেণিবিভাগ":
    feature8.app()
elif choice == "9. ক্যাচমেন্ট এরিয়া বিশ্লেষণ":
    feature9.app()
elif choice == "10. পিডিএফ প্রতিবেদন তৈরি":
    feature10.app()
elif choice == "11. বার্ষিক নদী স্বাস্থ্যের তুলনা":
    feature11.app()
elif choice == "12. পানিপ্রবাহ সিমুলেশন":
    feature12.app()
elif choice == "13. দখলের হিটম্যাপ":
    feature13.app()
elif choice == "14. বৃষ্টিপাত বিশ্লেষণ":
    feature14.app()
elif choice == "15. স্থানীয় ছবি দিয়ে এআই পুনঃপ্রশিক্ষণ":
    feature15.app()
elif choice == "16. মডেলের আত্মবিশ্বাস স্কোর":
    feature16.app()
elif choice == "17. জনগণের ফিডব্যাক সংযোজন":
    feature17.app()
elif choice == "18. ভুল রিপোর্ট চিহ্নিতকরণ":
    feature18.app()
elif choice == "19. জরুরি লেভেল ট্যাগিং":
    feature19.app()
elif choice == "20. দৃশ্যমানতা সেটিংস":
    feature20.app()
elif choice == "21. প্রাসঙ্গিকতা ভিত্তিক অগ্রাধিকার":
    feature21.app()
elif choice == "22. নির্ধারিত সময়ে ব্যবস্থা না নিলে অ্যালার্ট বৃদ্ধি":
    feature22.app()
elif choice == "23. স্মার্ট উচ্ছেদ নোটিশ তৈরি":
    feature23.app()
elif choice == "24. আইনগত ট্র্যাকিং সিস্টেম":
    feature24.app()
elif choice == "25. নদী রেটিং সিস্টেম (A-F)":
    feature25.app()
elif choice == "26. প্রশাসনিক কন্ট্রোল প্যানেল":
    feature26.app()
elif choice == "27. বন্যা ঝুঁকি বিশ্লেষণ":
    feature27.app()
elif choice == "28. নিরাপদ রুট পরিকল্পনা":
    feature28.app()
elif choice == "29. এমার্জেন্সি অ্যালার্ট সাউন্ড":
    feature29.app()
elif choice == "30. জনগণের রিপোর্ট সিস্টেম":
    feature30.app()
elif choice == "31. শিক্ষামূলক ইন্টারঅ্যাকটিভ মডিউল":
    feature31.app()
elif choice == "32. অফলাইন মোড অ্যাপ":
    feature32.app()
elif choice == "33. হুমকির গোয়েন্দা প্রতিবেদন":
    feature33.app()
elif choice == "34. জিও-ফেন্সিং অ্যালার্ট":
    feature34.app()
elif choice == "35. ওপেন ডেটা এপিআই এক্সপোর্ট":
    feature35.app()
else:
    st.warning("অনুগ্রহ করে সাইডবার থেকে একটি বৈধ ফিচার নির্বাচন করুন।")


    
        
