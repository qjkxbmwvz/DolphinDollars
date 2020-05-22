#! /usr/bin/env python
#  -*- coding: utf-8 -*-

'''The assignment entry screen.'''

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkcalendar import DateEntry
import student_home_screen


class AssignmentEntryScreen(tk.Frame):
    '''This class populates the window with asssignment entry screen stuff.'''
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.configure(bg="white")

        font10 = "-family {Noto Sans} -size 18"
        font9 = "-family {Noto Sans} -size 24"

        master.title("Dolphin Dollars Assignment Entry")

        label_1 = tk.Label(self)
        label_1.place(relx=0.5, rely=0.067, anchor="center")
        label_1.configure(background="#ffffff", cursor="fleur", disabledforeground="#ffffff",
                          font=font9, foreground="#ed1c24", text='''Dolphin Dollars''')

        label_2 = tk.Label(self)
        label_2.place(relx=0.5, rely=0.178, anchor="center")
        label_2.configure(background="#ffffff", cursor="fleur",
                          font=font10, text='''Assignment Submission''')

        label_3 = tk.Label(self)
        label_3.place(relx=0.083, rely=0.333, anchor="e")
        label_3.configure(background="#ffffff", justify='right', text='''Assignment Date:''')

        label_4 = tk.Label(self)
        label_4.place(relx=0.1, rely=0.5, anchor="e")
        label_4.configure(background="#ffffff", justify='right',
                          text='''Assignment Size:''')

        self.cal = DateEntry(self, width=12, background='#ed1c24',
                             foreground='white', borderwidth=2)
        self.cal.place(relx=0.5, rely=0.333, anchor="center")

        self.employee_id_entry = tk.Entry(self)
        self.employee_id_entry.place(relx=0.25, rely=0.333, height=23, relwidth=0.527)
        self.employee_id_entry.configure(background="white", font="TkFixedFont")

        self.password_entry = tk.Entry(self)
        self.password_entry.place(relx=0.25, rely=0.578, height=23, relwidth=0.527)
        self.password_entry.configure(background="white", font="TkFixedFont")

        self.submit_button = tk.Button(self)
        self.submit_button.place(relx=0.5, rely=0.833, height=50, width=150, anchor="center")
        self.submit_button.configure(background="#ed1c24", foreground="#ffffff",
                                     text='''Submit''', command=self.submit)

    def submit(self):
        '''Contacts the database to authenticate the employee.'''
        print(self.cal.get())

    def go_back(self):
        '''Returns to the student home screen.'''
        self.master.switch_frame(student_home_screen.StudentHomeScreen)
