import io
import streamlit as st
import ollama
from PIL import Image

st.set_page_config(page_title="Ofrenda Familiar", layout="wide")

st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at 50% 0%, #4a154b 0%, #14081c 80%);
        color: #fce6c5;
        font-family: 'Georgia', serif;
    }
    
    h1, h2, h3, p {
        font-family: 'Georgia', serif !important;
    }
    
    div[data-testid="stImage"] img {
        border: 12px solid #f4f1ea !important;
        border-bottom: 45px solid #f4f1ea !important;
        border-radius: 2px !important;
        box-shadow: 4px 6px 20px rgba(0, 0, 0, 0.9) !important;
        transform: rotate(-3deg);
        filter: sepia(0.7) contrast(1.2) brightness(0.85);
        transition: transform 0.4s ease;
    }
    div[data-testid="stImage"] img:hover {
        transform: rotate(1deg) scale(1.02);
    }

    .stTextInput input, .stTextArea textarea {
        background-color: rgba(20, 8, 28, 0.8) !important;
        color: #fce6c5 !important;
        border: 1px solid #e67e22 !important;
        font-family: 'Georgia', serif;
    }

    .stButton>button {
        background-color: #6c3483 !important;
        color: #fce6c5 !important;
        border: 1px solid #fce6c5 !important;
        font-family: 'Georgia', serif;
        font-size: 1.1rem;
        padding: 10px;
        transition: all 0.3s;
        width: 100%;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }
    .stButton>button:hover {
        background-color: #e67e22 !important;
        color: #14081c !important;
        border-color: #14081c !important;
    }

    .parchment-letter {
        background-color: #eaddcf;
        color: #2b1414;
        padding: 40px;
        box-shadow: 3px 3px 25px rgba(0,0,0,0.9);
        font-family: 'Georgia', serif;
        font-size: 1.15rem;
        line-height: 1.8;
        border: 1px solid #c9b49e;
        white-space: pre-wrap;
        border-radius: 2px;
        background-image: repeating-linear-gradient(rgba(0,0,0,0.03) 0px, rgba(0,0,0,0.03) 2px, transparent 2px, transparent 100%);
    }
</style>
""", unsafe_allow_html=True)

candle_svg = """
<svg width="45" height="70" viewBox="0 0 40 60" xmlns="http://www.w3.org/2000/svg" style="vertical-align: middle; filter: drop-shadow(0px 0px 6px rgba(230, 126, 34, 0.7));">
    <path d="M20 5 C 25 15 25 20 20 25 C 15 20 15 15 20 5 Z" fill="#e67e22">
        <animate attributeName="opacity" values="0.7; 1; 0.6; 1; 0.8" dur="1.5s" repeatCount="indefinite" />
    </path>
    <path d="M20 12 C 22 17 22 20 20 23 C 18 20 18 17 20 12 Z" fill="#fff7cc" />
    <rect x="13" y="25" width="14" height="35" fill="#f4f1ea" rx="2"/>
    <path d="M13 28 C 16 33 20 28 23 35 C 25 28 27 28 27 25 L 13 25 Z" fill="#f4f1ea" />
</svg>
"""

marigold_svg = """
<svg width="35" height="35" viewBox="0 0 50 50" xmlns="http://www.w3.org/2000/svg" style="vertical-align: middle; margin: 0 10px;">
    <path d="M25 2 L29 13 L40 10 L33 19 L44 25 L33 31 L40 40 L29 37 L25 48 L21 37 L10 40 L17 31 L6 25 L17 19 L10 10 L21 13 Z" fill="#e67e22" stroke="#d35400" stroke-width="1.5"/>
    <path d="M25 8 L28 16 L36 14 L31 21 L39 25 L31 29 L36 36 L28 34 L25 42 L22 34 L14 36 L19 29 L11 25 L19 21 L14 14 L22 16 Z" fill="#f39c12" />
    <circle cx="25" cy="25" r="6" fill="#d35400"/>
</svg>
"""

st.markdown(f"""
<div style="display: flex; justify-content: center; align-items: center; padding-top: 20px;">
{candle_svg}
<h1 style="margin: 0 20px; font-size: 3rem; color: #e67e22; border-bottom: none; text-shadow: 2px 2px 8px rgba(0,0,0,0.8);">Ofrenda Familiar</h1>
{candle_svg}
</div>
<div style="text-align: center; margin-bottom: 40px;">
{marigold_svg} {marigold_svg} {marigold_svg}
<p style="color: #fce6c5; font-size: 1.2rem; margin-top: 15px; font-style: italic;">Leave a memory, light a candle, and welcome them home.</p>
</div>
""", unsafe_allow_html=True)

def process_image_context(image_bytes):
    try:
        response = ollama.chat(
            model="moondream",
            messages=[{"role": "user", "content": "Describe this old photograph respectfully in one brief sentence.", "images": [image_bytes]}]
        )
        return response['message']['content']
    except Exception:
        return ""

def generate_tribute_document(name, favorites, memory, photo_desc):
    instructions = f"""Write a deeply traditional, warm, and poetic Dia de los Muertos remembrance for {name}. 
    Favorites/Offerings: {favorites}. 
    Shared memory: {memory}. 
    {"Look of their photograph: " + photo_desc if photo_desc else ""}
    
    Write it as if it were a physical letter placed on an altar by a loving relative. Keep it to two heartfelt paragraphs."""
    try:
        response = ollama.chat(
            model="llama3.2:3b", 
            messages=[{"role": "user", "content": instructions}], 
            options={"temperature": 0.65}
        )
        return response['message']['content']
    except Exception:
        return "The candle flickers, but the words remain unspoken. Please ensure the local service is running."

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("The Memory")
    name = st.text_input("Whom do we honor?", placeholder="e.g., Tia Maria")
    favorites = st.text_input("Offerings (Food, music, flowers)", placeholder="e.g., Sweet bread, yellow marigolds")
    memory = st.text_area("A story you carry", placeholder="Write a memory you hold dear...", height=120)
    
    uploaded_file = st.file_uploader("Place a photograph on the altar", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.image(uploaded_file, caption="Placed with love", use_container_width=True)

with col2:
    st.subheader("The Tribute")
    if st.button("Light the Candle"):
        if not name or not memory:
            st.error("Please offer a name and a memory.")
        else:
            with st.spinner("Lighting the candle and gathering memories..."):
                photo_desc = None
                if uploaded_file:
                    img = Image.open(uploaded_file)
                    bytes_io = io.BytesIO()
                    img.convert("RGB").save(bytes_io, format="JPEG")
                    photo_desc = process_image_context(bytes_io.getvalue())
                
                tribute_text = generate_tribute_document(name, favorites, memory, photo_desc)
                
                st.markdown(f'<div class="parchment-letter">{tribute_text}</div>', unsafe_allow_html=True)