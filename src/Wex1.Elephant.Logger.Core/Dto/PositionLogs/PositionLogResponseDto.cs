namespace Wex1.Elephant.Logger.Core.Dto.PositionLogs
{
    public class PositionLogResponseDto
    {
        public string Id { get; set; }
        public DateTime EventTimeStamp { get; set; }
        public string EventType { get; set; }
        public string Component { get; set; }
        public string Description { get; set; }
        public double PositionX { get; set; }
        public double PositionY { get; set; }
        public double PositionZ { get; set; }
    }
}
