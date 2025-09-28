import os
from colorama import init, Fore, Style
import shutil
import datetime
Ver = "1.1"
print("Starting New-Shell... [Version 1.1]")
name_prompt = input("Please enter your prompt name :")
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
        color = input("Please enter your desired color(red, green, blue, yellow, white) :")
        if color == "red":
            print(Fore.RED + "This is red text")
            os.system("cls")
        elif color == "green":
            print(Fore.GREEN + "This is green text")
            os.system("cls")
        elif color == "blue":
            print(Fore.BLUE + "This is blue text")
            os.system("cls")
        elif color == "yellow":
            print(Fore.YELLOW + "This is yellow text")
            os.system("cls")
        elif color == "white":
            print(Style.RESET_ALL + "This is white text")
            os.system("cls")
        else:
            print(Style.RESET_ALL + f"Sorry, this {color} is not supported.")
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
    elif user_input == "echo ":
        print(user_input[5:])
        if user_input == "echo":
            print()
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
    else:
        print(f"Command not found. please try 'Help'")