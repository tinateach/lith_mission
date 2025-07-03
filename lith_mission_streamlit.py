import streamlit as st
import random

def initialize_game():
    st.session_state.step = 0
    st.session_state.points = 0
    st.session_state.correct_count = 0
    st.session_state.wrong_count = 0
    st.session_state.finished = False
    st.session_state.validated = False
    st.session_state.feedback = ""
    st.session_state.confirmed_answer = None
    st.session_state.pending_answer = None
    st.session_state.show_feedback = False

    st.session_state.dialogue_steps = [
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
    random.shuffle(st.session_state.dialogue_steps)

    correct_answers = [item[2] for item in st.session_state.dialogue_steps]
    st.session_state.choices = []
    for phrase, question, correct in st.session_state.dialogue_steps:
        wrongs = random.sample([a for a in correct_answers if a != correct], 2)
        all_options = wrongs + [correct]
        random.shuffle(all_options)
        st.session_state.choices.append(all_options)

if "step" not in st.session_state:
    initialize_game()

# Game title in red color using HTML
st.markdown("<h1 style='color:red;'>☕ MISSION LIETUVA: COFFEE SHOP QUEST </h1>", unsafe_allow_html=True)

if not st.session_state.finished:

    total_questions = len(st.session_state.dialogue_steps)
    current_question = st.session_state.step + 1

    st.markdown(f"**Question {current_question} / {total_questions}**")

    phrase, question, correct_answer = st.session_state.dialogue_steps[st.session_state.step]
    options = st.session_state.choices[st.session_state.step]

    # Lithuanian phrase in blue
    st.markdown(f"### 🗨️ <span style='color:blue'>{phrase}</span>", unsafe_allow_html=True)
    st.markdown(f"**{question}**")

    if "pending_answer" not in st.session_state or st.session_state.pending_answer not in options:
        st.session_state.pending_answer = options[0]

    if not st.session_state.validated:
        st.session_state.pending_answer = st.radio(
            "Choose the correct answer:",
            options,
            index=options.index(st.session_state.pending_answer),
        )
    else:
        st.markdown(f"**Your answer:** {st.session_state.confirmed_answer}")

    if not st.session_state.validated:
        if st.button("Validate"):
            st.session_state.confirmed_answer = st.session_state.pending_answer
            if st.session_state.confirmed_answer == correct_answer:
                st.session_state.points += 10
                st.session_state.correct_count += 1
                st.session_state.feedback = "✅ Correct!"
            else:
                st.session_state.wrong_count += 1
                st.session_state.feedback = f"❌ Incorrect. Correct answer: {correct_answer}"
            st.session_state.validated = True
            st.session_state.show_feedback = True

    if st.session_state.show_feedback:
        if "Correct" in st.session_state.feedback:
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)

        if st.button("Next Question"):
            st.session_state.step += 1
            st.session_state.validated = False
            st.session_state.feedback = ""
            st.session_state.confirmed_answer = None
            st.session_state.pending_answer = None
            st.session_state.show_feedback = False

            if st.session_state.step >= len(st.session_state.dialogue_steps):
                st.session_state.finished = True

else:
    st.markdown("---")

    st.markdown("## 🎉 Coffee Shop Mission Complete!")
    st.markdown(f"**✅ Correct:** {st.session_state.correct_count}")
    st.markdown(f"**❌ Incorrect:** {st.session_state.wrong_count}")
    st.markdown(f"**🎯 Score:** {st.session_state.points} / 100")

    if st.session_state.points == 100:
        st.success("🏆 Perfect! You're a café pro!")
    elif st.session_state.points >= 60:
        st.info("👍 Good job! Keep practicing!")
    else:
        st.warning("🕵️ Keep learning! You're getting there!")

    if st.button("🔁 Play Again"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        initialize_game()
