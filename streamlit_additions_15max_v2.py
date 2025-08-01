
import streamlit as st
import random
import time

st.set_page_config(page_title="Additions ≤ 15", page_icon="➕", layout="centered")

st.title("🧠 Entraînement : Additions simples (≤ 15)")

# Initialisation
if "a" not in st.session_state:
    st.session_state.a = 0
    st.session_state.b = 0
    st.session_state.resultat = 0
    st.session_state.reponse = ""
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.feedback = ""
    st.session_state.start_time = time.time()
    st.session_state.stop = False

def nouvelle_question():
    st.session_state.a = random.randint(1, 14)
    st.session_state.b = random.randint(1, 15 - st.session_state.a)
    st.session_state.resultat = st.session_state.a + st.session_state.b
    st.session_state.reponse = ""
    st.session_state.feedback = ""

def verifier():
    try:
        reponse = int(st.session_state.reponse)
        st.session_state.total += 1
        if reponse == st.session_state.resultat:
            st.session_state.score += 1
            st.session_state.feedback = "✅ Bonne réponse !"
        else:
            st.session_state.feedback = f"❌ Faux : {st.session_state.a} + {st.session_state.b} = {st.session_state.resultat}"
        nouvelle_question()
    except:
        st.session_state.feedback = "⚠️ Entrez un nombre entier valide."

def arreter():
    st.session_state.stop = True

# Bouton Arrêter
st.button("🛑 Arrêter", on_click=arreter)

# Chrono
elapsed = int(time.time() - st.session_state.start_time)
minutes, seconds = divmod(elapsed, 60)
st.markdown(f"⏱️ Temps écoulé : **{minutes:02d}:{seconds:02d}**")

# Score
st.markdown(f"### 🎯 Score : {st.session_state.score} / {st.session_state.total}")

if not st.session_state.stop:
    # Affichage de l'addition
    if st.session_state.total == 0 and st.session_state.a == 0:
        nouvelle_question()

    st.markdown(f"### ➕ Combien font {st.session_state.a} + {st.session_state.b} ?")

    # Clavier numérique
    st.write("### Clavier numérique :")
    col1, col2, col3 = st.columns(3)
    for i in range(1, 10):
        if (i - 1) % 3 == 0:
            col1, col2, col3 = st.columns(3)
        col = [col1, col2, col3][(i - 1) % 3]
        if col.button(str(i)):
            st.session_state.reponse += str(i)

    col0, col_valider, col_effacer = st.columns(3)
    if col0.button("0"):
        st.session_state.reponse += "0"
    if col_effacer.button("⌫ Effacer"):
        st.session_state.reponse = st.session_state.reponse[:-1]
    if col_valider.button("✅ Valider"):
        verifier()

    # Affichage champ de réponse
    st.text_input("Ta réponse :", key="reponse", label_visibility="collapsed")

    # Feedback
    if st.session_state.feedback:
        st.write(st.session_state.feedback)

else:
    # Résumé si on arrête
    note = round((st.session_state.score / max(1, st.session_state.total)) * 20, 1)
    st.subheader("🏁 Entraînement terminé !")
    st.markdown(f"**Score final :** {st.session_state.score} / {st.session_state.total}")
    st.markdown(f"**Note :** {note} / 20")
    st.markdown(f"**Temps total :** {minutes:02d}:{seconds:02d}")
