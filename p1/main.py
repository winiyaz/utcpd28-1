
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
window.configure(bg="#020617", padx=200, pady=100)
check_mark = "✅"

# Main label
main_label = Label(text="BootyTimer", fg="yellow", bg="black", font=("Arial", 40, 'bold'))
main_label.grid(column=1, row=0)

# -- Canvas ---
canvas = Canvas(width=400, height=400, bg="#020617", highlightthickness=0)
girl_img = PhotoImage(file="w.png")
canvas.create_image(200,200, image=girl_img)
canvas.create_text(200,175, text="00:00", font=(FONT_NAME, 50, "bold"), fill="#DA0C81")
canvas.grid(column=1, row=1)

# Adding Buttons
start_button = Button(text="Start", bg="#005B41", fg="white", font=("Arial", 20))
start_button.grid(column=0, row=3, pady=20)
reset_button = Button(text="Reset", bg="#35155D", fg="white", font=("Arial", 20))
reset_button.grid(column=2, row=3, pady=20)

# -- Window setup ---
window.mainloop()
