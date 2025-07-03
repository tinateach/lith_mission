import streamlit as st
import random

def initialize_game():
    st.session_state.step = 0
    st.session_state.points = 0
    st.session_state.correct_count = 0
    st.session_state.wrong_count = 0
    st.session_state.finished = False

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

st.title("☕ MISSION LIETUVA: COFFEE SHOP QUEST ")

if not st.session_state.finished:
    phrase, question, correct_answer = st.session_state.dialogue_steps[st.session_state.step]
    options = st.session_state.choices[st.session_state.step]

    st.markdown(f"### 🗨️ {phrase}")
    st.markdown(f"**{question}**")

    with st.form(key="answer_form"):
        user_choice = st.radio("Choose the correct answer:", options)
        submitted = st.form_submit_button("Submit")

    if submitted:
        if user_choice == correct_answer:
            st.session_state.points += 10
            st.session_state.correct_count += 1
            st.success("✅ Correct!")
        else:
            st.session_state.wrong_count += 1
            st.error(f"❌ Incorrect. Correct answer: {correct_answer}")

        st.session_state.step += 1
        if st.session_state.step >= len(st.session_state.dialogue_steps):
            st.session_state.finished = True

else:
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
        initialize_game()
