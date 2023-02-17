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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    progress.config("")
    header.config("")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        countdown(long_break_sec)
        header.config(text="Break", fg=RED)
    elif reps % 2 != 0:
        countdown(work_sec)
        header.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        header.config(text="Break", fg=PINK)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


header = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, 'bold'), background=YELLOW)
header.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 114, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", background=YELLOW, font=(FONT_NAME, 12), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", background=YELLOW, font=(FONT_NAME, 12), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

progress = Label(text="", fg=GREEN, background=YELLOW, font=(FONT_NAME, 22, 'bold'))
progress.config(pady=20)
progress.grid(row=3, column=1)


def countdown(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    print(count_min, count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        marks = ""
        for _ in range(reps//2):
            marks += "✓"
        progress.config(text=marks)
        start_timer()



window.mainloop()
