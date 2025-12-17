import tkinter as tk
from tkinter import messagebox
ascii_table = {"A" : 65, "B" : 66, "C" : 67, "D" : 68, "E" : 69, "F" : 70}
def sign():
    content_1 = entry_1.get().strip()
    if content_1 in ascii_table:
        for i in ascii_table:
            if i == content_1:
                l = ascii_table[i]
                msg_box = messagebox.showinfo(f"{i}", f"{l}")
root = tk.Tk()
root.title("تبدیل کاراکتر به عدد باینری")
root.geometry("400x600+600+150")
root.resizable(False, False)
root.configure(bg="lightblue")
label_1 = tk.Label(root, text="لطفا کاراکتر مناسب را وارد کنید", bg="lightblue", font=("B Nazanin", 20))
label_1.pack()
entry_1 = tk.Entry(root, font=("SimSun", 18))
entry_1.pack()
button_1 = tk.Button(root, text="وارد", font=("B Titr", 26), bg="lightblue", command=sign, width=100)
button_1.pack()
root.mainloop()