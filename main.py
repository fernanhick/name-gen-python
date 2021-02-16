from tkinter import *
from tkinter import LabelFrame

import numpy as np

name = ["Carlos", "Jose", "Fernando", "Richard", "Santiago", "Andres", "Paul", "Jairo", "Pablo", "Juan", "Charlie",
        "Leo", "Pedro", "Jorge", "Damian", "Lucifer", "Zahian", "Marcos", "Steven", "Romeo"]

prob = [0.19, 0.11, 0.095, 0.1, 0.1, 0.09, 0.06, 0.05, 0.04, 0.03, 0.025, 0.02, 0.015, 0.012, 0.01, 0.008, 0.007, 0.006,
        0.0055, 0.0265]


# Here, we are creating our class , Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)


def client_exit():
    exit()


# Function to update the draft into Label widget
def get_draft(n):
    draft = np.random.choice(name, n, prob)
    Window.init_window(Window).set_text_label(draft)


class Window(Frame):
    txt = "This is first text"

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)
        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        button_frame: LabelFrame = LabelFrame(self, text="Name selector", labelanchor="n")
        # Button frame pack
        button_frame.pack(side="top", fill="x")

        # creating a button instance
        clear_button = Button(button_frame, height=1, width=5, text="Clear",
                              command=exit)

        # placing the button on my window
        clear_button.pack(side="left")

        # creating a button instance
        draft_button = Button(button_frame, height=1, width=5, text="Draft",
                              command=get_draft(5))

        # placing the button on my window
        draft_button.pack(side="left")

        # creating a button instance
        quit_button = Button(button_frame, height=1, width=5, text="Exit",
                             command=exit)

        # placing the button on my window
        quit_button.pack(side="right")

        print("before function declared")

        def set_text_label(txt):
            # Top Frame for text display
            labelframe = LabelFrame(self, text="Draft results", fg="white", background="black", borderwidth=15)
            labelframe.pack(side="bottom", fill="both", expand=True)

            text1 = Label(labelframe, text=txt, fg="white", background="black")
            text1.place(relx=0.5, rely=0.5, anchor=E)
            text1.pack()


def draft_console():
    print("Welcome to the name generator Tutorial")

    print("There is " + str(len(name)) + " names in the list")
    print("How many names do you want to draft?")
    draft_nb = input()

    print("You selected " + draft_nb + " names to be draft")

    get_draft_console(int(draft_nb))


def get_draft_console(n):
    #    Obtain the result out of the choices using a random selector
    #    this will read the list of options $name and generate a result using the probabilities table $prob

    draft = np.random.choice(name, n, prob)
    print(draft)


# function for drafting into console option


# Function to print the draft into console

root = Tk()
# root window created. Here, that would be the only window, but
# you can later have windows within windows.

root.geometry("600x400")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()
