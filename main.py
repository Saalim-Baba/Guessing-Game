import random
import tkinter as tk
from tkinter import messagebox

def check_guess():
    global count
    count += 1
    if count > 10:
        end_game("TOO MANY TRIES. YOU LOSE")
    else:
        try:
            guess = int(guess_entry.get())
            if guess == secret_number:
                end_game(f"You're right, it was the number {secret_number}")
            elif guess < secret_number:
                update_feedback("Num is higher")
            elif guess > 100 and count > 5:
                update_feedback("Come on bro, its not that hard. Fucking idiot")
            elif guess > 100:
                update_feedback('Too High, only between 1-100')
            else:
                update_feedback("Num is lower")
        except ValueError:
            update_feedback("Invalid input")

def update_feedback(message):
    feedback_label.config(text=message)

def end_game(message):
    choice = True
    if choice:
        choice = False
        messagebox.showinfo("Game Over", message)
        root.quit()

root = tk.Tk()
root.title("Guessing Game")
root.geometry("500x250")
secret_number = random.randint(1, 100)
count = 0
choice = True
root.configure(background="Light grey")

label = tk.Label(root, text="Hello player, welcome to the GUESSING GAME", font="Arial, 10", pady=10, padx=10,  relief="solid")
label.pack()

instructions = tk.Label(root, text="Choose between 1-100.", font="Arial, 20", pady=10, padx=10, relief="solid")
instructions.pack()


guess_entry = tk.Entry(root)
guess_entry.pack()
guess_entry.place(y=130, x=180)

submit_button = tk.Button(root, text="Submit Guess", command=check_guess)
submit_button.pack()
submit_button.place(y=170, x=200)

feedback_label = tk.Label(root, text="Here are hints", relief="solid")
feedback_label.pack()
feedback_label.place(y=200, x=200)

root.mainloop()
