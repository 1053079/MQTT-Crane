using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace Wex1.Elephant.Spreader.Core.SpreaderPositionDto
{
    public class SpreaderPositionDto
    {

        [JsonPropertyName ("positionX")]
        public double PositionX { get; set; }
        [JsonPropertyName("positionY")]
        public double PositionY { get; set; }

        [JsonPropertyName("positionZ")]
        public double PositionZ { get; set; }
    }
}
