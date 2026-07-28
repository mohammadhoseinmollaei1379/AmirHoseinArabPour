name = input("name: ")
E_Mail = input("E-Mail: ")
password = input("Password: ")
age_date = input("age and date: ")
phone = input("Phone: ")
a = input("a: ")



with open("pack.json", "w", encoding="ascii") as file:
    file.writable(name)
    file.writable(E_Mail)
    file.writable(password)
    file.writable(age_date)
    file.writable(phone)
    file.writable(a)