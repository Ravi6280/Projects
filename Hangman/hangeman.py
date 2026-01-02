import random as ran
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("1000x1000")

        self.word_list = ['apple', 'sweat', 'likes', 'india', 'treat', 'phone']
        self.word = ran.choice(self.word_list)
        self.guessmade = ''
        self.turns = 5

        self.hangman_images = [
            ImageTk.PhotoImage(Image.open("stage0.jpg").resize((500, 500))), 
            ImageTk.PhotoImage(Image.open("stage1.jpg").resize((500, 500))), 
            ImageTk.PhotoImage(Image.open("stage2.jpg").resize((500, 500))), 
            ImageTk.PhotoImage(Image.open("stage3.jpg").resize((500, 500))), 
            ImageTk.PhotoImage(Image.open("stage4.jpg").resize((500, 500))), 
        ]

        self.setup_gui()
    
    def setup_gui(self):
        self.label_word = tk.Label(self.root, text="_ " * len(self.word), font=("Helvetica", 20))
        self.label_word.pack(pady=20)

        self.hangman_label = tk.Label(self.root, image=self.hangman_images[0])
        self.hangman_label.pack(pady=20)

        self.label_prompt = tk.Label(self.root, text="Enter your guess:", font=("Helvetica", 12))
        self.label_prompt.pack()

        self.entry_guess = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_guess.pack()

        self.button_submit = tk.Button(self.root, text="Submit", command=self.make_guess)
        self.button_submit.pack(pady=20)
        
        self.button_reset = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.button_reset.pack(pady=20)
    
    def update_hangman_image(self):
        self.hangman_label.config(image=self.hangman_images[5 - self.turns])

    def update_word_label(self):
        display_word = ''
        for letter in self.word:
            if letter in self.guessmade:
                display_word += letter + ' '
            else:
                display_word += '_ '
        self.label_word.config(text=display_word)
        
        if display_word.replace(' ', '') == self.word:
            messagebox.showinfo("Hangman", "Congratulations, you won!")
            self.reset_game()

    def make_guess(self):
        guess = self.entry_guess.get().lower()
        self.entry_guess.delete(0, tk.END)
        if len(guess) == 1 and guess.isalpha() and guess not in self.guessmade:
            self.guessmade += guess
            if guess not in self.word:
                self.turns -= 1
                self.update_hangman_image()
                if self.turns == 0:
                    messagebox.showinfo("Hangman", f"You lost! The word was: {self.word}")
                    self.reset_game()
            self.update_word_label()
        elif len(guess) != 1:
            messagebox.showwarning("Invalid input", "Please enter a single letter.")
        elif not guess.isalpha():
            messagebox.showwarning("Invalid input", "Please enter a valid letter.")
        elif guess in self.guessmade:
            messagebox.showwarning("Invalid input", "You have already guessed this letter.")

    def reset_game(self):
        self.word = ran.choice(self.word_list)
        self.guessmade = ''
        self.turns = 5
        self.update_hangman_image()
        self.update_word_label()
        self.label_word.config(text="_ " * len(self.word))

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()


