import os
from colorama import init, Fore, Style
print("new shell [version 1.0] \nname corporation")
name_prompt = input("Please enter your prompt name :")
y = 0
while y == 0:
    user_input = input(f"C:\\{name_prompt}>")
    if user_input == "halt" or user_input == "shut down" or user_input == "khamoosh" or user_input == "shutdown" or user_input == "kamosh" or user_input == "poweroff" or user_input == "off":
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
            print(Style.RESET_ALL + f"Sorry, this {color} is not supported.")
    elif user_input == "dir" or user_input == "is" or user_input == "Is":
        path = input("Please enter the directory name :")
        files = dirs = 0
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    files += 1
                elif entry.is_dir():
                    dirs += 1
        print(f"folders :{files}, files :{dirs}")
    elif user_input == "Game" or user_input == "game" or user_input == "bazi" or user_input == "bazy":
        pass
    elif user_input.startswith("echo "):
        print(user_input[5:])
        if user_input == "echo":
            print()
        