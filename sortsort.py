import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.title("مرتب کردن اسامی کارمندان")
root.geometry("375x375+750+225")
root.resizable(False, False)
root.configure(bg="lightblue")
label = tk.Label(root, text="""به برنامۀ دفترچۀ اسامی خوش آمدید
    1     :                         ثبت کارمند جدید
    2     :     مشاهدۀ اسامی کارمندان ثبت شده
    3     :                               اخراج کارمند
    گزینۀ مناسب را وارد کنید""", font=("B Nazanin", 18), bg="lightblue")
label.pack()
entry = tk.Entry(root, width=20, font=("B Titr", 20))
entry.pack()
def click():
    content = entry.get().strip()
    if content == "1":
        root_1 = tk.Toplevel(root)
        root_1.title("ثبت کارمند جدید")
        root_1.geometry("350x275+762+250")
        root_1.resizable(False, False)
        root_1.configure(bg="lightblue")
        label_1 = tk.Label(root_1, text="نام و نام خانوادگی کارمند جدید را وارد کنید", font=("B Nazanin", 18), bg="lightblue")
        label_1.pack()
        entry_1 = tk.Entry(root_1, width=20, font=("B Nazanin", 20))
        entry_1.pack()
        def save_name():
            content_1 = entry_1.get().strip()
            if content_1:
                with open("sort.txt", "a", encoding="utf-8") as file:
                    file.write(f"{content_1} \n")
        def exit_1():
            root_1.destroy()
        btn_1 = tk.Button(root_1, text="ثبت نام", bg="lightyellow", font=("B Titr", 18), command=save_name)
        btn_1.pack()
        btn_1_1 = tk.Button(root_1, text="خروج", bg="lightyellow", font=("B Titr", 18), command=exit_1, width=600)
        btn_1_1.pack()
    elif content == "2":
        root_2 = tk.Toplevel(root)
        root_2.title("مشاهدۀ اسامی کارمندان ثبت شده")
        root_2.geometry("600x400+1000+450")
        root_2.resizable(False, False)
        root_2.configure(bg="lightblue")
        label_2 = tk.Label(root_2, text="برای دیدن اسامی کارمندان ثبت شده، دکمۀ زیر را کلیک کنید", font=("B Nazanin", 18), bg="lightblue")
        label_2.pack()
        def show_names():
            file_path_1 = filedialog.askopenfilename(filetypes=[("Textfile", "sort.txt")])
            if file_path_1:
                with open("sort.txt", "r", encoding="utf-8") as file:
                    file_1 = file.read()
                    txt_wgt.insert(tk.END, file_1)
        btn_2 = tk.Button(root_2, text="مشاهده", bg="lightyellow", font=("B Titr", 18), command=show_names)
        btn_2.pack()
        def exit_2():
            root_2.destroy()
        txt_wgt = tk.Text(root_2, wrap="word", width=50, height=10)
        txt_wgt.pack(padx=10, pady=10)
        btn_2_1 = tk.Button(root_2, text="خروج", bg="lightyellow", font=("B Titr", 18), command=exit_2, width=600)
        btn_2_1.pack()
btn = tk.Button(root, text="ثبت", bg="lightyellow", font=("B Titr", 18), command=click)
btn.pack()
def exit():
    root.destroy()
btn_1 = tk.Button(root, text="خروج", bg="lightyellow", font=("B Titr", 18), command=exit, padx=100)
btn_1.pack()
root.mainloop()