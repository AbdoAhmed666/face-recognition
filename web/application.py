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
        ["Register", "Recognize", "Live Camera", "Delete"],
        icons=["person-plus", "search", "camera", "trash"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
    )

# Instead of switch_page(), we display a prompt to guide the user to select from sidebar.
if choice == "Register":
    st.title("📄 Register Page")
    st.markdown("⬅️ Please open the 'Register' page from the sidebar (it appears under 'pages').")

elif choice == "Recognize":
    st.title("🔍 Recognize Page")
    st.markdown("⬅️ Please open the 'Recognize' page from the sidebar (it appears under 'pages').")

elif choice == "Live Camera":
    st.title("📷 Live Camera Page")
    st.markdown("⬅️ Please open the 'Live Camera' page from the sidebar (it appears under 'pages').")

elif choice == "Delete":
    st.title("🗑️ Delete Page")
    st.markdown("⬅️ Please open the 'Delete' page from the sidebar (it appears under 'pages').")
