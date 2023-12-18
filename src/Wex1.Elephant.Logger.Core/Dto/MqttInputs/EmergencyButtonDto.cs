using System.Text.Json.Serialization;

namespace Wex1.Elephant.Logger.Core.Dto.MqttInputs
{
    public class EmergencyButtonDto
    {
        [JsonPropertyName("status")]
        public bool IsPressed { get; set; }
    }
}
