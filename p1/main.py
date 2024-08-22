
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Girlo")
# window.minsize(width=600, height=600)
window.configure(bg="#020617", padx=200, pady=200)

# -- Canvas ---
canvas = Canvas(width=200, height=200)
girl_img = PhotoImage(file="w.png")
canvas.create_image(100,100, image=girl_img)
canvas.pack()



# -- Window setup ---
window.mainloop()
