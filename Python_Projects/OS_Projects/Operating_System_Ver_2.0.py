import os
import shutil
import datetime
from tqdm import tqdm
from time import sleep
from colorama import init, Fore


class Color:
    def helpColor(self):
        # global help_color
        help_color = """1 = Blue           9 = Light Blue
        2 = Green          A = Light Green
        3 = Aqua           B = Light Aqua
        4 = Red            C = Light Red
        5 = Purple         D = Light Purple
        6 = Yellow         E = Light Yellow
        7 = White          F = Bright White"""
        print(help_color)
    def colors(self, color):
        self.startswith(color) = color
        init()
        color = color[5:]
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
            print(Fore.WHITE + f"Sorry, this {color} is not supported. \n", helpColor())