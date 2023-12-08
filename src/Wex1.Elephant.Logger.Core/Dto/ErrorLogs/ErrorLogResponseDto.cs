namespace Wex1.Elephant.Logger.Core.Dto.ErrorLogs
{
    public class ErrorLogResponseDto
    {
        public string Id { get; set; }
        public DateTime EventTimeStamp { get; set; }
        public string EventType { get; set; }
        public string Component { get; set; }
        public string Description { get; set; }
    }
}
