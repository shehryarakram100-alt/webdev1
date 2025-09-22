import streamlit as st
import info
import pandas as pd

st.set_page_config(page_title="Sheri's Portfolio", layout="wide")

# --- Title ---
st.title("🧑‍ Sheri's Portfolio")

# --- About section: image left, text right (aligned) ---
col1, col2 = st.columns([1, 3])
with col1:
    st.image(info.profile_picture, width=250)
with col2:
    st.subheader("About Me")
    st.write(info.about_me)
    st.write("---")

# --- Education ---
st.header("🎓 Education")
for key, value in info.education_data.items():
    st.write(f"**{key}:** {value}")

# --- Courses ---
st.header("📚 Courses")
course_df = pd.DataFrame(info.course_data)
st.dataframe(course_df, use_container_width=True)

# --- Experience ---
st.header("💼 Experience")
for job, (tasks, img) in info.experience_data.items():
    st.subheader(job)
    st.image(img, width=200)
    for task in tasks:
        st.write(f"- {task}")  # bullet points

# --- Leadership ---
st.header("🌟 Leadership")
for role in info.leadership_data.get("roles", []):
   st.write(f"- {role.get('title', '')} ({role.get('organization', '')}, {role.get('year', '')})")
  

# --- Activities ---
st.header("🎯 Activities")
for activity in info.activity_data:
    st.write(f"- {activity}")

