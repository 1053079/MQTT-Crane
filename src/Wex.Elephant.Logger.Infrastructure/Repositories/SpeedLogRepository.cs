using Wex1.Elephant.Logger.Core.Entities;
using Wex1.Elephant.Logger.Core.Interfaces.Repositories;

namespace Wex.Elephant.Logger.Infrastructure.Repositories
{
    public class SpeedLogRepository : LogsRepositoryBase<SpeedLog>, ISpeedLogRepository
    {
        public SpeedLogRepository() : base("Speeds")
        {
        }
    }
}
