using Wex1.Elephant.Logger.Core.Entities;
using Wex1.Elephant.Logger.Core.Interfaces.Repositories;

namespace Wex.Elephant.Logger.Infrastructure.Repositories
{
    public class ActionLogRepository : LogsRepositoryBase<ActionLog>, IActionLogRepository
    {
        public ActionLogRepository() : base("Actions")
        {
        }
    }
}
