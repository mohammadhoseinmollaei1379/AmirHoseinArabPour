import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.geometry("600x600+700+200")
root.configure(bg="light green")
root.resizable(False, False)

root.title("سنگ کاغد قیچی")
score_bot = 0
score_gmr = 0
label = tk.Label(root, text="گزینه ی مورد نظر خود را وارد کنید", font=("B Nazanin", 26), bg="light green")
label.pack()

#مربوط به گذاشتن تصویر

entry = tk.Entry(root, font=("B Nazanin", 24))
entry.pack()

def sabt():
    content = entry.get().strip()

    bot = random.randint(1, 3)
    if bot == 1:
        bot = "سنگ"
    elif bot == 2:
        bot = "کاغذ"
    elif bot == 3:
        bot = "قیچی"
    elif content == "سنگ" and bot == "سنگ":
        score_bot = score_bot
        score_gmr = score_gmr
        msg = messagebox.showinfo("مساوی", "مساوی")
    elif content == "سنگ" and bot == "کاغذ":
        score_bot += 1
        score_gmr = score_gmr
        msg = messagebox.showinfo("ربات برد", "ربات برد")
    elif content == "سنگ" and bot == "قیچی":
        score_bot = score_bot
        score_gmr += 1
        msg = messagebox.showinfo("بازیکن برد", "بازیکن برد")
    elif content == "کاغذ" and bot == "سنگ":
        score_bot = score_bot
        score_gmr += 1
        msg = messagebox.showinfo("بازیکن برد", "بازیکن برد")
    elif content == "کاغذ" and bot == "کاغذ":
        score_bot = score_bot
        score_gmr = score_gmr
        msg = messagebox.showinfo("مساوی", "مساوی")
    elif content == "کاغذ" and bot == "قیچی":
        score_bot += 1
        score_gmr = score_gmr
        msg = messagebox.showinfo("ربات برد", "ربات برد")
    elif content == "قیچی" and bot == "سنگ":
        score_bot += 1
        score_gmr = score_gmr
        msg = messagebox.showinfo("ربات برد", "ربات برد")
    elif content == "قیچی" and bot == "کاغذ":
        score_bot = score_bot
        score_gmr += 1
        msg = messagebox.showinfo("ربات برد", "ربات برد")
    elif content == "قیچی" and bot == "قیچی":
        score_bot = score_bot
        score_gmr = score_gmr
        msg = messagebox.showinfo("مساوی", "مساوی")
    elif score_bot == 3:
        msg = messagebox.showinfo("برنده نهایی", "ربات برنده ی نهایی شد")
    elif score_gmr == 3:
        msg = messagebox.showinfo("برنده نهایی", "بازیکن برنده ی نهایی شد")

btn = tk.Button(root, text="تایید", font=("B Nazanin", 18),  command=sabt, width=22)
btn.pack()

root.mainloop()