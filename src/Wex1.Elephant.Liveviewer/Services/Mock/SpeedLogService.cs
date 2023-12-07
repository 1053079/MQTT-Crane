using Wex1.Elephant.Liveviewer.Model;
using Wex1.Elephant.Liveviewer.Services.Interfaces;

namespace Wex1.Elephant.Liveviewer.Services.Mock
{

    public class SpeedLogService : ILogProvider<SpeedLog>
    {
        private static readonly List<SpeedLog> _speedLogs = new List<SpeedLog>
        {
            new SpeedLog { Id = "fsd4651sd", Timestamp = DateTime.Now, Type = Enums.EventType.Speed, Component = Enums.Components.Crane ,  Description = "Kraan start op", Speed = 5.0},
            new SpeedLog { Id = "161", Timestamp = DateTime.Now, Type = Enums.EventType.Speed, Component = Enums.Components.Crane ,  Description = "Kraan haalt maximale snelheid", Speed = 42.0},
            new SpeedLog { Id = "qds4qsd146", Timestamp = DateTime.Now, Type = Enums.EventType.Speed, Component = Enums.Components.Motor ,  Description = "Motor start", Speed =10.0}
        };

        public Task<IEnumerable<SpeedLog>> GetAll()
        {
            return Task.FromResult(_speedLogs.AsEnumerable());
        }

        public Task<SpeedLog> Get(string id)
        {
            return Task.FromResult(_speedLogs.FirstOrDefault(speed => speed.Id.Equals(id)));
        }
    }

}
