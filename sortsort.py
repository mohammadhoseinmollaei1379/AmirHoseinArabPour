import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
pass_word_ = "123456"
root_4 = tk.Tk()
root_4.geometry("200x150+900+200")
root_4.configure(bg="lightblue")
root_4.title("ورود به برنامه")
root_4.resizable(False, False)
label_4 = tk.Label(root_4, text="رمز خود را وارد کنید", font=("B Nazanin", 18), bg="lightblue")
label_4.pack()
entry_4 = tk.Entry(root_4, width=75, font=("B Nazanin", 18))
entry_4.pack()
def sign_in():
    content_5 = entry_4.get().strip()
    if content_5 == pass_word_:
        return pass_word()
    else:
        msg_box = messagebox.showinfo("خطا!", "رمز عبور اشتباه است!")
        root_4.destroy()
def pass_word():
    content_4 = entry_4.get()
    if content_4 == pass_word_:
        root_4.withdraw()
        root = tk.Toplevel()
        root.title("دفترچۀ اسامی")
        root.geometry("410x375+750+225")
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
                root_1.geometry("350x225+1000+450")
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
                            file.write(f"\n {content_1} \n")
                            msg_box = messagebox.showinfo("ثبت شد!", "ثبت نام با موفقیت انجام شد!")
                def exit_1():
                    root_1.destroy()
                btn_1 = tk.Button(root_1, text="ثبت نام", bg="lightyellow", font=("B Titr", 18), command=save_name, width=600)
                btn_1.pack()
                btn_1_1 = tk.Button(root_1, text="خروج", bg="lightyellow", font=("B Titr", 18), command=exit_1, width=600)
                btn_1_1.pack()
            elif content == "2":
                root_2 = tk.Toplevel(root)
                root_2.title("مشاهدۀ اسامی کارمندان ثبت شده")
                root_2.geometry("475x370+1000+450")
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
                btn_2 = tk.Button(root_2, text="مشاهده", bg="lightyellow", font=("B Titr", 18), command=show_names, width=600)
                btn_2.pack()
                def exit_2():
                    root_2.destroy()
                txt_wgt = tk.Text(root_2, wrap="word", width=50, height=10)
                txt_wgt.pack(padx=10, pady=10)
                btn_2_1 = tk.Button(root_2, text="خروج", bg="lightyellow", font=("B Titr", 18), command=exit_2, width=600)
                btn_2_1.pack()
            elif content == "3": 
                root_3 = tk.Toplevel(root)
                root_3.title("اخراج کارمند")
                root_3.geometry("380x225+1000+450")
                root_3.resizable(False, False)
                root_3.configure(bg="lightblue")
                label_3 = tk.Label(root_3, text="نام و نام خانوادگی کارمند اخراج شده را وارد کنید", font=("B Nazanin", 18), bg="lightblue")
                label_3.pack()
                entry_3 = tk.Entry(root_3, width=40, font=("B Nazanin", 20))
                entry_3.pack()
                def delete_name():
                    with open("sort.txt", "r", encoding="utf-8") as file:
                        lines = file.readlines()
                    content_1 = entry_3.get().strip()
                    rem_line = [line for line in lines if line.strip() != content_1]
                    with open("sort.txt", "w", encoding="utf-8") as file:
                        file.writelines(rem_line)
                        lines.sort()
                        msg_box = messagebox.showinfo("اخراج شد!", "کارمند با موفقیت اخراج شد!")
                btn_3 = tk.Button(root_3, text="اخراج", bg="lightyellow", font=("B Titr", 18), command=delete_name, width=600)
                btn_3.pack()
                def exit_3():
                    root_3.destroy()
                btn_3_1 = tk.Button(root_3, text="خروج", bg="lightyellow", font=("B Titr", 18), command=exit_3, width=600)
                btn_3_1.pack()
        btn = tk.Button(root, text="ثبت", bg="lightyellow", font=("B Titr", 18), command=click, width=600)
        btn.pack()
        def exit():
            root.destroy()
            root_4.destroy()
        btn_1 = tk.Button(root, text="خروج", bg="lightyellow", font=("B Titr", 18), command=exit, width=600)
        btn_1.pack()
        root.mainloop()
    else:
        msg_box = messagebox.showinfo("خطا!", "رمز عبور اشتباه است!")
        root_4.destroy()
btn_4 = tk.Button(root_4, text="ورود", bg="lightyellow", font=("B Titr", 20), width=600, command=pass_word)
btn_4.pack()
root_4.mainloop()