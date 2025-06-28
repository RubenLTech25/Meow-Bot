import streamlit as st
import random
from streamlit.components.v1 import html

# --- Cat Config ---
AVATARS = {
    "Gray Tabby": "🐱",  # Default (your cat!)
    "Black Cat": "🐈⬛",
    "Orange Tabby": "🐈",
    "Siamese": "😸"
}

MOODS = {
    "happy": ["Meow!", "Purr...", "Mrow~", "*kneads paws*"],
    "grumpy": ["Hiss!", "MEEOOWW!", "＞﹏＜", "*swishes tail*"],
    "sleepy": ["Zzz...", "Mrrp...", "*yawns*", "(-_-)"]
}

# --- Sound Effects (Web Embed) ---
def play_sound(sound):
    html(f"""
    <audio autoplay>
        <source src="https://www.myinstants.com/media/sounds/{sound}.mp3" type="audio/mpeg">
    </audio>
    """)

# --- App ---
st.title("😺 Meow Bot 2.0")
st.caption("A moody cat chatbot with sound!")

# Sidebar Controls
with st.sidebar:
    st.header("⚙️ Cat Settings")
    # Avatar Picker
    avatar = st.radio("Choose your cat:", list(AVATARS.keys()), index=0)
    st.session_state.avatar = AVATARS[avatar]
    
    # Mood Tracker
    mood = st.select_slider("Current mood:", options=list(MOODS.keys()), value="happy")
    st.session_state.mood = mood

    # Sound Toggle
    st.session_state.sound_on = st.toggle("Enable purrs", True)

# Chat UI
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Meow! I'm a gray tabby cat like you! 😺"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Say something"):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Cat response
    response = f"""
    {st.session_state.avatar} **{random.choice(MOODS[st.session_state.mood])}**  
    *({st.session_state.mood} mood)*
    """
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response, unsafe_allow_html=True)
        if st.session_state.sound_on:
            play_sound(random.choice(["cat-purr", "cat-meow"]))

# Reset button
if st.sidebar.button("Reset Chat"):
    st.session_state.messages = []
    st.rerun()
