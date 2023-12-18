using System.Text.Json.Serialization;

namespace Wex1.Elephant.Liveviewer.Dto
{
    public class LogDto
    {

        public string Id { get; set; }

        [JsonPropertyName("EventTimeStamp")]
        public DateTime Timestamp { get; set; }

        public string Type { get; set; }
        
        public string Component { get; set; }
        public string Description { get; set; }
    }
}
