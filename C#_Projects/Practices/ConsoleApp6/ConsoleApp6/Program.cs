using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp6
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Practice One - 1
            /*
            Console.Write("Please Enter Number 1 : ");
            int NumberOne = int.Parse(Console.ReadLine());
            Console.Write("Please Enter Number 2 : ");
            int NumberTwo = int.Parse(Console.ReadLine());

            bool isEqual = NumberOne == NumberTwo;

            Console.WriteLine("--- Natijeh Ye Moghayeseh ---");

            if (NumberOne > NumberTwo)
            {
                Console.WriteLine("Adad Avval Bozorg Tar Ast.");
            }
            else if (NumberOne < NumberTwo)
            {
                Console.WriteLine("Adad Dovvom Bozorg Tar Ast.");
            }
            else {
                Console.WriteLine("Har Do Adad Barabarand.");
            }

            Console.WriteLine($"Aya Do Adad Barabarand? {isEqual}");
            */

            // Practice Two - 2
            /*
            Console.Write("Please Enter Number 1 : ");
            int NumberOne = Convert.ToInt32(Console.ReadLine());
            Console.Write("Please Enter Number 2 : ");
            int NumberTwo = Convert.ToInt32(Console.ReadLine());

            double result = 0;

            Console.Write("Please Enter The Amalgar (+, -, /, *) :");
            char Amalgar = Convert.ToChar(Console.ReadLine());

            Console.WriteLine("--- Natije ---");

            switch (Amalgar)
                {
                case '+':
                    result = NumberOne + NumberTwo;
                    Console.WriteLine($"{NumberOne} {Amalgar} {NumberTwo} = {result}");
                    break;
                case '-':
                    result = NumberOne - NumberTwo;
                    Console.WriteLine($"{NumberOne} {Amalgar} {NumberTwo} = {result}");
                    break;
                case '*':
                    result = NumberOne * NumberTwo;
                    Console.WriteLine($"{NumberOne} {Amalgar} {NumberTwo} = {result}");
                    break;
                case '/':
                    if (NumberOne != 0 ||
                        NumberTwo != 0) 
                    {
                        result = (NumberOne / NumberTwo);
                        Console.WriteLine($"{NumberOne} {Amalgar} {NumberTwo} = {result}");
                    }
                    else 
                    {
                        Console.WriteLine("KHATA: Taghsim Bar 0 Momken Nist!");
                    }
                    break;
                default:
                    Console.WriteLine("KHATA: Amalgar Na Motabar!");
                    break;
            }
            */

            // Practice Three - 3
            /*
            Console.Write("Lotfan Zel'e Aval Mosallas Ra Vared Konid : ");
            int A = Convert.ToInt32(Console.ReadLine());
            Console.Write("Lotfan Zel'e Dovvom Mosallas Ra Vared Konid : ");
            int D = Convert.ToInt32(Console.ReadLine());
            Console.Write("Lotfan Zel'e Sevvom Mosallas Ra Vared Konid : ");
            int S = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("--- Natijeh ---");

            if ((A + D > S) && 
                (A + S > D) &&
                (D + S > A))
            {
                if ((A == D) &&
                    (D == S) &&
                    (A == S))
                {
                    Console.WriteLine("No'e Mosallas : Mosallas Motasavi Olazlaa'e");
                }
                else if (
                    (A == D) ||
                    (D == S) ||
                    (A == S))
                {
                    Console.WriteLine("No'e Mosallas : Mosallas Motasavi Ossaghein");
                }
            }
            else
            {
                Console.WriteLine("In 3 Zel'e Nemitavaanand Yek Mosallas Tashkil Dahand!");
            }
            */

            // Practice Four - 4
            /*
            Console.Write("Mablaghe Kharid Ra Vared Konid : ");
            int Price = Convert.ToInt32(Console.ReadLine());
            Console.Write("Sathe Ozviat (1=Addi, 2=Noghreh iy, 3=Talaaye) : ");
            int Ozviat = Convert.ToInt32(Console.ReadLine());
            Console.Write("Aya Avvalin Kharide Shomast? (1=Bale, 2=Kheyr) : ");
            int AvvalKharid = Convert.ToInt32(Console.ReadLine());

            double Takhfif = 0.0;
            double TakhfifOzviat = 0.0;
            double TakhfifBish500 = 0.0;
            double TakhfifAvvalKharid = 0.0;

            Console.WriteLine("--- Factore Kharid ---");
            Console.WriteLine($"Mablaghe Avvalieh : {Price.ToString("N0")} Toman");

            switch (Ozviat) 
            {
                case 1:
                    TakhfifOzviat = 0.0 * Price;
                    Console.WriteLine($"Takhfif Sathe Ozviat : {"Bedoone Ozviat"}");
                    break;
                case 2:
                    TakhfifOzviat = 0.05 * Price;
                    Console.WriteLine($"Takhfif Sathe Ozviat (5%) : {TakhfifOzviat.ToString("N0")} Toman");
                    break;
                case 3:
                    TakhfifOzviat = 0.10 * Price;
                    Console.WriteLine($"Takhfif Sathe Ozviat (10%) : {TakhfifOzviat.ToString("N0")} Toman");
                    break;
                default:
                    Console.WriteLine("KHATA: Lotfan Baraye Ozviat Adad Monaseb Vared Konid!");
                    break;
            }
            if (Price > 500000)
            {
                TakhfifBish500 = 0.05 * Price;
                Console.WriteLine($"Takhfif Kharide Balaye 500 Hezar (5%) : {(TakhfifBish500).ToString("N0")} Toman");
            }
            if (AvvalKharid == 1) 
            {
                TakhfifAvvalKharid = 0.10 * Price;
                Console.WriteLine($"Takhfif Avvalin Kharid (10%) : {(TakhfifAvvalKharid).ToString("N0")} Toman");
            }

            Takhfif = TakhfifOzviat + TakhfifAvvalKharid + TakhfifBish500;

            Price -= Convert.ToInt32(Takhfif);

            Console.WriteLine("-------------------------");
            Console.WriteLine($"Mablaghe Nahaayie Ghabele Pardakht : {Price.ToString("N0")} Toman");
            */
        }
    }
}
