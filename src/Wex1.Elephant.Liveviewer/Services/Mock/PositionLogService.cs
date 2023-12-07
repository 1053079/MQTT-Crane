using Wex1.Elephant.Liveviewer.Model;
using Wex1.Elephant.Liveviewer.Services.Interfaces;

namespace Wex1.Elephant.Liveviewer.Services.Mock
{
    public class PositionLogService : ILogProvider<PositionLog>
    {
        private static readonly List<PositionLog> _positionLogs = new List<PositionLog>
            {
                new PositionLog { Id = "47675456", Timestamp = DateTime.Now, Type = Enums.EventType.Position, Component = Enums.Components.Crane ,  Description = "Kraan verandert van positio" , PositionX = 2.0 , PositionY = 3.0 , PositionZ = 5.0},
                new PositionLog { Id = "q56qds45qds", Timestamp = DateTime.Now, Type = Enums.EventType.Position, Component = Enums.Components.Motor ,  Description = "Motor in volle snelheid" , PositionX = 10.0 , PositionY = 13.0 , PositionZ = 15.0},
                new PositionLog { Id = "qsqs56d", Timestamp = DateTime.Now, Type = Enums.EventType.Position, Component = Enums.Components.Break ,  Description = "Kraan stopt" , PositionX = 0.0 , PositionY = 0.0 , PositionZ = 0.0}
            };

        public Task<IEnumerable<PositionLog>> GetAll()
        {
            return Task.FromResult(_positionLogs.AsEnumerable());
        }

        public Task<PositionLog> Get(string id)
        {
            return Task.FromResult(_positionLogs.FirstOrDefault(position => position.Id.Equals(id)));
        }

    }
}
