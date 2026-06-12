using System;

namespace MIR
{
    class Program
    {
        static void Main()
        {
            using (var game = new MakeItRain.Game())
                game.Run();
        }
    }
}
