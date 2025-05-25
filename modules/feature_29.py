# Feature 29.py implementation here

import streamlit as st
import pygame
import os

def app():
    st.header("🚨 এমার্জেন্সি অ্যালার্ট সাউন্ড")

    st.markdown("""
    জরুরি পরিস্থিতিতে দ্রুত সতর্কতা জানাতে এই ফিচারটি ব্যবহার করা হয়।
    একটি অ্যালার্ট সাউন্ড প্লে করা হবে যা পরিস্থিতি জানাবে।
    """)

    if 'pygame_initialized' not in st.session_state:
        pygame.mixer.init()
        st.session_state['pygame_initialized'] = True

    alert_sound_path = "modules/assets/alert_sound.mp3"  # আপনাকে এই ফাইলটি আপনার প্রোজেক্টে রাখতে হবে

    if st.button("অ্যালার্ট সাউন্ড চালু করুন"):
        if os.path.exists(alert_sound_path):
            pygame.mixer.music.load(alert_sound_path)
            pygame.mixer.music.play()
            st.success("সাউন্ড প্লে হচ্ছে...")
        else:
            st.error("সাউন্ড ফাইল পাওয়া যায়নি!")

    if st.button("অ্যালার্ট সাউন্ড বন্ধ করুন"):
        pygame.mixer.music.stop()
        st.info("সাউন্ড বন্ধ করা হয়েছে।")

