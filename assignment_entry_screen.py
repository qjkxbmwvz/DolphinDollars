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
    def __init__(self, master, ids):
        tk.Frame.__init__(self, master)

        [self.emp_id, self.student_id] = ids.split(",")
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
        label_3.place(relx=0.25, rely=0.333, anchor="e")
        label_3.configure(background="#ffffff", justify='right', text='''Assignment Date:''')

        label_4 = tk.Label(self)
        label_4.place(relx=0.25, rely=0.455, anchor="e")
        label_4.configure(background="#ffffff", justify='right', text='''Assignment Size:''')

        label_5 = tk.Label(self)
        label_5.place(relx=0.25, rely=0.58, anchor="e")
        label_5.configure(background="#ffffff", justify='right', text='''Assignment Grade:''')

        label_6 = tk.Label(self)
        label_6.place(relx=0.25, rely=0.705, anchor="e")
        label_6.configure(background="#ffffff", justify='right', text='''Course:''')

        self.cal = DateEntry(self, background='#ed1c24',
                             foreground='white', borderwidth=2)
        self.cal.place(relx=0.4, rely=0.333, anchor="center")

        self.size_choice = tk.StringVar(self)
        self.size_choice.set("small")
        size_choices = ["small", "medium", "large"]
        size_menu = tk.OptionMenu(self, self.size_choice, *size_choices)
        size_menu.place(relx=0.4, rely=0.455, width=115, anchor="center")
        size_menu.configure(background='#ed1c24')

        self.grade_choice = tk.StringVar(self)
        self.grade_choice.set("a")
        grade_choices = ["a", "b", "c", "d", "f"]
        grade_menu = tk.OptionMenu(self, self.grade_choice, *grade_choices)
        grade_menu.place(relx=0.4, rely=0.58, width=115, anchor="center")
        grade_menu.configure(background='#ed1c24')

        self.course_code_entry = tk.Entry(self)
        self.course_code_entry.place(relx=0.4, rely=0.705, height=23, width=115, anchor="center")
        self.course_code_entry.configure(background="white", font="TkFixedFont")

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
        grade = self.grade_choice.get()
        date = self.cal.get()
        size = self.size_choice.get()
        course = self.course_code_entry.get()

        if not course:
            tk.messagebox.showerror("Form Incomplete", "Please fill in all fields.")
            return

        cursor = self.master.execute("SELECT ValidateCourse('{}');".format(course))

        for i in cursor:
            for j in i:
                if j == 1:
                    print("CALL AssignmentDeposit('{}', STR_TO_DATE('{}', '%m/%d/%Y'), '{}', '{}', {}, {})"
                          .format(grade, date, size, course, self.student_id, self.emp_id))
                    self.master.execute(
                        "CALL AssignmentDeposit('{}', STR_TO_DATE('{}', '%m/%d/%Y'), '{}', '{}', {}, {})"
                        .format(grade, date, size, course, self.student_id, self.emp_id))
                    self.master.switch_frame(student_home_screen.StudentHomeScreen,
                                             "{},{}".format(self.emp_id, self.student_id))
                else:
                    tk.messagebox.showerror("Course Code Not Found",
                                            "Please check the entered course code and try again.")
                    return

    def go_back(self):
        '''Returns to the student home screen.'''
        self.master.switch_frame(student_home_screen.StudentHomeScreen,
                                 "{},{}".format(self.emp_id, self.student_id))
