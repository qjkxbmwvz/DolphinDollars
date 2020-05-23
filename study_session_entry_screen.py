#! /usr/bin/env python
#  -*- coding: utf-8 -*-

'''The assignment entry screen.'''

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkcalendar import DateEntry
import student_home_screen
import main_window

class StudySessionEntryScreen(tk.Frame):
    '''This class populates the window with study session entry screen stuff.'''
    def __init__(self, master, ids):
        tk.Frame.__init__(self, master)

        [self.emp_id, self.student_id] = ids.split(",")
        self.configure(bg="white")

        font10 = "-family {Noto Sans} -size 18"
        font9 = "-family {Noto Sans} -size 24"

        master.title("Dolphin Dollars Study Session Entry")

        label_1 = tk.Label(self)
        label_1.place(relx=0.5, rely=0.067, anchor="center")
        label_1.configure(background="#ffffff", cursor="fleur", disabledforeground="#ffffff",
                          font=font9, foreground="#ed1c24", text='''Dolphin Dollars''')

        label_2 = tk.Label(self)
        label_2.place(relx=0.5, rely=0.178, anchor="center")
        label_2.configure(background="#ffffff", cursor="fleur",
                          font=font10, text='''Study Session Submission''')

        label_3 = tk.Label(self)
        label_3.place(relx=0.25, rely=0.333, anchor="e")
        label_3.configure(background="#ffffff", justify='right', text='''Study Session Date:''')


        self.cal = DateEntry(self, background='#ed1c24',
                             foreground='white', borderwidth=2)
        self.cal.place(relx=0.4, rely=0.333, anchor="center")

        submit_button = tk.Button(self)
        submit_button.place(relx=0.4, rely=0.875, height=50, width=150, anchor="center")
        submit_button.configure(background="#ed1c24", foreground="#ffffff",
                                text='''Submit''', command=self.submit)

        cancel_button = tk.Button(self)
        cancel_button.place(relx=0.8, rely=0.875, height=50, width=150, anchor="center")
        cancel_button.configure(background="#ed1c24", foreground="#ffffff",
                                text='''Cancel''', command=self.go_back)

    def submit(self):
        '''Contacts the database to authenticate the employee.'''
        date = self.cal.get()
        self.master.execute(
            "CALL studySessionAssignmentDeposit(STR_TO_DATE('{}', '%m/%d/%Y'),{}, {})"
            .format(date, self.student_id, self.emp_id))




    def go_back(self):
        '''Returns to the student home screen.'''
        self.master.switch_frame(student_home_screen.StudentHomeScreen,
                                 "{},{}".format(self.emp_id, self.student_id))
