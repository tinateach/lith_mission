import streamlit as st
import random

st.set_page_config(page_title="☕ Lithuanian Coffee Shop Game", layout="centered")

# Master data
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

# --- Init session state ---
if "game_started" not in st.session_state:
    st.session_state.game_started = False
    st.session_state.step = 0
    st.session_state.points = 0
    st.session_state.correct_count = 0
    st.session_state.wrong_count = 0
    st.session_state.dialogue = []
    st.session_state.options = []
    st.session_state.show_feedback = False
    st.session_state.feedback_text = ""
    st.session_state.feedback_type = ""
    st.session_state.selected = None

# --- Start/Reset game ---
def start_game():
    st.session_state.step = 0
    st.session_state.points = 0
    st.session_state.correct_count = 0
    st.session_state.wrong_count = 0
    st.session_state.dialogue = random.sample(dialogue_steps_master, len(dialogue_steps_master))
    st.session_state.options = []
    for phrase, question, correct in st.session_state.dialogue:
        wrong_choices = random.sample([a for a in correct_answers_master if a != correct], 2)
        all_choices = wrong_choices + [correct]
        random.shuffle(all_choices)
        st.session_state.options.append(all_choices)
    st.session_state.game_started = True
    st.session_state.show_feedback = False
    st.session_state.feedback_text = ""
    st.session_state.selected = None

# --- Title screen ---
st.title("☕ MISSION LIETUVA: COFFEE SHOP QUEST ")

if not st.session_state.game_started:
    st.write("🎯 Learn Lithuanian through fun café interactions!")
    if st.button("Start Game"):
        start_game()

# --- Game in progress ---
elif st.session_state.step < len(st.session_state.dialogue):
    phrase, question, correct_answer = st.session_state.dialogue[st.session_state.step]
    choices = st.session_state.options[st.session_state.step]

    st.markdown(f"### 🗨️ {phrase}")
    st.write(f"**{question}**")
    st.write(f"**Progress:** {st.session_state.step + 1} / {len(st.session_state.dialogue)}")

    st.session_state.selected = st.radio(
        "Choose your answer:", choices, index=None, key=f"radio_{st.session_state.step}"
    )

    if not st.session_state.show_feedback:
        if st.button("Submit Answer"):
            if st.session_state.selected == correct_answer:
                st.session_state.feedback_text = "✅ Correct!"
                st.session_state.feedback_type = "success"
                st.session_state.points += 10
                st.session_state.correct_count += 1
            else:
                st.session_state.feedback_text = f"❌ Incorrect. The correct answer was: **{correct_answer}**"
                st.session_state.feedback_type = "error"
                st.session_state.wrong_count += 1
            st.session_state.show_feedback = True
    else:
        # Display feedback
        if st.session_state.feedback_type == "success":
            st.success(st.session_state.feedback_text)
        else:
            st.error(st.session_state.feedback_text)

        if st.button("Next Question"):
            st.session_state.step += 1
            st.session_state.show_feedback = False
            st.session_state.feedback_text = ""
            st.session_state.selected = None

# --- Game over screen ---
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
        start_game()
