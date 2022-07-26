# importing all the main packages
from tkinter import *
from tkinter import ttk
from functools import partial
import random, tkinter as tk


# create class canvas
class StudentInfo:

    # data contains student full names
    @staticmethod
    def student_name():
        name = ['Aileen Sabella Sentosa',
                'Alexander Christian Revandi',
                'Andreas Javier Gareso']
        return name

    # data contains student names
    @staticmethod
    def student_nickname():
        nim = ['Bella', 'Alex', 'Andreas']
        return nim

    # data contains student absence numbers
    @staticmethod
    def student_number():
        number = ['1', '2', '3']
        return number


# create a list to avoid the same student name
used_name_list = []


# designing positioning system
def position():
    random_number = random.randint(1, 3)
    if str(random_number) in StudentInfo.student_number():
        nim = StudentInfo.student_nickname()
        if random_number in used_name_list:
            position()
        else:
            used_name_list.append(random_number)
            print(used_name_list)
            return nim[random_number - 1]


# designing positioning interface
def position_interface():
    class_canvas.create_text(870, 231, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(750, 231, text=position(), font='poppins 12 bold', fill='#EEEEEE')
    class_canvas.create_text(870, 311, text=position(), font='poppins 12 bold', fill='#EEEEEE')

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
app.geometry('960x640')
app.title('Random Class Desk Positioning')

# designing main workspace interface
class_canvas = Canvas(app, width=960, height=640)
class_canvas.grid(row=1, column=1)

roundness = 20
color_fill = '#395B64'

# draw tables position
table_1 = round_rectangle(820, 200, 920, 260, roundness, fill=color_fill)
table_2 = round_rectangle(699, 200, 799, 260, roundness, fill=color_fill)
table_3 = round_rectangle(820, 280, 920, 340, roundness, fill=color_fill)
position_interface()

if __name__ == '__main__':
    app.mainloop()
