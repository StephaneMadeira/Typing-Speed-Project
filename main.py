from tkinter import *
import time


window = Tk()
window.title("Typing Speed Test")
window.geometry("1000x600")
window.grid_columnconfigure(1, weight= 2)

words = []
FONT = "Times 24 bold"

to_list = "Begin today. That's all the note said. There was no indication from where it came or who may have written it. Had it been meant for someone else? Meghan looked around the room, but nobody made eye contact back."

words = to_list.split()
def timer(letter):
    global time_start
    time_start = time.time()
    return time_start

def play(enter):
    user_words = []
    finish_time = time.time()
    for w in user_entry.get().split():
        if w in words:
            user_words.append(w)

    total_time = finish_time - time_start
    total_time = total_time / 60
    result = len(user_words) / total_time
    wpm.config(text=f'You got around {round(result)} WPM.', fg='green',font= "Times 16 bold")


# GUI
canvas = Canvas(window, width=700, height= 200, border= 2, relief= RIDGE)

text = canvas.create_text(350,100,text=to_list, font= FONT, width=700)
canvas.grid(column=1, row=0)

label = Label(window, text="Start typing whenever you want!\n Type ENTER when you finish!", font="Times 16 bold")
label.grid(column=1, row= 2, pady=(200,0))
user_entry = Entry(window, width=100)
user_entry.grid(column=1,row=3)
wpm = Label(window, text= '')
wpm.grid(column=1, row=2)

# user actions
window.bind('<Return>',play)
window.bind('<B>',timer)

# Program Loop
window.mainloop()



