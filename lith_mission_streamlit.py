import tkinter as tk
from tkinter import messagebox
import random

# Game state
points = 0
step = 0
correct_count = 0
wrong_count = 0

# Lithuanian phrases, questions, correct answers
dialogue_steps = [
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

# Extract correct answers for generating fake choices
correct_answers = [item[2] for item in dialogue_steps]

# Shuffle the questions
random.shuffle(dialogue_steps)

# Create shuffled options for each step
shuffled_options = []
for phrase, question, correct in dialogue_steps:
    wrong_choices = random.sample([ans for ans in correct_answers if ans != correct], 2)
    all_choices = wrong_choices + [correct]
    random.shuffle(all_choices)
    shuffled_options.append(all_choices)

# Setup UI window
root = tk.Tk()
root.title("☕ Lithuanian Coffee Shop Game")
root.geometry("700x500")

phrase_label = tk.Label(root, text="", font=("Arial", 22), wraplength=650, justify="center")
question_label = tk.Label(root, text="", font=("Arial", 20), wraplength=650, justify="center")
buttons = []

def start_game():
    start_button.pack_forget()
    title_label.pack_forget()
    show_step()

def show_step():
    if step >= len(dialogue_steps):
        show_result()
        return

    phrase, question, _ = dialogue_steps[step]
    phrase_label.config(text=f"🗨️ {phrase}")
    question_label.config(text=question)

    for i in range(3):
        buttons[i].config(text=shuffled_options[step][i])

    phrase_label.pack(pady=20)
    question_label.pack(pady=10)
    for btn in buttons:
        btn.pack(pady=5)

def check_answer(selected_text):
    global step, points, correct_count, wrong_count
    correct = dialogue_steps[step][2]

    if selected_text == correct:
        points += 10
        correct_count += 1
        messagebox.showinfo("✅ Correct!", "Well done!")
    else:
        wrong_count += 1
        messagebox.showerror("❌ Incorrect", f"The correct answer was: {correct}")
    
    step += 1
    show_step()

def show_result():
    for btn in buttons:
        btn.pack_forget()
        
    question_label.pack_forget()
    phrase_label.config(text="🎉 Coffee Shop Mission Complete!")

    summary = f"✅ Correct: {correct_count}\n❌ Incorrect: {wrong_count}\n🎯 Score: {points}/100"
    
    if points == 100:
        result = "🏆 Perfect! You're a café pro!"
    elif points >= 60:
        result = "👍 Good job! Keep practicing!"
    else:
        result = "🕵️ Keep learning! You're getting there!"

    messagebox.showinfo("Mission Result", f"{result}\n\n{summary}")

# Create answer buttons
for i in range(3):
    btn = tk.Button(root, text="", width=50, font=("Arial", 20),
                    command=lambda idx=i: check_answer(buttons[idx].cget("text")))
    buttons.append(btn)

# Title and start button
title_label = tk.Label(root, text="☕ MISSION LIETUVA: COFFEE SHOP QUEST 🧩", font=("Arial", 26, "bold"), wraplength=650, justify="center")
start_button = tk.Button(root, text="Start Coffee Shop Game", font=("Arial", 20), command=start_game)

title_label.pack(pady=30)
start_button.pack()

# Start main loop
root.mainloop()
