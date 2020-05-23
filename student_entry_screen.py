#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.3
#  in conjunction with Tcl version 8.6
#    May 21, 2020 07:14:13 PM PDT  platform: Linux

'''The student entry screen.'''

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import tkinter.messagebox
import login_screen
import student_home_screen


class StudentEntryScreen(tk.Frame):
    '''This class populates the window with entry screen stuff.'''
    def __init__(self, master, emp_id):
        tk.Frame.__init__(self, master)

        self.emp_id = emp_id
        self.configure(bg="white")

        font10 = "-family {Noto Sans} -size 18"
        font9 = "-family {Noto Sans} -size 24"

        master.title("Dolphin Dollars Student Entry")

        label_1 = tk.Label(self)
        label_1.place(relx=0.5, rely=0.067, anchor="center")
        label_1.configure(background="#ffffff", cursor="fleur", disabledforeground="#ffffff",
                          font=font9, foreground="#ed1c24", text='''Dolphin Dollars''')

        label_2 = tk.Label(self)
        label_2.place(relx=0.5, rely=0.178, anchor="center")
        label_2.configure(background="#ffffff", cursor="fleur",
                          font=font10, text='''Student Entry''')

        label_3 = tk.Label(self)
        label_3.place(relx=0.083, rely=0.489, height=23, width=90)
        label_3.configure(activebackground="#ffffff", background="#ffffff",
                          disabledforeground="#ffffff", justify='right', text='''Student ID:''')

        self.student_id_entry = tk.Entry(self)
        self.student_id_entry.place(relx=0.25, rely=0.489, height=23, relwidth=0.527)
        self.student_id_entry.configure(background="white", font="TkFixedFont")

        submit_button = tk.Button(self)
        submit_button.place(relx=0.45, rely=0.578, height=33, width=61)
        submit_button.configure(background="#ed1c24", foreground="#ffffff",
                                text='''Submit''', command=self.authenticate)

        logout_button = tk.Button(self)
        logout_button.place(relx=0.45, rely=0.9, height=33, width=61)
        logout_button.configure(background="#ed1c24", foreground="#ffffff",
                                text='''Log Out''', command=self.log_out)

    def authenticate(self):
        '''Contacts the database to authenticate the employee.'''
        student_id = self.student_id_entry.get()

        if not student_id:
            tk.messagebox.showerror("Enter a Student ID",
                                    "Please enter a student ID to proceed.")
            return

        cursor = self.master.execute(
            "SELECT AuthenticateStudent({});".format(student_id))

        for i in cursor:
            for j in i:
                if j == 1:
                    self.master.switch_frame(student_home_screen.StudentHomeScreen,
                                             "{},{}".format(self.emp_id, student_id))
                else:
                    tk.messagebox.showerror("Student ID Not Found",
                                            "Please check the entered ID and try again.")
                    return

    def log_out(self):
        '''Logs the employee out.'''
        self.master.switch_frame(login_screen.LoginScreen)
