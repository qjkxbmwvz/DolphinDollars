'''A container for the various screens of the program.'''

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import mysql.connector


class MainWindow(tk.Tk):
    '''The main window.'''
    def __init__(self, frame_class):
        tk.Tk.__init__(self)

        db_ = mysql.connector.connect(
            host="brettmusser.cikeys.com",
            user="brettmus_StephenBerks",
            passwd="k,4i17Xl@]HG",
            database="brettmus_COMP420_DolphinDollarsProject"
        )

        self.cursor = db_.cursor()

        self.geometry("600x450+650+150")
        self.minsize(1, 1)
        self.maxsize(1665, 1020)
        self.resizable(0, 0)
        self.configure(background="#ffffff")
        self.frame = None
        self.switch_frame(frame_class)
        self.mainloop()

    def switch_frame(self, frame_class, string_to_pass=None):
        '''Switches from one screen to another.'''
        new_frame = frame_class(self, string_to_pass) if string_to_pass is not None else \
                    frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def execute(self, command):
        '''Executes an SQL command.'''
        self.cursor.execute(command)
        return self.cursor
