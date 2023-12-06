namespace Wex1.Elephant.Logger.Core.Dto.SpeedLogs
{
    public class SpeedLogResponseDto
    {
        public string Id { get; set; }
        public DateTime EventTimeStamp { get; set; }
        public double Speed { get; set; }
        public string EventType { get; set; }
        public string component { get; set; }
        public string Description { get; set; }
    }
}
