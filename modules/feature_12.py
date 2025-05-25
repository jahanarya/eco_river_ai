# Feature 12.py implementation here

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def app():
    st.header("💧 পানিপ্রবাহ সিমুলেশন")
    st.markdown("""
    নদীর পানিপ্রবাহ সিমুলেট করে পানির গতি, প্রবাহ হার, ও অন্যান্য ফ্যাক্টর বিশ্লেষণ করা হয়।
    """)

    # ইউজার ইনপুট
    flow_rate = st.slider("পানির প্রবাহ হার (কিউবিক মিটার/সেকেন্ড)", 100, 1000, 500)
    channel_width = st.number_input("নদীর প্রস্থ (মিটার)", min_value=10, max_value=1000, value=50)
    channel_slope = st.slider("নদীর ঢাল (Slope)", 0.0001, 0.01, 0.001, step=0.0001)
    roughness = st.slider("নদীর পৃষ্ঠের ঘর্ষণ (Manning's n)", 0.01, 0.1, 0.03)

    st.markdown("---")

    # Manning's equation থেকে পানির গতি হিসাব (approximate)
    # V = (1/n) * R^(2/3) * S^(1/2)
    # যেখানে R = হাইড্রোলিক রেডিয়াস (A/P), A=অঞ্চল, P=পেরিমিটার
    # সরল জন্য A=width*depth, P=width+2*depth (depth অনুমান করা হয়)

    # Depth অনুমান
    depth = flow_rate / (channel_width * 1.0)  # assuming velocity = 1 m/s approx for initial guess

    # হাইড্রোলিক রেডিয়াস R
    perimeter = channel_width + 2 * depth
    area = channel_width * depth
    R = area / perimeter

    velocity = (1 / roughness) * (R ** (2/3)) * (channel_slope ** 0.5)
    discharge = velocity * area

    st.write(f"অনুমান করা পানির গভীরতা: **{depth:.2f} মিটার**")
    st.write(f"হাইড্রোলিক রেডিয়াস (R): **{R:.2f} মিটার**")
    st.write(f"পানির গতি (Velocity): **{velocity:.2f} মিটার/সেকেন্ড**")
    st.write(f"সর্বমোট পানির প্রবাহ (Discharge): **{discharge:.2f} কিউবিক মিটার/সেকেন্ড**")

    # পানির গতি গ্রাফ
    x = np.linspace(0, 100, 500)  # নদীর দৈর্ঘ্য ধরে 0-100 মিটার
    y = velocity * np.exp(-0.01 * x)  # সিমুলেশন: গতি হ্রাস পায় দূরত্বের সাথে

    fig, ax = plt.subplots()
    ax.plot(x, y, label="Velocity along river (m/s)")
    ax.set_xlabel("নদীর দৈর্ঘ্য (মিটার)")
    ax.set_ylabel("পানির গতি (মিটার/সেকেন্ড)")
    ax.set_title("পানিপ্রবাহ সিমুলেশন")
    ax.legend()
    st.pyplot(fig)

