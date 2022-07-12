from tkinter import *
from tkinter import ttk
from functools import partial
import random, tkinter as tk


SCORE = 0
def PLAY_QUIZ():
    global SCORE, QUESTION
    YOUR_POINT = APP_CANVAS.create_text(148, 400, text='YOUR SCORE :', font='poppins 13 bold', fill='#4A6274')
    SCORE_POINT = APP_CANVAS.create_text(218, 401, text=f'{SCORE}', font='poppins 13 bold', fill='#B53737')

    def CALL_RESULT(QUESTION_RESULT, USER_ANSWER, QUESTION, QUESTION_TEXT, PROBLEM, INFORMATION):
        global SCORE

        def INCREASE_POINT():
            global SCORE
            SCORE += 1
            APP_CANVAS.itemconfig(SCORE_POINT, text=f'{SCORE}')
            APP_CANVAS.itemconfig(YOUR_POINT, text='YOUR SCORE :')

        def DECREASE_POINT():
            global SCORE
            SCORE -= 1
            APP_CANVAS.itemconfig(SCORE_POINT, text=f'{SCORE}')
            APP_CANVAS.itemconfig(YOUR_POINT, text='YOUR SCORE :')

        def OTHER_PROBLEM(QUESTION_TEXT, ANSWER, SCORE_POINT):
            APP_CANVAS.delete(QUESTION_TEXT)
            APP_CANVAS.delete(PROBLEM)
            APP_CANVAS.delete(ANSWER)
            APP_CANVAS.delete(SCORE_POINT)
            APP_CANVAS.delete(YOUR_POINT)
            NEW_GAME_BUTTON.configure(state='disabled')
            PLAY_QUIZ()

        # TAKE USER_ANSWER value
        COMPARE = USER_ANSWER.get()

        # COMPARING USER_ANSWER value with the sum of FIRST_NUM and SECOND_NUM
        if COMPARE == QUESTION:
            ANSWER = APP_CANVAS.create_text(473, 340, fill='#378805', anchor=tk.W,
                                            font='poppins 16 bold', text=f'CORRECT ANSWER')
            INCREASE_POINT()
        else:
            ANSWER = APP_CANVAS.create_text(473, 340, fill='#B53737', anchor=tk.W,
                                            font='poppins 13 bold', text=f'WRONG, It\'s {QUESTION}')
            QUESTION_ENTRY.configure(foreground='#B53737')
            if SCORE != 0:
                DECREASE_POINT()

        # SECOND GAME BUTTON
        OTHER_PROBLEM = partial(OTHER_PROBLEM, QUESTION_TEXT, ANSWER, SCORE_POINT)
        NEW_GAME_BUTTON = tk.Button(app, text='New Problems', state='normal',
                                    font='poppins 10', padx=6, command=OTHER_PROBLEM, bg='#4A6274', fg='#FFFFFF')
        APP_CANVAS.create_window(875, 350, window=NEW_GAME_BUTTON)
        SUBMIT_BUTTON.configure(state='disabled')

    # PLACEHOLDER FUNCTION
    def REMOVE_PLACEHOLDER(e):
        QUESTION_ENTRY.delete(0, END)
        QUESTION_ENTRY.configure(foreground='#000000')

    def ADD_PLACEHOLDER(e):
        QUESTION_ENTRY.insert(0, 'Your Answer Here')
        QUESTION_ENTRY.configure(foreground='#949494')

    # Number Generator
    FIRST_NUM = random.randint(-10, 10)
    SECOND_NUM = random.randint(-10, 10)
    THIRD_NUM = random.randint(-10, 10)
    if FIRST_NUM != 0:
        RESULT = (THIRD_NUM - SECOND_NUM) / FIRST_NUM
        if RESULT - int(RESULT) == 0:
            QUESTION = int(RESULT)
        else:
            QUESTION = round(RESULT, 2)
    else:
        PLAY_QUIZ()

    # Main Workspace
    PROBLEM = APP_CANVAS.create_text(184, 250, fill='#4A6274', font='Georgia 30 bold',
                                     text=f'Problem.')
    INFORMATION = APP_CANVAS.create_text(90, 375, fill='#4A6274', font='poppins 10', anchor=tk.W,
                                         text='Note: Write a fraction with 2 digits after comma, e.g. 1.37')
    if SECOND_NUM >= 0:
        QUESTION_TEXT = APP_CANVAS.create_text(89, 300, fill='#4A6274', font='poppins 16', anchor=tk.W,
                                               text=f'The value of a if >> {FIRST_NUM}a + {SECOND_NUM} = {THIRD_NUM} is.')
    else:
        QUESTION_TEXT = APP_CANVAS.create_text(89, 300, fill='#4A6274', font='poppins 16', anchor=tk.W,
                                               text=f'The value of a if >> {FIRST_NUM}a - {abs(SECOND_NUM)} = {THIRD_NUM} is.')

    # RESULT OUTPUT
    QUESTION_RESULT = ttk.Label(app)
    # APP_CANVAS.create_window(540, 450, window=QUESTION_RESULT)

    # Take User Input Guess
    USER = tk.DoubleVar(app, name='double')
    app.setvar(name='double', value='')
    QUESTION_ENTRY = ttk.Entry(app, width=30, textvariable=USER, font='poppins 13')

    #Adding Placeholder
    QUESTION_ENTRY.insert(0, '  Enter Your Answer')
    QUESTION_ENTRY.configure(foreground='#949494')
    QUESTION_ENTRY.bind('<FocusIn>', REMOVE_PLACEHOLDER)
    QUESTION_ENTRY.bind('<FocusOut>', ADD_PLACEHOLDER)
    APP_CANVAS.create_window(640, 300, window=QUESTION_ENTRY)

    # Call CALL_RESULT function
    CALL_RESULT = partial(CALL_RESULT, QUESTION_RESULT, USER, QUESTION, QUESTION_TEXT, PROBLEM, INFORMATION)

    # SUBMIT BUTTON
    SUBMIT_BUTTON = tk.Button(app, text='Submit Answer', borderwidth=1, state='normal',
                              font='poppins 10', padx=5, command=CALL_RESULT, bg='#4A6274', fg='#FFFFFF')
    APP_CANVAS.create_window(875, 300, window=SUBMIT_BUTTON)

    # EXIT BUTTON
    EXIT_BUTTON = tk.Button(app, text='EXIT QUIZ', font='poppins 10 bold',
                            width=13, padx=1, command=exit, bg='#4A6274', fg='#FFFFFF')
    APP_CANVAS.create_window(875, 400, window=EXIT_BUTTON)


def NEW_PROBLEM():
    APP_CANVAS.delete(NEW_GAME_LABEL)
    APP_CANVAS.delete(GAME_BUTTON)
    PLAY_QUIZ()


# Window Main Workspace
app = tk.Tk()
app.geometry('980x560')
app.title('Arithmetic Problem Generator')

# Create a Widget
APP_CANVAS = Canvas(app, width=980, height=560, bg='#F9DDD2')
APP_CANVAS.grid(row=0, column=0)

# Create NEW_GAME_LABEL
NEW_GAME_LABEL = APP_CANVAS.create_text(490, 290, fill='#4A6274', font='poppins 15',
                                        text='Press \'START QUIZ\' to start the QUIZ', state='normal')

# Create NEW GAME BUTTON
GAME_BUTTON = tk.Button(app, text='START QUIZ', width=10,
                        font='poppins 13 bold', padx=10, command=NEW_PROBLEM, bg='#4A6274', fg='#FFFFFF')
GAME_BUTTON = APP_CANVAS.create_window(490, 350, window=GAME_BUTTON)

if __name__ == "__main__":
    app.mainloop()
