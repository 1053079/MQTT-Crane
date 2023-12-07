using MongoDB.Bson;
using Wex1.Elephant.Liveviewer.Dto;
using Wex1.Elephant.Liveviewer.Services.Interfaces;
using Wex1.Elephant.Logger.Core.Entities;
using Wex1.Elephant.Logger.Core.Filters;
using Wex1.Elephant.Logger.Core.Interfaces.Repositories;
using Wex1.Elephant.Logger.WebApi.Services.CrudServices;

namespace Wex1.Elephant.Liveviewer.Services
{
    public class ApiErrorProvider : ApiLogProvider<ErrorLog>
    {
        public ApiErrorProvider(ILogsRepositorybase<ErrorLog> repository) : base(repository)
        {

        }
    }
}
