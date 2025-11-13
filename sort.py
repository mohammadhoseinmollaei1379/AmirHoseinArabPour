names = []
while True:
    menu_1 = (
    "be barnameh ye daftarcheh ye asami khosh amadid!😊",
    "1     :     sabt karmand jadid",
    "2     :     moshahedeh ye asami karmandan sabt shodeh",
    "3     :     ekhraj karmand",
    "4     :     khorouj"
    )
    print("\n".join(menu_1))
    menu_2 = input("gozineh ye mored nazar ra vared konid :")
    if menu_2 == "1":
        num = input("shomareh ye mored nazar ra vared konid :")
        name = input("nam khod ra vared konid :")
        family = input("nam khanevedegi khod ra vared konid :")
        with open("sort.txt", "a", encoding="utf-8") as file:
                file.write((f"{num} {name} {family} \n")) 
    elif menu_2 == "2":
        try:
            with open("sort.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
                print("\n".join(lines))
                lines.sort() 
        except FileNotFoundError:
             print("hanouz faily sakhte nashodeh!")
    elif menu_2 == "3":
            with open("sort.txt", "r", encoding="utf-8") as file:
                lines = file.readlines() 
                print("\n".join(lines))
            rem = input("shomareh ye karmand ekhraj shode ra vared konid :")
            rem_line = [line for line in lines if line.split()[0] != rem]
            with open("sort.txt", "w", encoding="utf-8") as file:
                file.writelines(rem_line)
                lines.sort()
    elif menu_2 == "4":
        break
    elif menu_2 == "":
        pass
    else:
         break