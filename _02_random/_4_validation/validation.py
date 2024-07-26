import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)
    print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment
    for i in range(10):
        random_number = random.randint(1, 5)
        print(random_number)
        if random_number == 1:
            simpledialog.askstring(title='title', prompt="something nice")
        if random_number == 2:
            simpledialog.askstring(title='title', prompt="something nicer")
        if random_number == 3:
            simpledialog.askstring(title='title', prompt="something nicest")
        if random_number == 4:
            simpledialog.askstring(title='title', prompt="something mean")
    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
