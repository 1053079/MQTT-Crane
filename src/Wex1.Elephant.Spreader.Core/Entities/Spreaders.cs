using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Wex1.Elephant.Spreader.Core.Entities
{
    public class Spreaders
    {
        public double PositionX { get; set; }
        public double PositionY { get; set; }  
       

        public Sensor Sensor { get; set; } = new Sensor();


        public bool Lock { get; set; }

        
    }
}
