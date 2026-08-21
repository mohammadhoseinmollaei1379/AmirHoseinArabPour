using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Practice One - 1
            /*
            Console.Write("Tool Ra Vared Konid : ");
            double Tool = double.Parse(Console.ReadLine()); // Casting
            Console.Write("Arz Ra Vared Konid : ");
            double Arz = double.Parse(Console.ReadLine()); // Casting

            double Masahat = Tool * Arz;
            double Mohit = (Tool + Arz) * 2;
            double Ghotr = Math.Sqrt(Math.Pow(Tool, 2) + Math.Pow(Arz, 2));

            Console.WriteLine("--- Natayeje Mohasebeh ---");
            Console.WriteLine("Masahat : " + Masahat.ToString("F2"));
            Console.WriteLine("Mohit : " + Mohit.ToString("F2"));
            Console.WriteLine("Ghotr : " + Ghotr.ToString("F2"));*/
            // Practice Two - 2
            /*
            Console.Write("Gheymat Ghaza Ra Vared Konid (Toman) : ");
            int Gheymat = int.Parse(Console.ReadLine());
            Console.Write("Darsad Maliat Ra Vared Konid (Faghat Adad, Bedoon Darsad) : ");
            double Maliat = double.Parse(Console.ReadLine());
            Console.Write("Darsad Anaam Ra Vared Konid (Faghat Adad, Bedoon Darsad) : ");
            double Anaam = double.Parse(Console.ReadLine());

            double MaliatResult = (Maliat / 100) * Gheymat;
            double AnaamResult = (Anaam / 100) * Gheymat;
            double ResultNahaayi = (MaliatResult + AnaamResult + Gheymat);

            Console.WriteLine("--- Sourat Hesabe Shoma ---");
            Console.WriteLine("Gheymat Gaza : " + Gheymat.ToString("N0") + "Toman");
            Console.WriteLine("Maliat (" + Maliat + "%) : "+ MaliatResult.ToString("N0") + " Toman");
            Console.WriteLine("Anaam (" + Anaam + "%) : " + AnaamResult.ToString("N0") + " Toman");
            Console.WriteLine("Mablagh Nahaayie Ghabele Pardakht : " + ResultNahaayi.ToString("N0") + " Toman");*/
            // Practice Three - 3
            /*
            Console.Write("Tedaad Saniyeh Ha Ra Vared Konid : ");
            int Seconds = int.Parse(Console.ReadLine());
            int Hour = Convert.ToInt32(Seconds / 3600);
            Seconds -= Hour * 3600;
            int minute = Convert.ToInt32(Seconds / 60);
            Seconds -= minute * 60;
            int Second = Convert.ToInt32(Seconds / 1);
            Seconds -= Second * 1;

            Console.WriteLine("Natijeh Ye Tabdil : " + Hour + " Saat, " + minute + " Daghigheh, " + Second + " Saniyeh");*/
            // Practice Four - 4
            /*
            Console.Write("Masaafat Kolle Safar (Kilometr) : ");
            int Masaafat = int.Parse(Console.ReadLine());
            Console.Write("Soraat Motavasset (KM/H) : ");
            int Soraat = int.Parse(Console.ReadLine());
            Console.Write("Masraf Soukht (Litr Dar 100 Kilometr) : ");
            double Soukht = double.Parse(Console.ReadLine());
            Console.Write("Gheymat Har Litr Benzin (Toman) : ");
            int Gheymat = int.Parse(Console.ReadLine());

            double Saat = (Masaafat / Soraat);
            double SoukhtMasrafi = (Masaafat * Soukht) / 100;
            double HazinehBenzin = SoukhtMasrafi * Gheymat;

            Console.WriteLine("--- Gozaareshe Safar ---");
            Console.WriteLine("Zaman Taghribye Safar : " + Saat.ToString("F1") + " Saat");
            Console.WriteLine("Benzine Masrafi : " + SoukhtMasrafi.ToString("F2") + " Litr");
            Console.WriteLine("Hazine Benzin : " + HazinehBenzin.ToString("N0") + " Toman");*/
        }
    }
}
