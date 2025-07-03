import streamlit as st
import random

st.set_page_config(page_title="☕ Lithuanian Coffee Shop Game", layout="centered")

# --- Dialogue steps ---
dialogue_steps_master = [
    ("Kur yra kavinė?", "What does 'Kur yra kavinė?' mean?", "Where is the coffee shop?"),
    ("Kur galiu atsisėsti?", "What does 'Kur galiu atsisėsti?' mean?", "Where can I sit?"),
    ("Ar vieta laisva?", "What does 'Ar vieta laisva?' mean?", "Is this seat free?"),
    ("Kiek kainuoja kava?", "What does 'Kiek kainuoja kava?' mean?", "How much is the coffee?"),
    ("Prašau atnešti kavos.", "What does 'Prašau atnešti kavos.' mean?", "Please bring me coffee."),
    ("Ji per šalta.", "What does 'Ji per šalta.' mean?", "It is too cold."),
    ("Ji per karšta.", "What does 'Ji per karšta.' mean?", "It is too hot."),
    ("Ką norėtumėte užsisakyti?", "What does 'Ką norėtumėte užsisakyti?' mean?", "What would you like to order?"),
    ("Ar norėtumėte cukraus?", "What does 'Ar norėtumėte cukraus?' mean?", "Would you like some sugar?"),
    ("Ačiū, viskas gerai.", "What does 'Ačiū, viskas gerai.' mean?", "Thank you, everything is fine.")
]

correct_answers_master = [item[2] for item in dialogue_steps_master]

# --- Session State Initialization ---
if "game_started" not in st.session_state:
    st.session_state.game_started = False
    st.session_state.step = 0
    st.session_state.points = 0
    st.session_state.correct_count = 0
    st.session_state.wrong_count = 0
    st.session_state.dialogue = []
    st.session_state.options = []

# --- Game Reset ---
def reset_game():
    st.session_state.step = 0
    st.session_state.points = 0
    st.session_state.correct_count = 0
    st.session_state.wrong_count = 0
    st.session_state.game_started = True

    # Shuffle dialogue and prepare options
    st.session_state.dialogue = random.sample(dialogue_steps_master, len(dialogue_steps_master))
    st.session_state.options = []
    for phrase, question, correct in st.session_state.dialogue:
        wrong_choices = random.sample([ans for ans in correct_answers_master if ans != correct], 2)
        choices = wrong_choices + [correct]
        random.shuffle(choices)
        st.session_state.options.append(choices)

# --- Title Screen ---
st.title("☕ MISSION LIETUVA: COFFEE SHOP QUEST 🧩")

if not st.session_state.game_started:
    st.markdown("Learn Lithuanian through real café conversations! 🇱🇹")
    if st.button("🎮 Start Game"):
        reset_game()

# --- Game Play ---
elif st.session_state.step < len(st.session_state.dialogue):
    phrase, question, correct_answer = st.session_state.dialogue[st.session_state.step]
    choices = st.session_state.options[st.session_state.step]

    st.markdown(f"### 🗨️ {phrase}")
    st.markdown(f"**{question}**")
    st.markdown(f"**Progress:** Question {st.session_state.step + 1} of {len(st.session_state.dialogue)}")

    selected = st.radio("Choose your answer:", choices, key=f"q_{st.session_state.step}")

    if st.button("Submit Answer"):
        if selected == correct_answer:
            st.success("✅ Correct!")
            st.session_state.points += 10
            st.session_state.correct_count += 1
        else:
            st.error(f"❌ Incorrect. The correct answer was: **{correct_answer}**")
            st.session_state.wrong_count += 1
        st.session_state.step += 1
        st.experimental_rerun()

# --- Results ---
else:
    st.header("🎉 Coffee Shop Mission Complete!")
    st.subheader(f"🎯 Score: {st.session_state.points} / 100")
    st.write(f"✅ Correct answers: {st.session_state.correct_count}")
    st.write(f"❌ Incorrect answers: {st.session_state.wrong_count}")

    if st.session_state.points == 100:
        st.success("🏆 Perfect! You're a café pro!")
    elif st.session_state.points >= 60:
        st.info("👍 Good job! Keep practicing!")
    else:
        st.warning("🕵️ Keep learning! You're getting there!")

    if st.button("🔁 Play Again"):
        reset_game()
        st.experimental_rerun()
