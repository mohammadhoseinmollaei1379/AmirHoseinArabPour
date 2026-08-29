using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Practice One - 1
            /*
            Console.Write("Enter Number : ");
            int Number = int.Parse(Console.ReadLine());

            Console.WriteLine("Number Avvalieh : " + Number);
            Number += 10;
            Console.WriteLine("Ba'd az += 10 : " + Number);
            Number -= 3;
            Console.WriteLine("Ba'd az -= 3 : " + Number);
            Number *= 2;
            Console.WriteLine("Ba'd az *= 2 : " + Number);
            Number /= 4;
            Console.WriteLine("Ba'd az /= 4 : " + Number);
            Number %= 7;
            Console.WriteLine("Ba'd az %= 7 : " + Number);
            */
            // Practice Two - 2
            /*
            Console.Write("Enter Number 1 : ");
            int NumberOne = int.Parse(Console.ReadLine());
            Console.Write("Enter Number 2 : ");
            int NumberTwo = int.Parse(Console.ReadLine());
            Console.Write("Enter Number 3 : ");
            int NumberThree = int.Parse(Console.ReadLine());

            if (NumberOne % 2 == 0 && NumberTwo % 2 == 0 && NumberThree % 2 == 0) 
            {
                Console.WriteLine("Adad " + NumberOne + " : zouj");
                Console.WriteLine("Adad " + NumberTwo + " : zouj");
                Console.WriteLine("Adad " + NumberThree + " : zouj");
            }
            if (NumberOne % 2 == 1 && NumberTwo % 2 == 0 && NumberThree % 2 == 0)
            {
                Console.WriteLine("Adad " + NumberOne + " : fard");
                Console.WriteLine("Adad " + NumberTwo + " : zouj");
                Console.WriteLine("Adad " + NumberThree + " : zouj");
            }
            if (NumberOne % 2 == 0 && NumberTwo % 2 == 1 && NumberThree % 2 == 0)
            {
                Console.WriteLine("Adad " + NumberOne + " : zouj");
                Console.WriteLine("Adad " + NumberTwo + " : fard");
                Console.WriteLine("Adad " + NumberThree + " : zouj");
            }
            if (NumberOne % 2 == 0 && NumberTwo % 2 == 0 && NumberThree % 2 == 1)
            {
                Console.WriteLine("Adad " + NumberOne + " : zouj");
                Console.WriteLine("Adad " + NumberTwo + " : zouj");
                Console.WriteLine("Adad " + NumberThree + " : fard");
            }
            if (NumberOne % 2 == 1 && NumberTwo % 2 == 1 && NumberThree % 2 == 0)
            {
                Console.WriteLine("Adad " + NumberOne + " : fard");
                Console.WriteLine("Adad " + NumberTwo + " : fard");
                Console.WriteLine("Adad " + NumberThree + " : zouj");
            }
            if (NumberOne % 2 == 1 && NumberTwo % 2 == 0 && NumberThree % 2 == 1)
            {
                Console.WriteLine("Adad " + NumberOne + " : fard");
                Console.WriteLine("Adad " + NumberTwo + " : zouj");
                Console.WriteLine("Adad " + NumberThree + " : fard");
            }
            if (NumberOne % 2 == 0 && NumberTwo % 2 == 1 && NumberThree % 2 == 1)
            {
                Console.WriteLine("Adad " + NumberOne + " : zouj");
                Console.WriteLine("Adad " + NumberTwo + " : fard");
                Console.WriteLine("Adad " + NumberThree + " : fard");
            }
            if (NumberOne % 2 == 1 && NumberTwo % 2 == 1 && NumberThree % 2 == 1)
            {
                Console.WriteLine("Adad " + NumberOne + " : fard");
                Console.WriteLine("Adad " + NumberTwo + " : fard");
                Console.WriteLine("Adad " + NumberThree + " : fard");
            }

            Console.WriteLine("Adad avval va dovvom ba ham barabarand? : " + (NumberOne == NumberTwo));
            Console.WriteLine("Adad sevvom az majmou' do adad avval bozorgtar ast? : " + (NumberOne + NumberTwo < NumberThree));
            */
            // Practice Three - 3
            /*
            Console.Write("Vazn khod ra beh kilogeram vared konid : ");
            double Weight = double.Parse(Console.ReadLine());
            Console.Write("Ghad khod ra beh metr vared konid : ");
            double May = double.Parse(Console.ReadLine());

            double BMI = Weight / (Math.Pow(May, 2));

            Console.WriteLine("BMI Shoma : " +  BMI.ToString("F2"));
            Console.WriteLine("Aya dar mahdoudeh ye salem hastid? : " + (BMI >= 18.5 && BMI <= 24.9));
            */
            // Practice Four - 4
            /*
            Console.Write("Mablaghe kharid khod ra vared konid : ");
            int Price = int.Parse(Console.ReadLine());
            Console.Write("Aya kart bashgah moshtarian darid? (1=bale, 0=kheir) : ");
            string A = Console.ReadLine();
            bool CClub;
            if (A == "1") { CClub = true; }
            else { CClub = false; }

            if (Price < 200000)
            {
                Console.WriteLine("--- Factore Kharid ---");
                Console.WriteLine("Mablagh Payeh : " + Price.ToString("N0"));
                Console.WriteLine("Takhfif Payeh : " + "Bedoun Takhfif");
                Console.WriteLine("Mablagh Nahaayie Ghabele Pardakht : " + Price.ToString("N0"));
            }
            if (Price >= 200000 && Price <= 500000)
            {
                if (CClub)
                {
                    Console.WriteLine("--- Factore Kharid ---");
                    Console.WriteLine("Mablagh Payeh : " + Price.ToString("N0"));
                    Console.WriteLine("Takhfif Payeh (10%) : " + ((Price / 100) * 10).ToString("N0"));
                    Console.WriteLine("Mablagh Ba'd Az Takhfif Payeh : " + (Price - ((Price / 100) * 10)).ToString("N0"));
                    Console.WriteLine("Takhfif Bashgahe Moshtarian (5%) : " + ((Price / 100) * 5).ToString("N0"));
                    Console.WriteLine("Mablagh Nahaayie Ghabele Pardakht : " + (Price - ((Price / 100) * 10) - ((Price / 100) * 5)).ToString("N0"));
                }
                else
                {
                    Console.WriteLine("--- Factore Kharid ---");
                    Console.WriteLine("Mablagh Payeh : " + Price.ToString("N0"));
                    Console.WriteLine("Takhfif Payeh (10%) : " + ((Price / 100) * 10).ToString("N0"));
                    Console.WriteLine("Mablagh Ba'd Az Takhfif Payeh : " + (Price - ((Price / 100) * 10)).ToString("N0"));
                    Console.WriteLine("Mablagh Nahaayie Ghabele Pardakht : " + (Price - ((Price / 100) * 10)).ToString("N0"));
                }
            }
            if (Price > 500000)
            {
                if (CClub)
                {
                    Console.WriteLine("--- Factore Kharid ---");
                    Console.WriteLine("Mablagh Payeh : " + Price.ToString("N0"));
                    Console.WriteLine("Takhfif Payeh (15%) : " + ((Price / 100) * 15).ToString("N0"));
                    Console.WriteLine("Mablagh Ba'd Az Takhfif Payeh : " + (Price -= ((Price / 100) * 15)).ToString("N0"));
                    Console.WriteLine("Takhfif Bashgahe Moshtarian (5%) : " + ((Price / 100) * 5).ToString("N0"));
                    Console.WriteLine("Mablagh Nahaayie Ghabele Pardakht : " + (Price - ((Price / 100) * 5)).ToString("N0"));
                }
                else
                {
                    Console.WriteLine("--- Factore Kharid ---");
                    Console.WriteLine("Mablagh Payeh : " + Price.ToString("N0"));
                    Console.WriteLine("Takhfif Payeh (10%) : " + ((Price / 100) * 15).ToString("N0"));
                    Console.WriteLine("Mablagh Ba'd Az Takhfif Payeh : " + (Price - ((Price / 100) * 15)).ToString("N0"));
                    Console.WriteLine("Mablagh Nahaayie Ghabele Pardakht : " + (Price - ((Price / 100) * 15)).ToString("N0"));
                }
            */
            }
        }
    }
}
