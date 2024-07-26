import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    int1 = random.randint(1, 6)
    int2 = random.randint(1, 6)
    int3 = random.randint(1, 6)
    int4 = random.randint(1, 6)
    int5 = random.randint(1, 6)
    int6 = random.randint(1, 6)
    simpledialog.askstring(title='lottery', prompt=str(int1)+str(int2)+str(int3)+str(int4)+str(int5)+str(int6))
    # TODO 2) Display the selected numbers to the user in a pop-up

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
