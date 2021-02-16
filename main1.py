from tkinter import *

import numpy as np

name = ["Carlos", "Jose", "Fernando", "Richard", "Santiago", "Andres", "Paul", "Jairo", "Pablo", "Juan", "Charlie",
        "Leo", "Pedro", "Jorge", "Damian", "Lucifer", "Zahian", "Marcos", "Steven", "Romeo"]

prob = [0.19, 0.11, 0.095, 0.1, 0.1, 0.09, 0.06, 0.05, 0.04, 0.03, 0.025, 0.02, 0.015, 0.012, 0.01, 0.008, 0.007, 0.006,
        0.0055, 0.0265]


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def set_label_frame(self, ltxt):
        labelframe = LabelFrame(self, text="Draft results", fg="white", background="black", borderwidth=15)
        labelframe.pack(side="bottom", fill="both", expand=True)

        text1 = Label(labelframe, text=ltxt, fg="white", background="black")
        text1.place(relx=0.5, rely=0.5, anchor=E)
        text1.pack()

    def init_window(self):
        self.master.title("Everyday Heroes")
        self.pack(fill=BOTH, expand=1)

        draft_n = 5

        def set_buttons():
            button_frame = LabelFrame(self, text="Name selector", labelanchor="n")
            # Button frame pack
            button_frame.pack(side="top", fill="x")

            # creating a button instance
            clear_button = Button(button_frame, height=1, width=5, text="Clear")

            # placing the button on my window
            clear_button.pack(side="left")

            # creating a button instance
            draft_button = Button(button_frame, height=1, width=5, text="Draft", command=get_draft(draft_n))

            # placing the button on my window
            draft_button.pack(side="left")

            # creating a button instance
            quit_button = Button(button_frame, height=1, width=5, text="Exit", command=exit)

            # placing the button on my window
            quit_button.pack(side="right")


"""
        def set_label_frame(ltxt):
            labelframe = LabelFrame(self, text="Draft results", fg="white", background="black", borderwidth=15)
            labelframe.pack(side="bottom", fill="both", expand=True)

            text1 = Label(labelframe, text=ltxt, fg="white", background="black")
            text1.place(relx=0.5, rely=0.5, anchor=E)
            text1.pack()
"""


def get_draft(n):
    draft = np.random.choice(name, n, prob)
    print(draft)
    Window.set_label_frame(draft)


Window.init_window().set_label_frame("initial text")

root = Tk()
root.geometry("600x400")
app = Window(root)
root.mainloop()
