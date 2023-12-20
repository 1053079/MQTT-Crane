namespace Wex1.Elephant.Logger.Core.Dto.Actionlogs
{
    public class ActionLogResponseDto
    {
        public string Id { get; set; }
        public DateTime EventTimeStamp { get; set; }
        public string EventType { get; set; }
        public string Component { get; set; }
        public string Description { get; set; }
    }
}
