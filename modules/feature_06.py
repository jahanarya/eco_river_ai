import streamlit as st
import folium
from streamlit_folium import st_folium

def app():
    st.header("🗺️ লাইভ এআই ম্যাপ")
    st.markdown("""
    এই ফিচারটি ব্যবহার করে নদীর বিভিন্ন সমস্যা যেমন অবৈধ দখল, দূষণ, বর্জ্য স্থানের **লাইভ ম্যাপ** দেখতে পারবেন।
    
    🛰️ ডেটা রিয়েল-টাইম আপডেট হবে এবং ভিজ্যুয়াল ম্যাপে প্রদর্শিত হবে।
    """)

    # সিম্পল লোকেশন ডেটা (ডেমো)
    locations = [
        {"name": "অবৈধ দখল", "lat": 23.8103, "lon": 90.4125},
        {"name": "দূষণ উৎস", "lat": 23.8203, "lon": 90.4225},
        {"name": "ভাসমান বর্জ্য", "lat": 23.8000, "lon": 90.4325},
    ]

    m = folium.Map(location=[23.8103, 90.4125], zoom_start=12)

    for loc in locations:
        folium.Marker(
            location=[loc["lat"], loc["lon"]],
            popup=loc["name"],
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)

    # শুধু মেপটুকু রেন্ডার করো, আর কোন ফাংশন পাস করো নি
    st_folium(m, width=700, height=500)
