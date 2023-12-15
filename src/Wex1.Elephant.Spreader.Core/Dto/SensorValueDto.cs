using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace Wex1.Elephant.Spreader.Core.Dto
{
    public class SensorValueDto
    {
        [JsonPropertyName ("sensorValue")]
        public bool SensorValue { get; set; }
    }
}
