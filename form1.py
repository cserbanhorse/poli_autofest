import streamlit as st
import random
from PIL import Image
import base64

# CONFIG
st.set_page_config(page_title="Quiz Interactiv", layout="centered")

# === STYLE ===
st.markdown("""
    <style>
        .stButton > button {
            background-color: black;
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 5px;
        }

        .stButton > button:hover {
            background-color: #333333;
            color: white;
        }

        div[data-baseweb="radio"] div[role="radio"] {
            background-color: white;
            border: 2px solid black;
        }

        div[data-baseweb="radio"] div[role="radio"][aria-checked="true"] {
            background-color: black;
            color: white;
        }

        div[data-baseweb="radio"] div[role="radio"]:hover {
            border-color: black;
        }

        div[data-baseweb="radio"] div[role="radio"]:focus {
            outline: none;
        }
    </style>
""", unsafe_allow_html=True)

# === ENCODE LOGO ===
with open("horse-white-logo.png", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode()

# === HEADER ===
st.markdown(f"""
    <div style='background-color:#000000;padding:10px 20px;display:flex;align-items:center;'>
        <img src='data:image/png;base64,{encoded}' style='height:40px;margin-right:10px;' />
        <h1 style='color:white;font-size:20px;margin:0;'>Quiz Interactiv</h1>
    </div>
""", unsafe_allow_html=True)

# === QUESTIONS ===
intrebari = [
    {"enunt": "Care este capitala Italiei?", "raspuns1": "Madrid", "raspuns2": "Roma", "raspuns3": "Paris", "raspuns4": "Lisabona", "corect": "raspuns2"},
    {"enunt": "Câte continente există pe Pământ?", "raspuns1": "1", "raspuns2": "7", "raspuns3": "4", "raspuns4": "2", "corect": "raspuns2"},
    {"enunt": "Cine a scris „Hamlet”?", "raspuns1": "Dante Alighieri", "raspuns2": "J.K. Rowling", "raspuns3": "William Shakespeare", "raspuns4": "Lev Tolstoi", "corect": "raspuns3"},
    {"enunt": "În ce an a avut loc Revoluția Franceză?", "raspuns1": "1789", "raspuns2": "1848", "raspuns3": "1812", "raspuns4": "1914", "corect": "raspuns1"},
    {"enunt": "Ce planetă este cunoscută ca „Planeta Roșie”?", "raspuns1": "Venus", "raspuns2": "Jupiter", "raspuns3": "Marte", "raspuns4": "Saturn", "corect": "raspuns3"},
    {"enunt": "Ce limbaj se folosește pentru pagini web?", "raspuns1": "Python", "raspuns2": "HTML", "raspuns3": "SQL", "raspuns4": "Java", "corect": "raspuns2"},
    {"enunt": "Cât face 9 × 7?", "raspuns1": "56", "raspuns2": "63", "raspuns3": "72", "raspuns4": "69", "corect": "raspuns2"},
    {"enunt": "Cine a pictat „Mona Lisa”?", "raspuns1": "Michelangelo", "raspuns2": "Leonardo da Vinci", "raspuns3": "Pablo Picasso", "raspuns4": "Van Gogh", "corect": "raspuns2"}
]

# === SESSION INIT ===
if 'intrebari_random' not in st.session_state:
    st.session_state.intrebari_random = random.sample(intrebari, 5)
    st.session_state.index = 0
    st.session_state.scor = 0
    st.session_state.show_feedback = False
    st.session_state.last_correct = None
    st.session_state.raspuns_selectat = None

# === QUIZ FLOW ===
if st.session_state.index < 5:
    cur = st.session_state.intrebari_random[st.session_state.index]
    st.subheader(f"Întrebarea {st.session_state.index + 1} din 5")
    st.write(cur['enunt'])

    optiuni = ['raspuns1', 'raspuns2', 'raspuns3', 'raspuns4']
    st.session_state.raspuns_selectat = st.radio(
        "Alege varianta corectă:",
        [cur[o] for o in optiuni],
        index=0,
        key="radio"
    )

    if not st.session_state.show_feedback:
        if st.button("Verifică răspunsul"):
            idx = [cur[o] for o in optiuni].index(st.session_state.raspuns_selectat)
            st.session_state.last_correct = optiuni[idx] == cur['corect']
            if st.session_state.last_correct:
                st.session_state.scor += 1
            st.session_state.show_feedback = True
            st.rerun()
    else:
        if st.session_state.last_correct:
            st.success(" Corect!")
        else:
            st.error(f" Greșit! Răspunsul corect era: {cur[cur['corect']]}")
        if st.button("Pasul următor"):
            st.session_state.index += 1
            st.session_state.show_feedback = False
            st.session_state.raspuns_selectat = None
            st.rerun()

else:
    st.balloons()
    st.success(f" Ai terminat! Scorul tău: {st.session_state.scor}/5")

    if st.button("Ieși din quiz"):
        st.markdown("<meta http-equiv='refresh' content='0; URL=https://www.horse.cars/' />", unsafe_allow_html=True)
