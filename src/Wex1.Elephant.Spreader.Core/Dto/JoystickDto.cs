using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace Wex1.Elephant.Spreader.Core.Dto
{
    public class JoystickDto
    {
        [JsonPropertyName("movement")]
        public string Movement { get; set; }

        [JsonPropertyName("speed")]
        public string Speed { get; set; }

        [JsonPropertyName("lock")]
        public bool Lock { get; set; }
    }
}
