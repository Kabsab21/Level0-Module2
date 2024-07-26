import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    simpledialog.askstring(title='title', prompt="i don't know write something")
    # Make a variable and initialize it to a random number between 0 and 3
    var = random.randint(0, 3)
    # If the random number is 0
    if var == 0:
        simpledialog.askstring(title='title', prompt="yes!")

        # tell the user "Yes"

    # If the random number is 1
    if var == 1:
        simpledialog.askstring(title='title', prompt="no!")
        # tell the user "No"

    # If the random number is 2
    if var == 2:
        simpledialog.askstring(title='title', prompt="hello Sandra, it appears that your account has been blocked, to access your account again please enter your credit card information and your social security number.")
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
