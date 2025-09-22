import streamlit as st

st.title("✨ What Perfume Matches Your Personality? ✨")

st.write("Answer the following questions to discover which fragrance best fits your vibe!")

# -----------------------------
# Questions
# -----------------------------
st.subheader("1. What's your ideal night out?")
night_out = st.radio(
    "Choose one:",
    ["A rooftop dinner with city lights 🌃", 
     "An exclusive party with close friends 🥂", 
     "A calm night with books and music 📚🎶",
     "A bold adventure, maybe a concert or trip 🎤✈️"]
)  # NEW

st.subheader("2. Which notes appeal to you the most?")
notes = st.multiselect(
    "Pick as many as you like:",
    ["Citrus 🍋", "Woody 🌲", "Spicy 🌶️", "Vanilla 🍦", "Leather 🐂", "Floral 🌸"]
)  # NEW

st.subheader("3. How bold is your personality?")
boldness = st.slider("Drag to set your level:", 1, 10, 5)  # NEW

st.subheader("4. How many perfumes do you currently own?")
collection_size = st.number_input("Enter a number:", min_value=0, max_value=50, step=1)

st.subheader("5. Which occasion do you wear fragrance for the most?")
occasion = st.selectbox(
    "Choose one:",
    ["Daily wear 🌞", "Formal events 🎩", "Romantic dates 💘", "Special luxury nights ✨"]
)

# -----------------------------
# Logic for Results
# -----------------------------
st.subheader("✨ Your Perfume Match ✨")

if st.button("Show My Perfume!"):
    if "Woody 🌲" in notes or boldness >= 8:
        result = {
            "name": "Bleu de Chanel",
            "desc": "Confident, elegant, and timeless.",
            "video": "videos/bleudechanel.mp4"
        }
    elif "Spicy 🌶️" in notes or night_out == "An exclusive party with close friends 🥂":
        result = {
            "name": "Tom Ford Noir",
            "desc": "Bold, mysterious, and unforgettable.",
            "video":  "videos/noir.mp4"
        }
    elif "Vanilla 🍦" in notes or occasion == "Romantic dates 💘":
        result = {
            "name": "Dior Tobacolor",
            "desc": "Warm, sensual, and charming.",
            "video": "videos/dior.mp4"
        }
    elif "Floral 🌸" in notes or night_out == "A rooftop dinner with city lights 🌃":
        result = {
            "name": "YSL Libre",
            "desc": "Feminine, free-spirited, and modern.",
            "video": "videos/ysl.mp4"
        }
    elif "Leather 🐂" in notes or occasion == "Special luxury nights ✨":
        result = {
            "name": "Armani Code Profumo",
            "desc": "Sophisticated, daring, and seductive.",
            "video": "videos/code.mp4"
        }
    else:
        result = {
            "name": "Creed Aventus",
            "desc": "Unique, adventurous, and powerful.",
            "video": "videos/creed.mp4"
        }

    # Display result
    st.success(f"**{result['name']}** – {result['desc']}")
    st.video(result["video"])  # shows a video

    # Celebrations 
    st.balloons()  # NEW
