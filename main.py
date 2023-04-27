from tkinter import *
from english_words import get_english_words_set
import random


window = Tk()

window.config(width=800, height=600, background="#E9F8F9")
canvas = Canvas(width=800, height=450, background="#537FE7", highlightthickness=0,)
canvas.place(x=30, y=100)



#---------------CREATE A LIST OF 50 RANDOM WORDS----------
list_words = []


def words_list_upload():
    global list_words
    global canvas
    canvas.destroy()
    canvas = Canvas(width=800, height=450, background="#E9F8F9", highlightthickness=0, )
    canvas.place(x=30, y=100)
    words_set = get_english_words_set(['gcide'], lower=True)
    list_set = list(words_set)
    for i in range(50):
        random_word = random.choice(list_set)
        list_words.append(random_word)
    print(list_words)
    col = 0
    row = 2
    for i in range(len(list_words)):
        Label(canvas, text=list_words[i], highlightthickness=0, fg="black", background="#E9F8F9", font=("Times", 20, "normal")).grid(row=row, column=col)
        col += 1
        if col == 4:
            col = 0
            row += 1

words_list_upload()

#----------FUNCTION TO ACTIVATE TIMER WHEN PRESSED THE FIRTS LETTER INTO THE ENTRY BOX ----------
final_result_cpm = Label()
final_result_wpm = Label()
def countdown():
    global canvas, final_result_wpm, final_result_cpm
    final_result_wpm.destroy()
    final_result_cpm.destroy()
    correct_cpm_entry.delete(0, END)
    correct_cpm_entry.insert(0, '?')
    wpm_entry.delete(0, END)
    wpm_entry.insert(0, '?')
    seconds = 61
    for n in range(seconds):
        seconds -= 1
        timer_label.config(text=seconds)
        timer_label.update()
        window.after(1000)
        if seconds == 0:
            canvas.destroy()
            canvas = Canvas(width=800, height=350, background="#E9F8F9", highlightthickness=0, )
            canvas.place(x=30, y=100)
            final_result_cpm = Label(text=f'Your Final CPM is: {cpm_score}', bg="white", highlightthickness=0, fg="#1363DF",
                                     background="#E9F8F9", font=("Times", 40, "normal"))
            final_result_cpm.place(x=150, y=150)
            final_result_wpm = Label(text=f'Your Final WPM is: {wpm_score}', bg="white", highlightthickness=0,
                                     fg="#1363DF",
                                     background="#E9F8F9", font=("Times", 40, "normal"))
            final_result_wpm.place(x=150, y=250)




#---------- SETTING TIMER FOR RESTART BUTTON----------
def restart():
    global list_words, click
    final_result_wpm.destroy()
    final_result_cpm.destroy()
    list_words = []
    type_entry.delete(0, END)
    correct_cpm_entry.delete(0, END)
    correct_cpm_entry.insert(0, '?')
    wpm_entry.delete(0, END)
    wpm_entry.insert(0, '?')
    words_list_upload()
    click = 1
    countdown_entry()





#---------- SETTING TIMER FOR ENTRY TYPING----------

click = 1
def countdown_entry(event):
    global click
    if click == 1:
        click -= 1
        countdown()





#-----TOP LABELS--------#

#CORRECT CPM
correct_cpm = Label(text="Corrected CPM", bg="#E9F8F9", fg="#009EFF", highlightthickness=0,
                    font=('Arial', 15, "bold"))
correct_cpm.place(x=100, y=25)
correct_cpm_entry = Entry(width=5, bg="white", highlightthickness=0, fg="#009EFF", justify=CENTER)
correct_cpm_entry.insert(0, "?")
correct_cpm_entry.place(x=225, y=25)

#WPM LABEL
wpm = Label(text="WPM", bg="#E9F8F9", fg="#009EFF", highlightthickness=0,
                    font=('Arial', 15, "bold"))
wpm.place(x=300, y=25)
wpm_entry = Entry(width=5, bg="white", highlightthickness=0, fg="#009EFF", justify=CENTER)
wpm_entry.insert(0, "?")
wpm_entry.place(x=350, y=25)

#TIMER COUNTDOWN

timer = Label(text="Time left", bg="#E9F8F9", fg="#009EFF", highlightthickness=0,
                    font=('Arial', 15, "bold"))
timer.place(x=420, y=25)
timer_label = Label(text="60", width=3, bg="white", highlightthickness=0, fg="#009EFF")
timer_label.place(x=500, y=25)

#RESTART BUTTON

restart_button = Button(text="Restart", highlightbackground="#FFEA11", fg="#1363DF", highlightthickness=0,
                    font=('Arial', 15, "bold"), command=restart)
restart_button.place(x=680, y=25)

#TYPE ENTRY

type_entry = Entry(width=25, bg="white", highlightthickness=0, fg="black", background="#E9F8F9", font=("Times", 30, "normal"), justify=CENTER)
type_entry.place(x=400, y=545)

type_label = Label(text="Type words here  >", bg="white", highlightthickness=0, fg="#009EFF", background="#E9F8F9", font=("Times", 40, "normal"))
type_label.place(x=30, y=535)

#--------ACTIVATE THE COUNTDOWN CLICKING THE ENTRY BOX -------

type_entry.bind("<KeyRelease>", countdown_entry)


#--------- FUNCTION TO GET ENTRY VALUE--------
cpm_score = 0
wpm_score = 0
def get_entry_text(event):
    global cpm_score, wpm_score
    input_word = type_entry.get()
    if input_word in list_words:
        type_entry.config(fg="black")
        type_entry.delete(0, END)
        cpm_score += len(input_word)
        wpm_score = cpm_score / 5
        correct_cpm_entry.delete(0, END)
        correct_cpm_entry.insert(0, f'{cpm_score}')
        wpm_entry.delete(0, END)
        wpm_entry.insert(0, f'{wpm_score}')
    else:
        type_entry.config(fg="red")



type_entry.bind("<Return>", get_entry_text)


window.mainloop()


