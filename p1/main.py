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

def start_timer():
	count_down(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
	canvas.itemconfig(timer_text, text=count)
	if count > 0:
		window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("AssSuckingTimer")
# window.minsize(width=600, height=600)
window.configure(bg="#020617", padx=200, pady=100)

# Main label
main_label = Label(text="BootyTimer", fg="yellow", bg="black", font=("Arial", 50, 'bold'))
main_label.grid(column=1, row=0)

# -- Canvas ---
canvas = Canvas(width=400, height=400, bg="#020617", highlightthickness=0)
girl_img = PhotoImage(file="w.png")
canvas.create_image(200, 200, image=girl_img)
timer_text = canvas.create_text(200, 175, text="00:00", font=(FONT_NAME, 50, "bold"), fill="#DA0C81")
canvas.grid(column=1, row=1)

# Adding Buttons
start_button = Button(text="Start", bg="#005B41", fg="white", font=("Arial", 20), command=start_timer)
start_button.grid(column=0, row=3, pady=20)
reset_button = Button(text="Reset", bg="#35155D", fg="white", font=("Arial", 20))
reset_button.grid(column=2, row=3, pady=20)

# Check marks
check_marks = Label(text="✔", background="green", font=("Arial", 30))
check_marks.grid(column=1, row=4)

# -- Window setup ---
window.mainloop()
