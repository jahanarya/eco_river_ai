# Feature 13.py implementation here

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.header("🔥 দখলের হিটম্যাপ")
    st.markdown("""
    নদীর বিভিন্ন অংশে অবৈধ দখলের ঘনত্ব (Heatmap) প্রদর্শন করে।
    """)

    # উদাহরণ ডেটা তৈরি: নদীর ১০০ x ১০০ ইউনিট এর মধ্যে দখলের পয়েন্ট সমূহ
    np.random.seed(42)
    encroachment_points_x = np.random.randint(0, 100, 200)  # ২০০ পয়েন্টের এক্স কোঅর্ডিনেট
    encroachment_points_y = np.random.randint(0, 100, 200)  # ২০০ পয়েন্টের ওয়াই কোঅর্ডিনেট

    data = pd.DataFrame({
        'x': encroachment_points_x,
        'y': encroachment_points_y
    })

    st.subheader("অবৈধ দখলের পয়েন্টসমূহ")
    st.map(data.rename(columns={'x': 'lat', 'y': 'lon'}))  # সাধারণত lat-lon দরকার, এখানে ডেমো

    # Heatmap জন্য 2D হিস্টোগ্রাম
    heatmap_data, xedges, yedges = np.histogram2d(data['x'], data['y'], bins=30, range=[[0,100],[0,100]])
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    fig, ax = plt.subplots(figsize=(7,6))
    sns.heatmap(heatmap_data.T, cmap="Reds", cbar=True, ax=ax)
    ax.set_title("নদীতে অবৈধ দখলের হিটম্যাপ")
    ax.set_xlabel("X কোঅর্ডিনেট")
    ax.set_ylabel("Y কোঅর্ডিনেট")

    st.pyplot(fig)

