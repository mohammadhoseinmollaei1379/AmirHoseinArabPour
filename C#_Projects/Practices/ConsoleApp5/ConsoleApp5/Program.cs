using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Practice One - 1
            /*
            Console.Write("Please Enter The First Name : ");
            string FirstName = Console.ReadLine().Trim();
            Console.Write("Please Enter The Last Name : ");
            string LastName = Console.ReadLine().Trim();
            Console.Write("Please Enter The Job : ");
            string Job = Console.ReadLine().Trim() + '\n'; 

            string FullName = $"{FirstName} {LastName}";

            Console.WriteLine(
                ('\n' + FullName.ToUpper()).PadLeft(30, '=') + '\n' + 
                Job.PadRight(30, '-') + '\n' +
                ("Tedad Caracter Haye Name Kamel : " + FullName.Length + '\n').PadRight(52, '=')
                ); // استفاده از شکل نوشتاری در زبان های C/C++
                   // برای تابع PadRight() خیلی باید امتحان کنیم تا یکسان در بیان
                   //الان 58 و 30 توی PadLeft و PAdRight با هم برابرن
                   */
            // Practice Two - 2
            /*
            Console.Write("Please Enter The E-Mail : ");
            string Email = Console.ReadLine().Trim();

            int IndexAt = Email.IndexOf('@');
            int LenEmail = Email.Length;
            string UserName = Email.Substring(0, IndexAt);
            string Domain = Email.Substring(IndexAt + 1);
            bool www = (Email.StartsWith("www")) ? true : false; 
            bool com = (Email.EndsWith(".com")) ? true : false;
            bool At = (IndexAt > 0) ? true : false; // با بریک پوینت امتحان کردم و دیدم که وقتی اتساین نیست، منفی یک میده

            Console.WriteLine("--- Tahlil Email ---" + '\n' + 
                "Tool Email : " + LenEmail + '\n' + 
                "Shamele @ Mishavad? : " + At + '\n' + 
                "Ba www Shoroue Mishavad? : " + www + '\n' + 
                "Ba .com Tamam Mishavad? : " + com + "\n\n" +
                "Name Karbari : " + UserName + '\n' + 
                "Damaneh : " + Domain
                );
            */
            // Practice Three - 3
            /*
            Console.Write("Enter The Jomleh : ");
            string Jomleh = Console.ReadLine().Trim();
            string Jomleh2 = Jomleh;
            int LenJomleh = Jomleh.Length;

            Jomleh2 = Jomleh2.Replace('a', '4');
            Jomleh2 = Jomleh2.Replace('e', '3');
            Jomleh2 = Jomleh2.Replace('i', '1');
            Jomleh2 = Jomleh2.Replace('o', '0');
            Jomleh2 = Jomleh2.Replace('s', '5');
            Jomleh2 = Jomleh2.Replace(' ', '_');

            Jomleh2 = Jomleh2.ToUpper();

            string CharOne = Jomleh2.Substring(0, 3);
            string CharTwo = Jomleh2.Substring(LenJomleh - 3);
            Console.WriteLine("--- Payame Ramznegari Shodeh" + '\n' + 
                "Payame Asli : " + Jomleh + '\n' + 
                "Payame Ramz : " + Jomleh2 + '\n' + 
                "Toole Payame Ramz : " + LenJomleh + '\n' + 
                "Se Caracter Avval : " + CharOne + '\n' +
                "Se Caracter Akhar : " + CharTwo
                );
            */
            // Practice Four - 4

            Console.Write("Please Enter The Jomleh : ");
            string Jomleh = Console.ReadLine();
            string JomlehTrim = Jomleh.Trim();
            string TenCharOne = Jomleh.Trim().Substring(0, 10);
            string TenCharTwo = Jomleh.Trim().Substring(Jomleh.Length - 10);
            bool IsPowerful = (Jomleh.ToLower().Contains("powerful")) ? true : false;
            bool IsPython = (Jomleh.ToLower().Contains("python")) ? true : false;
            
            Console.WriteLine(
                "--- Gozareshe Tahlil Matn ---" + '\n' + 
                $"Matne Asli : {Jomleh}" + '\n' + 
                $"Matne TRIM Shodeh : {JomlehTrim}" + '\n' + 
                $"Toole Matne TRIM Shodeh : {JomlehTrim.Length}" + '\n' + 
                $"Tedade Caracter Haye Bedone Faseleh : {(Jomleh.Replace(" ", "")).Length}" + "\n\n" + 
                $"Namayesh Ba Horoofe Bozorg : {Jomleh.ToUpper()}" + '\n' +
                $"Namayesh Ba Horoofe Koochak : {Jomleh.ToLower()}" + "\n\n" + 
                $"Shamele Kalemeh Ye \"Powerful\" Ast? {IsPowerful}" + '\n' +
                $"Shamele Kalemeh Ye \"Python\" Ast? {IsPython}" + "\n\n" +
                $"Matne Ba Khatte Tireh : {Jomleh.Trim().Replace(" ", "-")}" + "\n\n" + 
                $"10 Caracter Avval : {TenCharOne}" + '\n' + 
                $"10 Caracter Akhar : {TenCharTwo}"
                );
        }
    }
}
