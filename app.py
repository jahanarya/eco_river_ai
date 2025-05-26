import streamlit as st

# ------------------ LOGIN FUNCTION ------------------
def login():
    st.sidebar.title("🔐 EcoRiver Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username == "admin" and password == "password":
            st.session_state["logged_in"] = True
        else:
            st.sidebar.error("❌ Incorrect username or password")

# ------------------ MAIN APP FUNCTION ------------------
def main_app():
    st.set_page_config(page_title="EcoRiver AI – Intelligent River Protection System", layout="wide")
    st.title("🌊 EcoRiver AI – Intelligent River Protection System")
    
    # 🌟 Slogan
    st.markdown("### 🛡️ *Saving Every Drop, Protecting Every River.*")
    
    # 👥 Team Members
    st.markdown("#### 👨‍💻 Project Team:")
    st.markdown("- **Mimtaj**")
    st.markdown("- **Tasfia Aminul Mimi**")
    st.markdown("- **Tanvir Ahmed Khan**")

    st.sidebar.title("🧭 EcoRiver AI Features")
    features = [
        "1. Home Dashboard",
        "2. River Map View",
        "3. Satellite Image Upload",
        "4. Image-Based Encroachment Detection",
        "5. Manual Encroachment Reporting",
        "6. AI Model Retraining",
        "7. PDF Report Generation",
        "8. Geo-Coordinate Extraction",
        "9. Historical Change Analysis",
        "10. Riverbank Overlay Detection",
        "11. ML Confidence Scoring",
        "12. Admin Panel",
        "13. User Feedback System",
        "14. Alert Sound System",
        "15. Email Alert System",
        "16. Encroachment Timeline Graph",
        "17. Monthly Encroachment Chart",
        "18. Zone-Wise Risk Map",
        "19. Live River CCTV Feed (Simulated)",
        "20. River Pollution Level Checker",
        "21. Public Awareness Section",
        "22. Legal Action Module",
        "23. River Boundary PDF Download",
        "24. NGO Collaboration Portal",
        "25. Media Gallery",
        "26. Success Stories",
        "27. Team Info",
        "28. River Cleanup Tracker",
        "29. Emergency Contact Button",
        "30. Auto River Area Calculator",
        "31. River Depth Estimator",
        "32. Community Forum",
        "33. News and Updates",
        "34. Language Selector",
        "35. Logout"
    ]

    choice = st.sidebar.selectbox("Select a Feature", features)

    st.subheader(f"🔹 Selected: {choice}")
    st.info("🔧 This is a placeholder for the selected feature's implementation.")

# ------------------ APP LAUNCH ------------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
else:
    main_app()
