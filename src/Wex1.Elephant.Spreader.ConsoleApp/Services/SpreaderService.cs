using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using Wex1.Elephant.Spreader.Core.Entities;

namespace Wex1.Elephant.Spreader.ConsoleApp.Services
{
    public class SpreaderService
    {
        public SpreaderService()
        {
            Spreaders spreader = new Spreaders();

            spreader.PositionZ = 0;
            spreader.PositionX = 0;
            spreader.PositionX = 0;

        }
    }
}
