import os
from colorama import init, Fore
import shutil
import datetime
from tqdm import tqdm
from time import sleep
for i in tqdm(range(20)):
    sleep(0.2)
print("Starting New-Shell... [Version 1.2]")
name_prompt = input("Please enter your prompt name :")
Ver = "1.2"
while True:
    user_input = input(f"C:\\{name_prompt}>")
    user_input = user_input.lower()
    user_input = user_input.replace(" ", "")
    user_input = user_input.replace("-", "")
    if user_input == "halt" or user_input == "shutdown":
        print("See you later...")
        break
    elif user_input == "cls" or user_input == "clear" or user_input == "clearscreen" or user_input == "clr":
        os.system("cls")
    elif user_input.startswith("color"):
        init()
        color = user_input[5:]
        if color == "1":
            print(Fore.BLUE + "This is blue text")
        elif color == "2":
            print(Fore.GREEN + "This is green text")
        elif color == "3":
            print(Fore.CYAN + "This is aqua text")
        elif color == "4":
            print(Fore.RED + "This is red text")
        elif color == "5":
            print(Fore.MAGENTA + "This is purple text")
        elif color == "6":
            print(Fore.YELLOW + "This is yellow text")
        elif color == "7":
            print(Fore.RESET + "This is white text")
        elif color == "9":
            print(Fore.LIGHTBLUE_EX + "This is light blue text")
        elif color == "a":
            print(Fore.LIGHTGREEN_EX + "This is light green text")
        elif color == "b":
            print(Fore.LIGHTCYAN_EX + "This is light aqua text")
        elif color == "c":
            print(Fore.LIGHTRED_EX + "This is light red text")
        elif color == "d":
            print(Fore.LIGHTMAGENTA_EX + "This is light purple text")
        elif color == "e":
            print(Fore.LIGHTYELLOW_EX + "This is light yellow text")
        elif color == "f":
            print(Fore.LIGHTWHITE_EX + "This is bright white text")
        else:
            print(Fore.WHITE + f"Sorry, this {color} is not supported.")
    elif user_input == "dir" or user_input == "ls":
        path = input("Please enter the directory name :")
        files = dirs = 0
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    files += 1
                elif entry.is_dir():
                    dirs += 1
        print(f"folders : {files}, files : {dirs}")
    elif user_input.startswith("echo"):
        print(user_input[4:])
    elif user_input == "copycon":
        input_1 = input()
        print(input_1)
    elif user_input == "rd" or user_input == "rm" or user_input == "removeitem":
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
    elif user_input.startswith("newprompt") or user_input.startswith("prompt"):
        if user_input == "newprompt":
            name_prompt = user_input[9:]
        else:
            name_prompt = user_input[6:]
    elif user_input == "":
        pass
    elif user_input == "ver" or user_input == "version":
        print(Ver)
    elif user_input == "time" or user_input == "time/t":
        time = datetime.datetime.now().time()
        print("The current time is :", time)
    elif user_input == "date":
        date = datetime.date.today()
        print("The current date is :", date)
    elif user_input.startswith("mkdir") or user_input.startswith("md"):
        name_folder = user_input[5:]
        os.mkdir(name_folder)
        print("Folder created")
    elif user_input.startswith("cd"):
        name_prompt = user_input[2:]
    elif user_input.startswith("help"):
        user_input_1 = user_input[4:]
        if user_input_1 == "color" or user_input_1 == "color/?":
            print(
               "","1 = Blue","           ","9 = Light Blue","\n",
                "2 = Green","          ","A = Light Green","\n",
                "3 = Aqua","           ","B = Light Aqua","\n",
                "4 = Red","            ","C = Light Red","\n",
                "5 = Purple","         ","D = Light Purple","\n",
                "6 = Yellow","         ","E = Light Yellow","\n",
                "7 = White","          ","F = Bright White ")
        elif user_input_1 == "dir" or user_input_1 == "dir/?" or user_input_1 == "ls":
            print("Displays a list of files and subdirectories in a directory.")
        elif user_input_1 == "time" or user_input_1 == "time/?":
            print("Displays system time.")
        elif user_input_1 == "date" or user_input_1 == "date/?":
            print("Displays system date.")
        elif user_input_1 == "cls":
            print("Clears the screen.")
        elif user_input_1 == "echo" or user_input_1 == "copycon":
            print("Displays messages, or turns command-echoing on or off.")
        elif user_input_1 == "md" or user_input_1 == "mkdir":
            print("Creates a directory.")
    else:
        print("Command not found. please try 'Help'")