import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 1. Page Configuration (Component #1)
st.set_page_config(page_title="WidgetzWorld", page_icon="🎡", layout="wide")

# 2. Sidebar (Component #2)
st.sidebar.title("🎡 WidgetzWorld Nav")
page = st.sidebar.selectbox("Select a Zone", ["Information Desk", "The Input Playground", "Status & Feedback"]) # Component #3

# --- ZONE 1: ABOUT (The Assignment Requirements) ---
if page == "Information Desk":
    st.title("🎡 Welcome to WidgetzWorld") # Component #4
    st.divider() # Component #5
    
    # 3. Columns (Component #6)
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("What is WidgetzWorld?") # Component #7
        st.write("WidgetzWorld is a demo application designed to explore the vast library of Streamlit UI components. It acts as a visual dictionary for developers.") # Component #8
        
    with col2:
        st.header("Who is it for?") # Component #9
        st.info("Target User: New Python developers and UI/UX designers looking for rapid prototyping tools.") # Component #10

    st.subheader("App Logic") # Component #11
    st.markdown("""
    *   **Inputs:** User names, dates, numerical values, color choices, and file uploads.
    *   **Outputs:** Real-time data visualization, status messages, and interactive balloons.
    """) # Component #12

# --- ZONE 2: INPUT PLAYGROUND ---
elif page == "The Input Playground":
    st.title("🕹️ The Input Playground")
    
    # 4. Tabs (Component #13)
    tab1, tab2 = st.tabs(["Basic Inputs", "Advanced Selectors"])
    
    with tab1:
        name = st.text_input("Enter your Player Name", "User123") # Component #14
        age = st.number_input("Enter your Level (Age)", 1, 100, 18) # Component #15
        power_level = st.slider("Select Power Level", 0, 100, 50) # Component #16
        is_ready = st.checkbox("Ready to Play?") # Component #17
        
    with tab2:
        favorite_class = st.radio("Choose a Class", ["Mage", "Warrior", "Rogue"]) # Component #18
        skills = st.multiselect("Pick Skills", ["Fireball", "Stealth", "Healing", "Strength"]) # Component #19
        start_date = st.date_input("Adventure Start Date") # Component #20
        quest_time = st.time_input("Daily Quest Time") # Component #21

# --- ZONE 3: STATUS & FEEDBACK ---
elif page == "Status & Feedback":
    st.title("📊 Status & Output")
    
    # 5. Expander (Component #22)
    with st.expander("Click to see raw data logic"):
        st.code("print('This is where the magic happens!')", language='python') # Component #23
    
    # 6. Color Picker & Caption
    theme_color = st.color_picker("Customize your Aura", "#FF4B4B") # Component #24
    st.caption(f"Your current aura hex code is {theme_color}") # Component #25
    
    # 7. Final Action
    if st.button("Finalize Adventure"): # Component #26
        st.success("Adventure Data Saved!") # Component #27
        st.balloons() # Component #28
