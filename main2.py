from tkinter import *

import numpy as np

name = ["Carlos", "Jose", "Fernando", "Richard", "Santiago", "Andres", "Paul", "Jairo", "Pablo", "Juan", "Charlie",
        "Leo", "Pedro", "Jorge", "Damian", "Lucifer", "Zahian", "Marcos", "Steven", "Romeo"]

prob = [0.19, 0.11, 0.095, 0.1, 0.1, 0.09, 0.06, 0.05, 0.04, 0.03, 0.025, 0.02, 0.015, 0.012, 0.01, 0.008, 0.007, 0.006,
        0.0055, 0.0265]
draft_n = 5


def set_label_frame(ltxt):
    labelframe = LabelFrame(Frame, text="Draft results", justify="LEFT", fg="white", background="black", borderwidth=15)
    labelframe.pack(side="bottom", fill="both", expand=True)

    text1 = Label(labelframe, text=ltxt, fg="white", background="black")
    text1.place(relx=0.5, rely=0.5, anchor=E)
    text1.pack()


def get_draft(n):
    draft = np.random.choice(name, n, prob)
    print(draft)


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    """    def get_draft(n):
            draft = np.random.choice(name, n, prob)
            print(draft)
            wd.init_window().set_label_frame(draft)
"""

    def init_window(self):
        self.master.title("Everyday Heroes")
        self.pack(fill=BOTH, expand=1)
        set_label_frame("initial text")

    def set_buttons(self):
        button_frame = LabelFrame(self, text="Name selector", labelanchor="n")
        button_frame.pack(side="top", fill="x")
        clear_button = Button(button_frame, height=1, width=5, text="Clear")
        clear_button.pack(side="left")
        draft_button = Button(button_frame, height=1, width=5, text="Draft", command=get_draft(draft_n))
        draft_button.pack(side="left")
        quit_button = Button(button_frame, height=1, width=5, text="Exit", command=exit)
        quit_button.pack(side="right")


"""
        def set_label_frame(ltxt):
            labelframe = LabelFrame(self, text="Draft results", fg="white", background="black", borderwidth=15)
            labelframe.pack(side="bottom", fill="both", expand=True)

            text1 = Label(labelframe, text=ltxt, fg="white", background="black")
            text1.place(relx=0.5, rely=0.5, anchor=E)
            text1.pack()
"""

if __name__ == "__main__":
    root = Tk()
    root.geometry("600x400")
    app = Window(root)
    root.mainloop()
