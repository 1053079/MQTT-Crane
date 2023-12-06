using Wex1.Elephant.Liveviewer.Model;

namespace Wex1.Elephant.Liveviewer.Services.Mock
{
    public class ErrorLogService : ILogProvider<ErrorLog>
    {
        private static readonly List<ErrorLog> _errorLogs = new List<ErrorLog>
        {
            new ErrorLog { Id = "1615", Timestamp = DateTime.Now, Type = Enums.EventType.Error, Component = Enums.Components.Crane ,  Description = "Kraan werkt niet"},
            new ErrorLog { Id = "1616565", Timestamp = DateTime.Now, Type = Enums.EventType.Error, Component = Enums.Components.Joystick ,  Description = "Positie niet correct"},
            new ErrorLog { Id = "e64f4q6", Timestamp = DateTime.Now, Type = Enums.EventType.Error, Component = Enums.Components.Motor ,  Description = "Motor start niet"}
        };

        public Task<IEnumerable<ErrorLog>> GetAll()
        {
            return Task.FromResult(_errorLogs.AsEnumerable());
        }

        public Task<ErrorLog> Get(string id)
        {
            return Task.FromResult(_errorLogs.FirstOrDefault(error => error.Id.Equals(id)));
        }
    }
}
