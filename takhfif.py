import tkinter as tk
import os
from openpyxl import Workbook, load_workbook
root = tk.Tk()

label = tk.Label(root, text="لطفا نام و نام خانوادگی خود را وارد کنید", bg="lightgreen", fg="red", font=("B Titr", 18))
label.pack()

entry_1 = tk.Entry(root, width=50, font=("B Nazanin", 20))
entry_1.pack(pady=2)

label = tk.Label(root, text="لطفا شماره خود را وارد کنید", bg="lightgreen", fg="red", font=("B Titr", 18))
label.pack()

entry_2 = tk.Entry(root, width=25, font=("B Nazanin", 20))
entry_2.pack(pady=2)

label = tk.Label(root, text="اینجا هم تأیید کنید که مشتری ثابت هستید یا مشتری گذری", bg="lightgreen", fg="red", font=("B Titr", 18))
label.pack()

rad_btn = tk.StringVar()
rb_1 = tk.Radiobutton(root, text="مشتری ثابت", variable=rad_btn, value="مشتری ثابت")
rb_2 = tk.Radiobutton(root, text="مشتری گذری", variable=rad_btn, value="مشتری گذری")
rb_1.pack()
rb_2.pack()

def click():
    content_1 = entry_1.get()
    content_2 = entry_2.get()
    selected_rd_btn = rad_btn.get()
    wb = Workbook()
    ws = wb.active
    try:
        name, family_1, family_2 = content_1.split()
        ws.append([name, family_1, family_2, content_2, selected_rd_btn])
        wb.save("takhfif.xlsx")
    except ValueError:
        error_label = tk.Label(root, text="ورودی باید شامل نام، نام خانوادگی و شماره تلفن باشد.", fg="red", bg="lightblue", font=("B Nazanin", 14))
        error_label.pack()


button = tk.Button(root, text="ثبت نام",bg="lightyellow", font=("B Titr", 18), command=click)
button.pack()

root.title("برنامه جامع مشتری")

root.geometry("1000x800+400+100")

root.resizable(False, False)

root.configure(bg="lightblue")

root.mainloop()