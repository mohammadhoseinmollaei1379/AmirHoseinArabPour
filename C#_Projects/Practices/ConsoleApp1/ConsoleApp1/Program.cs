using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // practice One - 1
            /*
            Console.Write("Please Enter The Name : ");
            string name = Console.ReadLine();
            for (int i = 0; i < name.Length; i++)
            {
                Console.WriteLine("index " + i + " = " + name[i]);
            }*/
            // -----------------------
            // practice Two - 2
            /*
            Console.Write("aya havaa aftabi ast?? ( bale / kheir)");
            string weather = Console.ReadLine();
            switch (weather) 
            {
                case "bale":
                    Console.WriteLine("chatr nayaavar!");
                    break;
                case "kheir":
                    Console.WriteLine("chatr bardaar!");
                    break;
                default:
                    Console.WriteLine("lotfan faghat bale ya kheir vared konid");
                    break;
            }*/
            /*
            if (weather == "bale")
            {
                Console.WriteLine("chatr nayaavar!");
            }
            else if (weather == "kheir")
            {
                Console.WriteLine("chatr bardaar!");
            }
            else
            {
                Console.WriteLine("lotfan faghat bale ya kheir vared konid");
            }*/
            // --------------------------
            // practice three - 3
            /*
            Console.Write("Enter The Words : ");
            string words = Console.ReadLine();
            int index_1 = 0;
            int index_2 = 0;
            // int index_3 = 0;
            for (int i = 0; i < words.Length; i++)
            {
                if (words[i] == 'a')
                {
                    index_1++;
                }
                else if (words[i] == 'A')
                {
                    index_2++;
                }
                
                //else if (words[i] == 'a' || words[i] == 'A')
                //{
                //    index_3++;
                //}
                // به دلیل اینکه این شرط آخر بود و همه قبل از اون اجرا میشدن، این قسمت کامنت گرفته شد
            }
            Console.WriteLine("tekrar a = " + index_1);
            Console.WriteLine("tekrar A = " +  index_2);*/
            // Console.WriteLine("tekrar a and A = " +  index_3);
            // ------------------------------
            // practice four - 4
            /*
            string text = "Hello World";
            char maxChar = text[0];

            for (int i = 0; i < text.Length; i++)
            {
                if (text[i] > maxChar)
                {
                    maxChar = text[i];
                }
            }
            Console.WriteLine("Max Char => " + maxChar); // خروجی r و درست است چون دبلیو بزرگ در جدول اسکی از حرف r کم ارزش تر است
            */
        }
    }
}
