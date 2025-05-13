import streamlit as st
import random
from PIL import Image
import base64

# === CONFIG ===
st.set_page_config(page_title="Quiz Interactiv", layout="centered")

# === CSS CUSTOM ===
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

# === LOGO HEADER ===
with open("horse-white-logo.png", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode()

st.markdown(f"""
    <div style='background-color:#000000;padding:10px 20px;display:flex;align-items:center;'>
        <img src='data:image/png;base64,{encoded}' style='height:40px;margin-right:10px;' />
        <h1 style='color:white;font-size:20px;margin:0;'>Quiz Interactiv</h1>
    </div>
""", unsafe_allow_html=True)

# === ÎNTREBĂRI CU IMAGINI ===
static_image_question = [
    {
        "enunt": "Ce componentă auto se află în imagine?",
        "image": "./engine.jpg",
        "raspuns1": "Ambreiaj",
        "raspuns2": "Cutie de viteze",
        "raspuns3": "Motor",
        "corect": "raspuns3"
    },
    {
        "enunt": "Ce componentă auto se află în imagine?",
        "image": "./cutie-viteze.jpg",
        "raspuns1": "Ambreiaj",
        "raspuns2": "Cutie de viteze",
        "raspuns3": "Motor",
        "corect": "raspuns2"
    }
]

# === ÎNTREBĂRI FĂRĂ IMAGINI ===
other_questions = [
    {
        "enunt": "Compania HORSE s-a desprins din:",
        "raspuns1": "Grupul VAG",
        "raspuns2": "Grupul Renault",
        "raspuns3": "Grupul Stelantis",
        "corect": "raspuns2"
    },
    {
        "enunt": "Compania HORSE produce:",
        "raspuns1": "Vehicule electrice",
        "raspuns2": "Vehicule pe benzina",
        "raspuns3": "Motoare si cutii de viteze termice si hibride",
        "corect": "raspuns3"
    },
    {
        "enunt": "Ce permite cutia de viteze?",
        "raspuns1": "Schimbarea raportului de transmise",
        "raspuns2": "Generarea de electricitate",
        "raspuns3": "Depozitarea pieselor vechi",
        "corect": "raspuns1"
    },
    {
        "enunt": "Ce combina un motor hibrid",
        "raspuns1": "Doua motoare termice",
        "raspuns2": "Un motor termic si unul electric",
        "raspuns3": "Doua motoare electrice",
        "corect": "raspuns2"
    },
    {
        "enunt": "Unde este sediul central al companiei HORSE?",
        "raspuns1": "Paris",
        "raspuns2": "Madrid",
        "raspuns3": "Bucuresti",
        "corect": "raspuns2"
    },
    {
        "enunt": "Ce oraș din România găzduiește o unitate majoră HORSE de producție motoare?",
        "raspuns1": "Mioveni",
        "raspuns2": "Cluj",
        "raspuns3": "Craiova",
        "corect": "raspuns1"
    },
    {
        "enunt": "Ce tip de transmisie oferă confort sporit în oraș?",
        "raspuns1": "Automată",
        "raspuns2": "Manuală",
        "raspuns3": "Cu lanț",
        "corect": "raspuns1"
    },
    {
        "enunt": "Ce înseamnă \"plug-in hybrid\"?",
        "raspuns1": "Mașină 100% electrică",
        "raspuns2": "Hibrid fără baterie",
        "raspuns3": "Hibrid care poate fi încărcat la priză",
        "corect": "raspuns3"
    },
    {
        "enunt": "Ce înseamnă R&D în industria auto?",
        "raspuns1": "Repair & Distribution",
        "raspuns2": "Research & Development",
        "raspuns3": "Rotate & Drive",
        "corect": "raspuns2"
    },
    {
        "enunt": "Ce componentă nu face parte dintr-un sistem de transmisie?",
        "raspuns1": "Ambreiaj",
        "raspuns2": "Cutia de viteze",
        "raspuns3": "Parbriz",
        "corect": "raspuns3"
    }
]

# === INITIALIZARE QUIZ ===
if 'intrebari_random' not in st.session_state:
    static_q = random.sample(static_image_question, 1)
    selected_others = random.sample(other_questions, 4)
    st.session_state.intrebari_random = static_q + selected_others
    random.shuffle(st.session_state.intrebari_random)
    st.session_state.index = 0
    st.session_state.scor = 0

# === ÎNTREBARE CURENTĂ ===
if st.session_state.index < 5:
    cur = st.session_state.intrebari_random[st.session_state.index]
    st.subheader(f"Întrebarea {st.session_state.index + 1} din 5")
    st.write(cur['enunt'])

    if 'image' in cur:
        img = Image.open(cur['image'])
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image(img, width=300)
        st.markdown("</div>", unsafe_allow_html=True)

    optiuni = [key for key in ['raspuns1', 'raspuns2', 'raspuns3', 'raspuns4'] if key in cur]
    raspuns_selectat = st.radio("Alege varianta corectă:", [cur[o] for o in optiuni], index=0)

    if st.button("Continuă"):
        idx = [cur[o] for o in optiuni].index(raspuns_selectat)
        if optiuni[idx] == cur['corect']:
            st.session_state.scor += 1
        st.session_state.index += 1
        st.rerun()

# === FINAL ===
else:
    st.balloons()
    st.success(f" Ai terminat! Scorul tău: {st.session_state.scor}/5")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Reia quiz-ul"):
            for key in ['intrebari_random', 'index', 'scor']:
                del st.session_state[key]
            st.rerun()

    with col2:
         if st.button("Ieși din chestionar"):
            st.markdown("""
                <meta http-equiv="refresh" content="0; url='https://www.horse.cars/'" />
            """, unsafe_allow_html=True)
