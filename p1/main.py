import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
	global reps
	reps += 1

	work_sec = WORK_MIN * 60
	short_break_sec = SHORT_BREAK_MIN * 60
	long_break_sec = LONG_BREAK_MIN * 60

	if reps % 8 == 0:
		count_down(long_break_sec)
	elif reps % 2 == 0:
		count_down(short_break_sec)
	else:
		count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
	count_min = math.floor(count / 60)
	count_sec = count % 60
	if count_sec < 10:
		count_sec = f"0{count_sec}"  # Dynamic typing here
	canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
	if count > 0:
		window.after(1000, count_down, count - 1)
	else:
		start_timer()


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
timer_text = canvas.create_text(200, 175, text="00:00", font=(FONT_NAME, 40, "bold"), fill="#DA0C81")
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
