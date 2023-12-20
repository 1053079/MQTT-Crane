using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace Wex1.Elephant.Logger.Core.Dto.MqttInputs
{
    public class motorDto
    {
        [JsonPropertyName("direction")]
        public string Direction { get; set; }
        [JsonPropertyName("speed")]
        public string Speed { get; set; }
    }
}
