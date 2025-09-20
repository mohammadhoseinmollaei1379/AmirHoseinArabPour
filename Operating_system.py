import os
from colorama import init, Fore, Style
print("""name [version 1.0]
    name corporation""")
name_prompt = input("Please enter your prompt name :")
y = 0
while y == 0:
    user_input = input(f"C:\\{name_prompt}>")
    if user_input == "halt" or user_input == "shut down" or user_input == "khamoosh" or user_input == "shutdown":
        print("""See you later...""")
        break
    elif user_input == "cls" or user_input == "clear" or user_input == "pak" or user_input == "pac":
        os.system("cls")
    elif user_input == "color" or user_input == "colors" or user_input == "rang":
        init()
        color = input("Please enter your desired color(red, green, blue, yellow, reset) :")
        if color == "red":
            print(Fore.RED + "This is red text")
        elif color == "green":
            print(Fore.GREEN + "This is green text")
        elif color == "blue":
            print(Fore.BLUE + "This is blue text")
        elif color == "yellow":
            print(Fore.YELLOW + "This is yellow text")
        elif color == "reset":
            print(Style.RESET_ALL + "This is reset text")
        else:
            print(Style.RESET_ALL + "Sorry, this color is not supported.")