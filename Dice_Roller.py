# Dice Roller Game Version 0.0.0
# Copyright (c) 2025 Z_yx2
# Licensed under the MIT License

import tkinter as tk
import random

# score board
player_score = 0
compute_score = 0

# Roll dice function
def roll_dice(event=None):
    global player_score, compute_score


    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    dice4 = random.randint(1, 6)
    total1 = dice1 + dice2
    total2 = dice3 + dice4
    
    # total dice score
    result_label.config(
        text=f" You rolled {dice1} and {dice2} → Total: {total1}, Computer rolled {dice3} and {dice4} → Total: {total2}"
    )
    if total1 > total2:
        result_label.config(text=result_label.cget("text") + "\n You win this round!")
        player_score += 1
        score_label1.config(text=f"Player Score: {player_score}")
    elif total1 < total2:
        result_label.config(text=result_label.cget("text") + "\n Computer wins this round!")
        compute_score += 1
        score_label2.config(text=f"Computer Score: {compute_score}")
    elif total1 == total2:
        result_label.config(text=result_label.cget("text") + "\n It's a tie!")

# Game interface
root = tk.Tk()
root.title("Dice Roller 0.0.0")
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))


title_label = tk.Label(root, text=" Dice Roller Game", font=("Arial", 28, "bold"))
title_label.pack(pady=20)


roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 16), command=roll_dice)
roll_button.pack(pady=10)


root.bind('<Return>', roll_dice)


result_label = tk.Label(root, text="", font=("Arial", 20))
result_label.pack(pady=20)


score_label1 = tk.Label(root, text="Player Score: 0", font=("Arial", 20))
score_label1.pack(pady=20)
score_label2 = tk.Label(root, text="Computer Score: 0", font=("Arial", 20))
score_label2.pack(pady=20)


root.mainloop()


