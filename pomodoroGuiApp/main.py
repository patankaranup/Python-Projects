import time
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    label.config(text="Timer")
    check_mark.config(text="")
    # ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if REPS % 8 == 0:
        label.config(text="LONG BREAK", bg=YELLOW,
                     fg=RED, font=(FONT_NAME, 54, 'bold'))

        count_down(long_break_sec)
    elif REPS % 2 == 0:
        label.config(text="SHORT BREAK", bg=YELLOW,
                     fg=PINK, font=(FONT_NAME, 54, 'bold'))
        count_down(short_break_sec)
    else:
        label.config(text="WORK TIME", bg=YELLOW,
                     fg=GREEN, font=(FONT_NAME, 54, 'bold'))
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    # ADDING MINUTES AND SECONDS LOGIC
    count_min = math.floor(count / 60)
    count_sec = (count % 60)
    # dynamic Typing count sec change to string from int
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # writing to canvas
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)

    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            mark += '✔'
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Timer App (Pomodoro)")
window.config(padx=100, pady=50, bg=YELLOW, )


# label
label = Label(text="Timer")
label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 54, 'bold'))

label.grid(column=1, row=0)


# to show image use canvas widget
tomato_image = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white',
                                font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


# start button
start_btn = Button(text='Start', command=start_timer)
start_btn.config(highlightthickness=0)

start_btn.grid(row=4, column=0)

# checkmark
check_mark = Label()
check_mark.config(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=4)

# reset butn
reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.config(highlightthickness=0)
reset_btn.grid(column=2, row=4)


window.mainloop()
