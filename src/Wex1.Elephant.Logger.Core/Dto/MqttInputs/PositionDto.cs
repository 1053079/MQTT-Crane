using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace Wex1.Elephant.Logger.Core.Dto.MqttInputs
{
    public class PositionDto
    {
        [JsonPropertyName("positionX")]
        public double X { get; set; }
        [JsonPropertyName("positionY")]
        public double Y { get; set; }
    }
}
