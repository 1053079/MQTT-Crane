using Wex1.Elephant.Liveviewer.Enums;

namespace Wex1.Elephant.Liveviewer.Dto
{
    public class LogDto
    {

        public string Id { get; set; }
        public DateTime Timestamp { get; set; }
        public EventType Type { get; set; }
        public Components Component { get; set; }
        public string Description { get; set; }
    }
}
