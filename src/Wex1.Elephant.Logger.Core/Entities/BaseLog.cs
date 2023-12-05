using MongoDB.Bson;


namespace Wex1.Elephant.Logger.Core.Entities
{
    public class BaseLog
    {

        public ObjectId Id { get; set; }
        public DateTime EventTimeStamp { get; set; }
        public string EventType { get; set; }
        public string Component { get; set; }
        public string Description { get; set; }
    }
}
