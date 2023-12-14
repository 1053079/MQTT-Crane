using System.Text.Json.Serialization;

namespace Wex1.Elephant.Logger.Core.Dto.MqttInputs
{
    public class JoyStickDto
    {
        [JsonPropertyName("movement")]
        public string Direction { get; set; }
        [JsonPropertyName("speed")]
        public string Speed { get; set; }
        [JsonPropertyName("lock")]
        public bool IsLocked { get; set; }
    }
}
