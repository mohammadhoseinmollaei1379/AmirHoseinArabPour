using System;
using System.Collections.Generic;
using System.ComponentModel.Design;
using System.Data.SqlClient;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            
            Console.WriteLine("New-Shell Corporation.");
            Console.WriteLine(" _   _                   ____  _          _ _\n| \\ | | _____      __   / ___|| |__   ___| | |\n|  \\| |/ _ \\ \\ /\\ / /___\\___ \\| '_ \\ / _ \\ | |\n| |\\  |  __/\\ V  V /_____|__) | | | |  __/ | |\n|_| \\_|\\___| \\_/\\_/     |____/|_| |_|\\___|_|_|");
            Console.Write("Please enter your name prompt : ");
            string namePrompt = Console.ReadLine();
            string ver = "1.0.0";
            string shutDown = "/r";
            string help = "CLS, CLEAR                    => Clear the screen \nHALT, SHUTDOWN(/s), POWEROFF  => Off the system \nVER                           => Display the version of system \nECHO                          => Displays messages";
            while (shutDown == "/r")
            {
                Console.Write($"{namePrompt}:\\>");
                string read = Console.ReadLine();
                read = read.ToLower();
                switch (read)
                {
                    case "poweroff":
                    case "shutdown /s":
                    case "shutdown":
                    case "halt":
                    case "exit":
                        shutDown = "/s";
                        break;
                    case "":
                    case " ":
                        break;
                    case "clear":
                    case "cls":
                        Console.Clear();
                        break;
                    case "ver":
                    case "version":
                        Console.WriteLine(ver);
                        break;
                    case "echo":
                        Console.WriteLine(Console.ReadLine());
                        break;
                    case "help":
                        Console.WriteLine(help);
                        break;
                    default:
                        Console.WriteLine("Command not found. please try 'Help'");
                        break;
                }
            }
        }
    }
}
