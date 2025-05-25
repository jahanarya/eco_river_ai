# Feature 34.py implementation here

import streamlit as st
import folium
from streamlit_folium import st_folium

def app():
    st.header("📡 জিও-ফেন্সিং অ্যালার্ট")

    st.markdown("""
    নদীর সংরক্ষিত এলাকা (জিও-ফেন্স) বাইরে কোন অননুমোদিত কার্যকলাপ সনাক্ত হলে অ্যালার্ট প্রদান করবে।
    """)

    # ডেমো জন্য একটি সেন্টার পয়েন্ট এবং রেডিয়াস
    center = [23.8103, 90.4125]  # ঢাকা শহরের কোঅর্ডিনেট
    radius = 5000  # মিটার

    m = folium.Map(location=center, zoom_start=12)

    # জিও-ফেন্স এলাকা (সার্কেল)
    folium.Circle(
        location=center,
        radius=radius,
        color='blue',
        fill=True,
        fill_opacity=0.1,
        popup="নিরাপদ নদী এলাকা"
    ).add_to(m)

    # ব্যবহারকারীর লোকেশন সিমুলেশন (ডেমোতে ফিক্সড পয়েন্ট)
    user_location = [23.8150, 90.4200]

    folium.Marker(
        location=user_location,
        popup="ব্যবহারকারীর অবস্থান",
        icon=folium.Icon(color='red')
    ).add_to(m)

    st_folium(m, width=700, height=500)

    # জিও-ফেন্সিং চেক (ডেমো লজিক)
    from geopy.distance import geodesic

    distance = geodesic(center, user_location).meters

    st.write(f"ব্যবহারকারীর নদী থেকে দূরত্ব: {distance:.2f} মিটার")

    if distance > radius:
        st.error("⚠️ সতর্কতা: ব্যবহারকারী নিরাপদ এলাকা থেকে বাইরে!")
    else:
        st.success("✅ ব্যবহারকারী নিরাপদ জিও-ফেন্সিং এর মধ্যে আছে।")
