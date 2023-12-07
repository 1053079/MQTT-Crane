using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Wex1.Elephant.Logger.Core.Entities;

namespace Wex.Elephant.Logger.Infrastructure.Repositories
{
    public class PositionLogRepository : LogsRepositoryBase<PositionLog>
    {
        public PositionLogRepository() : base("Positions")
        {
        }
    }
}
