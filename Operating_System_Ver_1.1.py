import os
from colorama import init, Fore, Style
import shutil
import datetime
print("Starting New-Shell... [Version 1.1]")
name_prompt = input("Please enter your prompt name :")
Ver = "1.1"
y = 0
while y == 0:
    user_input = input(f"C:\\{name_prompt}>")
    user_input = user_input.lower()
    user_input = user_input.replace(" ", "")
    user_input = user_input.replace("-", "")
    if user_input == "halt" or user_input == "shutdown" or user_input == "poweroff" or user_input == "off":
        print("See you later...")
        break
    elif user_input == "cls" or user_input == "clear" or user_input == "clearscreen" or user_input == "clr":
        os.system("cls")
    elif user_input == "color":
        init()
        color = user_input[4:]
        if color == "1":
            print(Fore.BLUE + "This is blue text")
            os.system("cls")
        elif color == "2":
            print(Fore.GREEN + "This is green text")
            os.system("cls")
        elif color == "3":
            print(Fore.CYAN + "This is aqua text")
            os.system("cls")
        elif color == "4":
            print(Fore.RED + "This is red text")
            os.system("cls")
        elif color == "5":
            print(Fore.MAGENTA + "This is purple text")
            os.system("cls")
        elif color == "6":
            print(Fore.YELLOW + "This is yellow text")
            os.system("cls")
        elif color == "7" or color == "reset":
            print(Style.RESET_ALL + "This is white text")
            os.system("cls")
        elif color == "9":
            print(Fore.LIGHTBLUE_EX + "This is light blue text")
            os.system("cls")
        elif color == "a":
            print(Fore.LIGHTGREEN_EX + "This is light green text")
            os.system("cls")
        elif color == "b":
            print(Fore.LIGHTCYAN_EX + "This is light aqua text")
            os.system("cls")
        elif color == "c":
            print(Fore.LIGHTRED_EX + "This is light red text")
            os.system("cls")
        elif color == "d":
            print(Fore.LIGHTMAGENTA_EX + "This is light purple text")
            os.system("cls")
        elif color == "e":
            print(Fore.LIGHTYELLOW_EX + "This is light purple text")
            os.system("cls")
        elif color == "f":
            print(Fore.LIGHTWHITE_EX + "This is bright white text")
        else:
            print(Style.RESET_ALL + f"Sorry, this {color} is not supported.")
            os.system("cls")
    elif user_input == "dir" or user_input == "ls":
        path = input("Please enter the directory name :")
        files = dirs = 0
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    files += 1
                elif entry.is_dir():
                    dirs += 1
        print(f"folders :{files}, files :{dirs}")
    elif user_input.startswith("echo"):
        print(user_input[4:])
        print()
        user_input.lower()
    elif user_input == "copycon":
        input_1 = input()
        print(input_1)
    elif user_input == "rd" or user_input == "rm" or user_input == "removeitem" or user_input == "del":
        folder_path = input("Please enter the directory or file name :")
        if os.path.exists(folder_path):
            confirm = input(f"Are you sure you want to delete the folder '{folder_path}'? (Y/N): ").strip().lower()
            if confirm == "y":
                shutil.rmtree(folder_path)
                print("Folder deleted successfully.")
            else:
                print("Deletion canceled.")
        else:
            print("Folder does not exist.")
    elif user_input == "newprompt" or user_input == "prompt" or user_input == "nameprompt":
        name_prompt = input("Please enter your new prompt name :")
    elif user_input == "":
        pass
    elif user_input == "ver" or user_input == "version":
        print(Ver)
    elif user_input == "time":
        now = datetime.datetime.now().time()
        print("The current time is :", now)
    elif user_input == "date":
        now = datetime.date.today()
        print("The current date is :", now)
    elif user_input == "mkdir":
        name_folder = user_input[5:]
        os.mkdir(name_folder)
        print("Folder created")
    elif user_input == "help":
        user_input_1 = user_input[3:]
        if user_input_1 == "color":
            print(
                "1 = Blue",               "9 = Light Blue",
                "2 = Green",              "A = Light Green",
                "3 = Aqua",               "B = Light Aqua",
                "4 = Red",                "C = Light Red",
                "5 = Purple",             "D = Light Purple",
                "6 = Yellow",             "E = Light Yellow",
                "7 = White",              "F = Bright White ")
    else:
        print("Command not found. please try 'Help'")