using System.ComponentModel.DataAnnotations;
using System.Runtime.Serialization;


namespace Wex1.Elephant.Liveviewer.Model
{
    public class Baselog
    {
        
        public string Id { get; set; }

        public DateTime Timestamp { get; set; }
        
        public string Component { get; set; }
        
        public string Type { get; set; }
        
        public string Description { get; set;  }


    }
}
