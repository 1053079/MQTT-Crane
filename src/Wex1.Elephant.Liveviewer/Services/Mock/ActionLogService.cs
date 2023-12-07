using Wex1.Elephant.Liveviewer.Model;
using Wex1.Elephant.Liveviewer.Services.Interfaces;

namespace Wex1.Elephant.Liveviewer.Services.Mock
{
    public class ActionLogService : ILogProvider<ActionLog>
    {
        private static readonly List<ActionLog> _actionLogs = new List<ActionLog>
            {
                new ActionLog { Id = "4qfd56456q5d", Timestamp = DateTime.Now, Type = Enums.EventType.Action, Component = Enums.Components.Crane ,  Description = "Kraan staat aan"},
                new ActionLog { Id = "6qd54sd465", Timestamp = DateTime.Now, Type = Enums.EventType.Action, Component = Enums.Components.Joystick ,  Description = "Joystick gaat naar links"},
                new ActionLog { Id = "qsd65qsd4q6", Timestamp = DateTime.Now, Type = Enums.EventType.Action, Component = Enums.Components.Motor ,  Description = "Motor staat uit"}
            };

        public Task<IEnumerable<ActionLog>> GetAll()
        {
            return Task.FromResult(_actionLogs.AsEnumerable());
        }

        public Task<ActionLog> Get(string id)
        {
            return Task.FromResult(_actionLogs.FirstOrDefault(action => action.Id.Equals(id)));
        }
    }
}
