import streamlit as st

# Title of App
st.title("Web Development Lab01")

# Assignment Data 
st.header("CS 1301")
st.subheader("Web Development - Section X")
st.subheader("Sheri Akram")   
st.subheader("GTID: 904131168]")
st.subheader("Section: C/KEARSE")

st.write("Welcome to my page!")
st.write("Use the sidebar to open the full pages, or preview them below:")

# Tabs for a seamless home page
tab1, tab2 = st.tabs(["📂 Portfolio", "🌸 Perfume Quiz"])

with tab1:
    st.subheader("Portfolio (Preview)")
    st.write("""
    - Personal projects 
    - Skills and experiences  
    """)
    st.info("👉 Open the **Portfolio** page from the sidebar for full details.")

with tab2:
    st.subheader("Perfume Quiz (Preview)")
    st.write("""
    A fun interactive quiz to test your knowledge about perfumes!  
    - Take a personality test 
    - Picks a fragrance for you based on your personality!
    """)
    st.info("👉 Try the full **Perfume Quiz** in the sidebar.")
