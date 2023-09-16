from tkinter import *
import  math
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
initial = "none"
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(initial)
    timer.config(text="Timer")
    check_mark.config(text=" ")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        clock(long_break_sec)
        timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        clock(short_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        clock(work_sec)
        timer.config(text="Work", fg=GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def clock(time):
    # print(time)

    time_min = math.floor(time / 60)
    time_sec = time % 60
    if time_sec < 10:
        time_sec = f"0{time_sec}"
    if time_min < 10:
        time_min = f"0{time_min}"
    canvas.itemconfig(timer_text, text =f"{time_min}:{time_sec}")
    if time >0:
        global initial
        initial = window.after(1000, clock, time -1)
    else:
        start_timer()
        mark = ""
        no_of_session = math.floor(reps/2)
        for i in range(no_of_session):
            mark += "✓"
            check_mark.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label Timer
timer = Label(window, text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN, highlightthickness=0)
timer.grid(row=0, column=1)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)


# start Button
start = Button(text="Start",bg=YELLOW, highlightthickness=0, command=start_timer)
start.grid(row=2,column=0)

# Reset button
reset = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset)
reset.grid(row=2, column=2)

# Label Check_mark
check_mark = Label(window, font=(FONT_NAME, 15),bg=YELLOW,fg=GREEN, highlightthickness=0)
check_mark.grid(row=4,column=1)


window.mainloop()