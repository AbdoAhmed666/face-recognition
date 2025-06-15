import streamlit as st
from streamlit_option_menu import option_menu
import os

st.set_page_config(page_title="Face Recognition", layout="wide")

BASE_PATH = os.path.dirname(__file__)
LOGO_PATH = os.path.join(BASE_PATH, "assets", "logo.jpg")

with st.sidebar:
    st.image(LOGO_PATH, width=200)
    st.markdown("---")

    choice = option_menu(
        "Navigation",
        ["Home", "Register", "Recognize", "Live Camera", "Delete"],
        icons=["house", "person-plus", "search", "camera", "trash"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
    )

if choice == "Home":
    st.title("🏠 Welcome to Leap Smart Face Recognition")
    st.markdown(
        """
        This app supports:
        - 🔐 Face registration for smart home access.
        - 🔍 Image-based face recognition.
        - 📷 Live face detection via camera.
        - 🗑️ Managing face database.

        👉 Please use the left menu to navigate to the appropriate module.
        """
    )

elif choice == "Register":
    st.title("📝 Register Page")
    st.info("Use the **pages/1_Register.py** tab in the sidebar to access registration.")

elif choice == "Recognize":
    st.title("🔍 Recognize Page")
    st.info("Use the **pages/2_Recognize.py** tab in the sidebar to run recognition.")

elif choice == "Live Camera":
    st.title("📷 Live Camera")
    st.info("Use the **pages/3_Live_Camera.py** tab in the sidebar to start live recognition.")

elif choice == "Delete":
    st.title("🗑️ Delete Page")
    st.info("Use the **pages/4_Delete.py** tab in the sidebar to manage your face database.")
