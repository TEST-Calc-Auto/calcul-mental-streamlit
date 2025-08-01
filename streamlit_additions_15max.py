
import streamlit as st
import random
import time

st.set_page_config(page_title="Additions ≤ 15", page_icon="➕", layout="centered")

st.title("🧠 Entraînement : Additions simples (≤ 15)")

# Initialisation de l'état de session
if "a" not in st.session_state:
    st.session_state.a = random.randint(1, 14)
    st.session_state.b = random.randint(1, 15 - st.session_state.a)
    st.session_state.resultat = st.session_state.a + st.session_state.b
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.feedback = ""
    st.session_state.start_time = time.time()

def nouvelle_question():
    st.session_state.a = random.randint(1, 14)
    st.session_state.b = random.randint(1, 15 - st.session_state.a)
    st.session_state.resultat = st.session_state.a + st.session_state.b
    st.session_state.feedback = ""
    st.session_state.reponse = ""

def verifier():
    reponse = st.session_state.reponse
    st.session_state.total += 1
    if reponse == st.session_state.resultat:
        st.session_state.score += 1
        st.session_state.feedback = "✅ Bravo !"
    else:
        st.session_state.feedback = f"❌ Faux ! La bonne réponse était {st.session_state.resultat}."
    nouvelle_question()

# Chrono
elapsed = int(time.time() - st.session_state.start_time)
minutes, seconds = divmod(elapsed, 60)
st.markdown(f"⏱️ Temps écoulé : **{minutes:02d}:{seconds:02d}**")

# Affichage de l'addition
st.markdown(f"### Combien font {st.session_state.a} + {st.session_state.b} ?")

# Formulaire
with st.form(key="form_addition"):
    st.number_input("Ta réponse :", key="reponse", step=1, format="%d")
    submitted = st.form_submit_button("Valider")
    if submitted:
        verifier()

# Feedback
if st.session_state.feedback:
    st.write(st.session_state.feedback)

# Score
st.markdown(f"### 🎯 Score : {st.session_state.score} / {st.session_state.total}")
