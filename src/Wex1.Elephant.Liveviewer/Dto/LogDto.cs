using System.Text.Json.Serialization;
using Wex1.Elephant.Liveviewer.Enums;

namespace Wex1.Elephant.Liveviewer.Dto
{
    public class LogDto
    {

       
        public DateTime Timestamp { get; set; }
        
        public Components Component { get; set; }
        public string Description { get; set; }
    }
}
