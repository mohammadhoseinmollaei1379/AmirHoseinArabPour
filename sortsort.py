import tkinter as tk
root = tk.Tk()
root.title("مرتب کردن اسامی کارمندان")
root.geometry("800x600+600+200")
label = tk.Label(root, text="""به برنامۀ دفترچۀ اسامی خوش آمدید😊
    1     :                         ثبت کارمند جدید
    2     :     مشاهدۀ اسامی کارمندان ثبت شده
    3     :                               اخراج کارمند
    4     :                             خروج از برنامه
    گزینۀ مناسب را وارد کنید""", font=("B Nazanin", 18))
label.pack()
entry = tk.Entry(root, width=20, font=("B Titr", 20))
entry.pack()
def click():
    content = entry.get().strip()
    if content == "1":
        root_1 = tk.Toplevel(root)
        root_1.title("ثبت کارمند جدید")
        root_1.geometry("600x400+1000+450")
        label_1 = tk.Label(root_1, text="نام و نام خانوادگی کارمند جدید را وارد کنید", font=("B Nazanin", 18))
        label_1.pack()
        entry_1 = tk.Entry(root_1, width=20, font=("B Nazanin", 20))
        entry_1.pack()
        def save_name():
            content_1 = entry_1.get().strip()
            if content_1 != "8":
                with open("sort.txt", "a", encoding="utf-8") as file:
                    file.write(f"{content_1} \n")
            else:
                root_1.destroy()
        btn_1 = tk.Button(root_1, text="ثبت نام", bg="lightyellow", font=("B Titr", 18), command=save_name)
        btn_1.pack()
        label_1_1 = tk.Label(root_1, text="در صورت خروج عدد 8 را وارد کنید", font=("B Nazanin", 18))
        label_1_1.pack()
btn = tk.Button(root, text="ثبت", bg="lightyellow", font=("B Titr", 18), command=click)
btn.pack()
root.mainloop()