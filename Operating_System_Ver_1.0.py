import os
from colorama import init, Fore, Style
import shutil
print("new shell [version 1.0] \nname corporation")
name_prompt = input("Please enter your prompt name :")
y = 0
while y == 0:
    user_input = input(f"C:\\{name_prompt}>")
    user_input = user_input.lower()
    if user_input == "halt" or user_input == "shut down" or user_input == "khamoosh" or user_input == "shutdown" or user_input == "kamosh" or user_input == "poweroff" or user_input == "off":
        print("See you later...")
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
    elif user_input.startswith("echo "):
        print(user_input[5:])
        if user_input == "echo":
            print()
    elif user_input == "rd" or user_input == "rmdir" or user_input == "rm" or user_input == "remove-item" or user_input == "del":
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
    elif user_input == "newprompt" or user_input == "new prompt" or user_input == "prompt":
        name_prompt = input("Please enter your new prompt name :")
    