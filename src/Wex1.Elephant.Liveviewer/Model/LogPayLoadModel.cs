using MongoDB.Bson;
using System.Text.Json.Serialization;

namespace Wex1.Elephant.Liveviewer.Model
{
    public class LogPayLoadModel
    {
        [JsonPropertyName("Id")]
        public ObjectId Id { get; set; }

        [JsonPropertyName("EventTimeStamp")]
        public DateTime Timestamp { get; set; }

        public string Component { get; set; }
        [JsonPropertyName("EventType")]
        public string Type { get; set; }

        public string Description { get; set; }
    }
}
