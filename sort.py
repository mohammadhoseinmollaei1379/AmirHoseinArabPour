names = []
while True:
    menu_1 = (
    "be barnameh daftarcheh asami khosh amadid! 😊",
    "1     :     voroud nam jadid",
    "2     :     didan asami sabt shode",
    "3     :     khorouj az list"
    )
    print("\n".join(menu_1))
    menu_2 = int(input("gozinehg monaseb ra vared konid: "))
    if menu_2 == 1:
        name = input("nam khod ra vared konid: ")
        family = input("nam khanevadegi khod ra vared konid: ")
        names.append((name, family))
        with open("sort.txt", "a", encoding="utf-8") as file:
            for name, family in names:
                file.write((f"{name} {family}\n"))
    elif menu_2 == 2:
        with open("sort.txt", "r", encoding="utf-8") as file:
            lines = file.read()
            sorted(lines)
            print(lines)
    elif menu_2 == 3:
        break