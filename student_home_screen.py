#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.3
#  in conjunction with Tcl version 8.6
#    May 21, 2020 11:42:39 PM PDT  platform: Linux

'''The student home screen.'''

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import student_entry_screen
import assignment_entry_screen


class StudentHomeScreen(tk.Frame):
    '''This class populates the window with student home screen stuff.'''
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.configure(bg="white")

        font10 = "-family {Noto Sans} -size 18"
        font9 = "-family {Noto Sans} -size 24"

        master.title("Dolphin Dollars Student Home")

        label_1 = tk.Label(self)
        label_1.place(relx=0.5, rely=0.067, anchor="center")
        label_1.configure(background="#ffffff", cursor="fleur", disabledforeground="#ffffff",
                          font=font9, foreground="#ed1c24", text='''Dolphin Dollars''')

        label_2 = tk.Label(self)
        label_2.place(relx=0.5, rely=0.178, anchor="center")
        label_2.configure(background="#ffffff", cursor="fleur",
                          font=font10, text='''Student Home''')

        self.assignment_button = tk.Button(self)
        self.assignment_button.place(relx=0.5, rely=0.333, height=50, width=150, anchor="center")
        self.assignment_button.configure(background="#ed1c24", foreground="#ffffff",
                                         text='''Submit Assignment''', command=self.assignment)

        self.voucher_button = tk.Button(self)
        self.voucher_button.place(relx=0.5, rely=0.5, height=50, width=150, anchor="center")
        self.voucher_button.configure(background="#ed1c24", foreground="#ffffff",
                               text='''Deposit Study Session Voucher''', wraplength="125")

        self.prize_button = tk.Button(self)
        self.prize_button.place(relx=0.5, rely=0.667, height=50, width=150, anchor="center")
        self.prize_button.configure(background="#ed1c24", foreground="#ffffff",
                               text='''Redeem for Prizes''')

        self.back_button = tk.Button(self)
        self.back_button.place(relx=0.5, rely=0.833, height=50, width=150, anchor="center")
        self.back_button.configure(background="#ed1c24", foreground="#ffffff",
                               text='''Done''', command=self.go_back)

    def assignment(self):
        '''Goes to the assignment submission screen.'''
        self.master.switch_frame(assignment_entry_screen.AssignmentEntryScreen)

    def go_back(self):
        '''Returns to the student entry screen.'''
        self.master.switch_frame(student_entry_screen.StudentEntryScreen)
