import streamlit as st

st.set_page_config(page_title="☕ Lithuanian Coffee Shop Game", layout="centered")

# Dialogue steps: (phrase, English question, correct answer)
dialogue_steps = [
    ("Kur yra kavinė?", "What does 'Kur yra kavinė?' mean?", "Where is the coffee shop?"),
    ("Kur galiu atsisėsti?", "What does 'Kur galiu atsisėsti?' mean?", "Where can I sit?"),
    ("Ar vieta laisva?", "What does 'Ar vieta laisva?' mean?", "Is this seat free?"),
    ("Kiek kainuoja kava?", "What does 'Kiek kainuoja kava?' mean?", "How much is the coffee?"),
    ("Prašau atnešti kavos.", "What does 'Prašau atnešti kavos.' mean?", "Please bring me coffee."),
    ("Ji per šalta.", "What does 'Ji per šalta.' mean?", "It is too cold."),
    ("Ji per karšta.", "What does 'Ji per karšta.' mean?", "It is too hot.")
]

# Multiple choice options
options = [
    ["Where is the coffee shop?", "Where is the table?", "Where is the teacher?"],
    ["Where can I walk?", "Where can I sit?", "Where can I eat?"],
    ["Is this drink hot?", "Is this your coffee?", "Is this seat free?"],
    ["How much is the coffee?", "Is the coffee cold?", "Do you like coffee?"],
    ["Please bring me coffee.", "I don't want coffee.", "Can I make coffee?"],
    ["It is too cold.", "It is delicious.", "It is just right."],
    ["It is too bitter.", "It is too hot.", "It is too small."]
]

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.points = 0
    st.session_state.feedback_shown = False

# Title
st.markdown("## ☕ MISSION LIETUVA: COFFEE SHOP QUEST ")

# Game flow
if st.session_state.step < len(dialogue_steps):
    phrase, question, correct_answer = dialogue_steps[st.session_state.step]

    st.markdown(f"### 🗨️ {phrase}")
    st.markdown(f"**{question}**")

    selected = st.radio("Choose your answer:", options[st.session_state.step], key=f"choice_{st.session_state.step}")

    if st.button("Submit Answer"):
        if selected == correct_answer:
            st.success("✅ Correct! Well done!")
            st.session_state.points += 10
        else:
            st.error(f"❌ Incorrect. The correct answer was: **{correct_answer}**")
        st.session_state.step += 1
        st.session_state.feedback_shown = True

elif st.session_state.step >= len(dialogue_steps):
    st.markdown(f"## 🎉 Coffee Shop Mission Complete!")
    st.markdown(f"**Final Score: {st.session_state.points} points**")

    if st.session_state.points == 70:
        st.success("🏆 Perfect! You handled the café like a local!")
    elif st.session_state.points >= 40:
        st.info("👍 Good job! You're on your way!")
    else:
        st.warning("🕵️ Keep learning! Practice makes perfect!")

    if st.button("🔁 Replay"):
        st.session_state.step = 0
        st.session_state.points = 0
        st.session_state.feedback_shown = False
