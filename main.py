from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
rounds = 1
timer = None


def restart_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="READY??")
    timer_label.config(text='Timer')
    number_rounds.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    global rounds
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg='red')
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg='pink')
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg='green')
        number_rounds.config(text=f'Round\n{rounds}', fg=GREEN)
        rounds += 1


def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f'{count_min:02}:{count_sec:02}')
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=250, height=280, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file='tomato.png')
canvas.create_image(125, 125, image=tomato_pic)

timer_text = canvas.create_text(125, 230, text="Ready??", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=0)

reset_button = Button(text="Reset", command=restart_timer)
reset_button.grid(column=3, row=0)

number_rounds = Label(text=f'Round\n1', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
number_rounds.grid(column=1, row=3, pady=30)

window.mainloop()
