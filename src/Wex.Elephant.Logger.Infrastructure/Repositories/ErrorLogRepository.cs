using MongoDB.Bson.Serialization;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Wex1.Elephant.Logger.Core.Entities;
using Wex1.Elephant.Logger.Core.Interfaces.Repositories;

namespace Wex.Elephant.Logger.Infrastructure.Repositories
{
    public class ErrorLogRepository : LogsRepositoryBase<ErrorLog>, IErrorLogRepository
    {
        public ErrorLogRepository() : base("Errors")
        {
            
        }
    }
}
