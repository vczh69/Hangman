import random
import tkinter as tk
from tkinter import ttk, messagebox

class Hangman:

    def __init__(self, master):
        self.tries = 0
        self.max_tries = 0
        self.difficulty = "Easy"
        self.difficulty_options = ["Easy", "Medium", "Hard"]
        self.display_word = []

        # GUI setup
        self.master = master
        self.master.title("Hangman by Gor Mar")

        self.frame = ttk.Frame(master)
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        # Title
        self.title_label = ttk.Label(self.frame, text="Hangman", font=("Arial", 15))
        self.title_label.grid(row=0, column=0, pady=10)

        # Difficulty
        self.difficulty_frame = tk.LabelFrame(self.frame, text="Difficulty", font=("Arial", 10))
        self.difficulty_frame.grid(row=1, column=0, pady=10)

        self.difficulty_var = tk.StringVar(value=self.difficulty)
        self.difficulty_dropdown = ttk.Combobox(self.difficulty_frame, textvariable=self.difficulty_var, values=self.difficulty_options, state='readonly')
        self.difficulty_dropdown.grid(row=0, column=0, padx=5, pady=5)
    
        # Start
        start_style = ttk.Style()
        start_style.configure("Start.TButton", font=("Arial", 15), width=13)

        self.start_button = ttk.Button(self.frame, style="Start.TButton", text="Start", command=self.start)
        self.start_button.grid(row=3, column=0, pady=10)

    def start(self):
        self.title_label.grid_forget()
        self.start_button.grid_forget()
        self.difficulty = self.difficulty_var.get()
        self.difficulty_frame.grid_forget()        

        with open(self.difficulty.lower() + ".txt", 'r') as file:
            words = file.read().splitlines()
            self.secret_word = random.choice(words).lower()
            print(f"Random word is:{self.secret_word}")
        
        for self.letter in self.secret_word:
            self.display_word += "_"

        self.max_tries = len(self.secret_word) + 5

        # Title Label
        self.guess_label = ttk.Label(self.frame, text="Guess the word:", font=("Arial", 15))
        self.guess_label.grid(row=0, column=0, pady=10)

        self.word_label = ttk.Label(self.frame, text=self.display_word, font=("Arial", 15))
        self.word_label.grid(row=1, column=0, pady=10)

        # Guess Entry
        self.entry_frame = tk.LabelFrame(self.frame, text="Guess", font=("Arial", 10))
        self.entry_frame.grid(row=2, column=0, pady=10)

        validate_cmd = self.frame.register(self.validate_input)
        self.guess_entry = ttk.Entry(self.entry_frame, width=23, validate='key', validatecommand=(validate_cmd, '%P'))
        self.guess_entry.grid(row=0, column=0, padx=5, pady=5)

        # Guess Button
        guess_style = ttk.Style()
        guess_style.configure("Guess.TButton", font=("Arial", 15), width=13)
        self.guess_button = ttk.Button(self.frame, style="Guess.TButton", text="Guess", command=self.guess)
        self.guess_button.grid(row=3, column=0, pady=10)

        # Tries Label
        self.tries_label = ttk.Label(self.frame, text=f"Tries: {self.tries}/{self.max_tries}", font=("Arial", 15))
        self.tries_label.grid(row=4, column=0, pady=10)

    def validate_input(self, input_text):
        return input_text.isalpha() and len(input_text) <= 1 or input_text == ''

    def guess(self):
        self.input = self.guess_entry.get()
        self.guess_letter = self.input.lower()
        self.tries += 1
        self.tries_label.configure(text=f"Tries: {self.tries}/{self.max_tries}")
        
        for position in range(len(self.secret_word)):
            self.letter = self.secret_word[position]
            if self.letter == self.guess_letter:
                self.display_word[position] = self.letter
        
        self.word_label.config(text=self.display_word)

        if "_" not in self.display_word:
            result = messagebox.askquestion("Game Over", "Congratulations! You won!\nDo you want to restart?", icon='info')
            self.handle_game_result(result)

        if self.tries == self.max_tries:
            result = messagebox.askquestion("Game Over", f"You lost. The word was: {self.secret_word}\nDo you want to restart?", icon='error')
            self.handle_game_result(result)

        self.guess_entry.delete(0, tk.END)

    def handle_game_result(self, result):
        if result == 'yes':
            self.entry_frame.grid_forget()
            self.guess_label.grid_forget()
            self.guess_button.grid_forget()
            self.tries_label.grid_forget()
            self.__init__(self.master)
        else:
            self.master.destroy()

def main():
    root = tk.Tk()
    app = Hangman(root)
    root.geometry("250x300")
    root.mainloop()

if __name__ == "__main__":
    main()