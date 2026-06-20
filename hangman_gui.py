import tkinter as tk
from tkinter import messagebox
import random

WORDS = ["python", "apple", "coding", "computer", "game"]

root = tk.Tk()
root.title("🎮 Hangman Master")
root.state("zoomed")
root.configure(bg="#0f172a")
root.resizable(False, False)

word = ""
guessed_letters = []
attempts = 6
score = 0

title = tk.Label(
    root,
    text="🎮 HANGMAN MASTER",
    font=("Arial", 30, "bold"),
    bg="#0f172a",
    fg="#00ffff"
)
title.pack(pady=8)

score_label = tk.Label(
    root,
    text="🏆 Score: 0",
    font=("Arial", 20, "bold"),
    bg="#0f172a",
    fg="gold"
)
score_label.pack()

canvas = tk.Canvas(
    root,
    width=350,
    height=300,
    bg="#111827",
    highlightthickness=0
)
canvas.pack(pady=5)

word_label = tk.Label(
    root,
    text="",
    font=("Arial", 30, "bold"),
    bg="#0f172a",
    fg="white"
)
word_label.pack(pady=5)

lives_label = tk.Label(
    root,
    text="❤️❤️❤️❤️❤️❤️",
    font=("Arial", 25),
    bg="#0f172a"
)
lives_label.pack()

status_label = tk.Label(
    root,
    text="Click a letter to start",
    font=("Arial", 15, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
status_label.pack(pady=5)

keyboard_frame = tk.Frame(root, bg="#0f172a")
keyboard_frame.pack(pady=10)

buttons = {}

def draw_base():
    canvas.delete("all")

    canvas.create_line(40, 250, 260, 250, fill="white", width=4)
    canvas.create_line(80, 250, 80, 30, fill="white", width=4)
    canvas.create_line(80, 30, 200, 30, fill="white", width=4)
    canvas.create_line(200, 30, 200, 70, fill="white", width=4)

def draw_hangman():
    wrong = 6 - attempts

    if wrong >= 1:
        canvas.create_oval(170, 70, 230, 130, outline="white", width=3)

    if wrong >= 2:
        canvas.create_line(200, 130, 200, 190, fill="white", width=3)

    if wrong >= 3:
        canvas.create_line(200, 150, 160, 170, fill="white", width=3)

    if wrong >= 4:
        canvas.create_line(200, 150, 240, 170, fill="white", width=3)

    if wrong >= 5:
        canvas.create_line(200, 190, 170, 230, fill="white", width=3)

    if wrong >= 6:
        canvas.create_line(200, 190, 230, 230, fill="white", width=3)

def update_display():
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter.upper() + " "
        else:
            display += "_ "

    word_label.config(text=display)
    lives_label.config(text="❤️" * attempts)
    score_label.config(text=f"🏆 Score: {score}")

    if "_" not in display:
        win_game()

def win_game():
    global score

    score += 10

    messagebox.showinfo(
        "Winner",
        "🎉 Congratulations!\nYou guessed the word!"
    )

    new_game()

def lose_game():
    messagebox.showerror(
        "Game Over",
        f"💀 Game Over!\n\nThe word was: {word}"
    )

    new_game()

def guess_letter(letter):
    global attempts

    buttons[letter].config(
        state="disabled",
        bg="#374151"
    )

    guessed_letters.append(letter.lower())

    if letter.lower() not in word:
        attempts -= 1

        status_label.config(
            text=f"❌ Wrong Guess! {attempts} lives left",
            fg="red"
        )

        draw_hangman()

    else:
        status_label.config(
            text="✅ Correct Guess!",
            fg="#22c55e"
        )

    update_display()

    if attempts <= 0:
        lose_game()

def new_game():
    global word, guessed_letters, attempts

    word = random.choice(WORDS)
    guessed_letters = []
    attempts = 6

    draw_base()

    for btn in buttons.values():
        btn.config(
            state="normal",
            bg="#00bfff",
            fg="black"
        )

    status_label.config(
        text="Click a letter to start",
        fg="#38bdf8"
    )

    update_display()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

row = 0
col = 0

for letter in alphabet:

    btn = tk.Button(
        keyboard_frame,
        text=letter,
        width=3,
        height=2,
        font=("Arial", 14, "bold"),
        bg="#00bfff",
        fg="black",
        activebackground="#38bdf8",
        cursor="hand2",
        command=lambda l=letter: guess_letter(l)
    )

    btn.grid(
        row=row,
        column=col,
        padx=3,
        pady=3
    )

    buttons[letter] = btn

    col += 1

    if col == 7:
        row += 1
        col = 0

restart_btn = tk.Button(
    root,
    text="🔄 New Game",
    font=("Arial", 15, "bold"),
    bg="#22c55e",
    fg="white",
    width=17,
    command=new_game,
    cursor="hand2"
)
restart_btn.pack(pady=10)

new_game()

root.mainloop()
