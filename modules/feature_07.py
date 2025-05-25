# Feature 07.py implementation here

import streamlit as st
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(image):
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            exif_data[decoded] = value
    return exif_data

def get_gps_info(exif_data):
    gps_info = {}
    if "GPSInfo" in exif_data:
        for key in exif_data["GPSInfo"].keys():
            decode = GPSTAGS.get(key, key)
            gps_info[decode] = exif_data["GPSInfo"][key]
    return gps_info

def convert_to_degress(value):
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)

    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)

def get_coordinates(gps_info):
    lat = None
    lon = None

    if ("GPSLatitude" in gps_info) and ("GPSLatitudeRef" in gps_info) and \
       ("GPSLongitude" in gps_info) and ("GPSLongitudeRef" in gps_info):
        lat = convert_to_degress(gps_info["GPSLatitude"])
        if gps_info["GPSLatitudeRef"] != "N":
            lat = -lat

        lon = convert_to_degress(gps_info["GPSLongitude"])
        if gps_info["GPSLongitudeRef"] != "E":
            lon = -lon
    return lat, lon

def app():
    st.header("📍 জিপিএস লোকেশন এক্সট্রাকশন")
    st.markdown("""
    **আপনার ছবির EXIF ডেটা থেকে GPS লোকেশন এক্সট্রাক্ট করুন।**

    - ছবি আপলোড করুন যা GPS ডাটা ধারণ করে।
    - সিস্টেম ছবির অবস্থান (ল্যাটিচিউড ও লংগিচিউড) দেখাবে।
    """)

    uploaded_file = st.file_uploader("📤 GPS-সহ ছবি আপলোড করুন", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="আপলোডকৃত ছবি", use_column_width=True)

        exif_data = get_exif_data(image)
        gps_info = get_gps_info(exif_data)

        if gps_info:
            lat, lon = get_coordinates(gps_info)
            if lat and lon:
                st.success(f"GPS অবস্থান পাওয়া গেছে: \n\nLatitude: {lat:.6f}, Longitude: {lon:.6f}")
                st.map(data={"lat": [lat], "lon": [lon]})
            else:
                st.error("GPS ডেটা পাওয়া গেল না।")
        else:
            st.error("EXIF ডেটাতে GPS তথ্য নেই।")

