import random
name = input("lotfan nam khod ra vared konid : ")
while True:
    input_ = input(">>>")
    if input_ == "salam" or input_ == "salam!" or input_ == "سلام" or input_ == "سلام!":
        rand = random.randint(1, 4)
        if rand == 1:
            print(f"salam {name} jan!az didar ba to khoshhalam!😊")
        elif rand == 2:
            print(f"salam {name} aziz!moshtagh didaret boodam!amade am ta az man soal beporsi😁")
        elif rand == 3:
            print(f"salam {name} jan!bia ba ham ye safar elmi ro shrooe konim!🚀")
        elif rand == 4:
            print(f"salam {name} jan!khorsandam az didar emrooz ba to! che soali azam dary?")
# import tkinter as tk
# root = tk.Tk()
# root.title("هوش مصنوعی امیر")
# root.resizable(False, False)
# root.geometry("500x500+700+175")
# root.mainloop()