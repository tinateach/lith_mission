import tkinter as tk
from tkinter import messagebox

points = 0
step = 0

# Game steps: Lithuanian phrase, English question, correct answer
dialogue_steps = [
    ("Kur yra kavinė?", "What does 'Kur yra kavinė?' mean?", "Where is the coffee shop?"),
    ("Kur galiu atsisėsti?", "What does 'Kur galiu atsisėsti?' mean?", "Where can I sit?"),
    ("Ar vieta laisva?", "What does 'Ar vieta laisva?' mean?", "Is this seat free?"),
    ("Kiek kainuoja kava?", "What does 'Kiek kainuoja kava?' mean?", "How much is the coffee?"),
    ("Prašau atnešti kavos.", "What does 'Prašau atnešti kavos.' mean?", "Please bring me coffee."),
    ("Ji per šalta.", "What does 'Ji per šalta.' mean?", "It is too cold."),
    ("Ji per karšta.", "What does 'Ji per karšta.' mean?", "It is too hot.")
]

# Multiple choice options for each step
options = [
    ["Where is the coffee shop?", "Where is the table?", "Where is the teacher?"],
    ["Where can I walk?", "Where can I sit?", "Where can I eat?"],
    ["Is this drink hot?", "Is this your coffee?", "Is this seat free?"],
    ["How much is the coffee?", "Is the coffee cold?", "Do you like coffee?"],
    ["Please bring me coffee.", "I don't want coffee.", "Can I make coffee?"],
    ["It is too cold.", "It is delicious.", "It is just right."],
    ["It is too bitter.", "It is too hot.", "It is too small."]
]

# UI
root = tk.Tk()
root.title("☕ Lithuanian Coffee Shop Game")
root.geometry("700x500")  # Increased window size for better spacing

phrase_label = tk.Label(root, text="", font=("Arial", 22), wraplength=650, justify="center")
question_label = tk.Label(root, text="", font=("Arial", 20), wraplength=650, justify="center")
buttons = []

def start_game():
    start_button.pack_forget()
    show_step()

def show_step():
    if step >= len(dialogue_steps):
        show_result()
        return

    phrase, question, _ = dialogue_steps[step]
    phrase_label.config(text=f"🗨️ {phrase}")
    question_label.config(text=question)

    for i in range(3):
        buttons[i].config(text=options[step][i])

    phrase_label.pack(pady=20)
    question_label.pack(pady=10)
    for btn in buttons:
        btn.pack(pady=5)

def check_answer(selected_text):
    global step, points
    correct = dialogue_steps[step][2]
    if selected_text == correct:
        points += 10
        messagebox.showinfo("✅ Correct!", "Well done!")
    else:
        messagebox.showerror("❌ Incorrect", f"The correct answer was: {correct}")
    step += 1
    show_step()

def show_result():
    for btn in buttons:
        btn.pack_forget()
    phrase_label.config(text=f"🎉 Coffee Shop Mission Complete!\nFinal Score: {points} points")
    if points == 70:
        result = "🏆 Perfect! You handled the café like a local!"
    elif points >= 40:
        result = "👍 Good job! You're on your way!"
    else:
        result = "🕵️ Keep learning! Practice makes perfect!"
    messagebox.showinfo("Mission Result", result)

# Setup buttons
for i in range(3):
    btn = tk.Button(root, text="", width=50, font=("Arial", 20),
                    command=lambda idx=i: check_answer(buttons[idx].cget("text")))
    buttons.append(btn)

# Title screen
title_label = tk.Label(root, text="☕ MISSION LIETUVA: COFFEE SHOP QUEST 🧩", font=("Arial", 26, "bold"), wraplength=650, justify="center")
start_button = tk.Button(root, text="Start Coffee Shop Game", font=("Arial", 20), command=start_game)

# Layout
title_label.pack(pady=30)
start_button.pack()

# Run app
root.mainloop()
