# importing all the main packages
from tkinter import *
from pynput.keyboard import Key, Controller
import random, os, tkinter as tk


# create class canvas
class StudentInfo:

    # data contains student full names
    @staticmethod
    def student_name():
        name = ['Aileen Sabella Sentosa', 'Alexander Christian Revandi',
                'Andreas Javier Gareso', 'Bertram Steven Potalangi',
                'Christian Kurniawan', 'Dennis Fredyson Amalo',
                'Eduard Mario Kayesa', 'Fania Margaretha Budiharjo',
                'Gisela Herawati Kusumaningtyas', 'Grace Birgitta Handhinata',
                'Hizkia Sebastian Dannari', 'Immanuel Grepadya Moetar',
                'Jeremy Krisnanta Julian Adi', 'Juan Agustiano Ali',
                'Lukas Eric Danutirtho', 'Madeline Eliana Suwono',
                'Maria Angel Setitit', 'Martha Ora', 'Nathaniel Kevin',
                'Ni Luh Made Kartika Nariswari', 'Nonnie Felisha Savitri',
                'Paschalia Margaretha Permatasari', 'Patrick Ignatius Djogo Waso',
                'Russel Ezra Marvelinettou', 'Xavier Renjiro Ganeshia Talie']
        return name

    # data contains student names
    @staticmethod
    def student_nickname():
        nim = ['Bella', 'Alex', 'Andreas', 'Steven', 'Christian', 'Dennis', 'Mario',
               'Fania', 'Gisela', 'Grace', 'Hizkia', 'Gery', 'Jemy', 'Juan', 'Lukas',
               'Madeline', 'Angel', 'Martha', 'Kevin', 'Tika', 'Nonnie', 'Pascha',
               'Patrick', 'Marvel', 'Xavier']
        return nim

    # data contains student absence numbers
    @staticmethod
    def student_number():
        number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                  '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                  '21', '22', '23', '24', '25']
        return number

    # condition roll number
    @staticmethod
    def condition_number():
        num = ['8', '10', '15', '17', '21']
        return num


# create a list to avoid the same student name
first_crosscheck = []
second_crosscheck = []
check = []


# create restart program system
def restart():
    # restart function doesn't return any
    app.destroy()
    os.startfile('class-desk-position.py')
    keyboard.press(Key.shift)
    keyboard.press(Key.f10)
    keyboard.release(Key.shift)
    keyboard.release(Key.f10)


# counting 'True' word
def counting():
    count = 0
    for counter in check:
        if counter == 'True':
            count = count + 1
    return count


# call StudentInfo class
name = StudentInfo.student_name()
nim = StudentInfo.student_nickname()
absence = StudentInfo.student_number()
condition = StudentInfo.condition_number()


# designing important positioning system
def important_position():
    while True:
        random_number = random.randint(1, len(condition))
        if random_number not in first_crosscheck:
            for p in range(1, len(absence)):
                if absence[p - 1] == condition[random_number - 1]:
                    print(name[p - 1], '==', condition[random_number - 1])
                    first_crosscheck.append(random_number)
                    second_crosscheck.append(int(absence[p - 1]))
                    print(first_crosscheck)
                    print(second_crosscheck)
                    print(f'Full Name : {name[p - 1]}\n'
                          f'NickName : {nim[p - 1]}\n'
                          f'Roll Number : {absence[p - 1]}\n')
                    return nim[p - 1]
        else:
            continue


# designing other positioning system
def position():
    while True:
        random_number = random.randint(1, len(name))
        if random_number not in second_crosscheck:
            if str(random_number) in absence:
                second_crosscheck.append(random_number)
                print(second_crosscheck)
                print(f'Full Name : {name[random_number - 1]}\n'
                      f'NickName : {nim[random_number - 1]}\n'
                      f'Roll Number : {absence[random_number - 1]}\n')
                return nim[random_number - 1]
        else:
            continue


# designing positioning interface
def position_interface():

    class_canvas.create_text(870, 231, text=important_position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(750, 231, text=important_position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(630, 231, text=important_position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(510, 231, text=important_position(), font='poppins 12 bold', fill='#EEEEEE')

    class_canvas.create_text(870, 311, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(750, 311, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(630, 311, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(510, 311, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(390, 311, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(270, 311, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(150, 311, text=position(), font='poppins 12 bold', fill='#EEEEEE')

    # show and check if all item in condition has already show up on desktop
    for q in range(len(second_crosscheck)):
        if str(second_crosscheck[q]) in condition:
            check.append('True')

    if not len(check) == 5:
        restart()

    class_canvas.create_text(870, 391, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(750, 391, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(630, 391, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(510, 391, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(390, 391, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(270, 391, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(150, 391, text=position(), font='poppins 12 bold', fill='#EEEEEE')

    class_canvas.create_text(870, 471, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(750, 471, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(630, 471, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(510, 471, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(390, 471, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(270, 471, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(150, 471, text=position(), font='poppins 12 bold', fill='#EEEEEE')


# create round rectangle shape template
def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return class_canvas.create_polygon(points, **kwargs, smooth=True)


# create main workspace
app = tk.Tk()
app.geometry('1020x600')
app.title('Random Class Desk Positioning')

# designing main workspace interface
class_canvas = Canvas(app, width=960, height=640)
class_canvas.grid(row=1, column=1)

# control the roundness and color_fill value
roundness = 20
color_fill = '#395B64'

# initiate from package pynput
keyboard = Controller()

# draw tables position
table_1 = round_rectangle(820, 200, 920, 260, roundness, fill=color_fill)
table_2 = round_rectangle(700, 200, 800, 260, roundness, fill=color_fill)
table_3 = round_rectangle(580, 200, 680, 260, roundness, fill=color_fill)
table_4 = round_rectangle(460, 200, 560, 260, roundness, fill=color_fill)

table_5 = round_rectangle(820, 280, 920, 340, roundness, fill=color_fill)
table_6 = round_rectangle(700, 280, 800, 340, roundness, fill=color_fill)
table_7 = round_rectangle(580, 280, 680, 340, roundness, fill=color_fill)
table_8 = round_rectangle(460, 280, 560, 340, roundness, fill=color_fill)
table_9 = round_rectangle(340, 280, 440, 340, roundness, fill=color_fill)
table_10 = round_rectangle(220, 280, 320, 340, roundness, fill=color_fill)
table_11 = round_rectangle(100, 280, 200, 340, roundness, fill=color_fill)

table_12 = round_rectangle(820, 360, 920, 420, roundness, fill=color_fill)
table_13 = round_rectangle(700, 360, 800, 420, roundness, fill=color_fill)
table_14 = round_rectangle(580, 360, 680, 420, roundness, fill=color_fill)
table_15 = round_rectangle(460, 360, 560, 420, roundness, fill=color_fill)
table_16 = round_rectangle(340, 360, 440, 420, roundness, fill=color_fill)
table_17 = round_rectangle(220, 360, 320, 420, roundness, fill=color_fill)
table_18 = round_rectangle(100, 360, 200, 420, roundness, fill=color_fill)

table_19 = round_rectangle(820, 440, 920, 500, roundness, fill=color_fill)
table_20 = round_rectangle(700, 440, 800, 500, roundness, fill=color_fill)
table_21 = round_rectangle(580, 440, 680, 500, roundness, fill=color_fill)
table_22 = round_rectangle(460, 440, 560, 500, roundness, fill=color_fill)
table_23 = round_rectangle(340, 440, 440, 500, roundness, fill=color_fill)
table_24 = round_rectangle(220, 440, 320, 500, roundness, fill=color_fill)
table_25 = round_rectangle(100, 440, 200, 500, roundness, fill=color_fill)

# designing widget
teacher_table_1 = round_rectangle(250, 165, 360, 225, roundness, fill=color_fill)
teacher_table_2 = round_rectangle(135, 165, 245, 225, roundness, fill=color_fill)
whiteboard_1 = round_rectangle(180, 80, 500, 100, fill=color_fill)
whiteboard_2 = round_rectangle(505, 80, 825, 100, fill=color_fill)

class_canvas.create_text(515, 555, text='CLASS BLUEPRINT', font='poppins 18 bold', fill=color_fill)

# create reusable refresh button
position_interface()

# restart button
restart_round_button = round_rectangle(820, 520, 920, 580, roundness, fill='#800000')
restart_button = tk.Button(app, text='Restart', width=5, bd=0,
                           font='poppins 12 bold', padx=10, command=restart, bg='#800000', fg='#FFFFFF')
restart_button = class_canvas.create_window(870, 550, window=restart_button)

if __name__ == '__main__':
    app.mainloop()
