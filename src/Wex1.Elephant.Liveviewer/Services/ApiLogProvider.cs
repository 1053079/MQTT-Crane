using MongoDB.Bson;
using Wex.Elephant.Logger.Infrastructure.Repositories;
using Wex1.Elephant.Liveviewer.Services.Interfaces;
using Wex1.Elephant.Logger.Core.Entities;
using Wex1.Elephant.Logger.Core.Interfaces.Repositories;

namespace Wex1.Elephant.Liveviewer.Services
{
    public class ApiLogProvider<T> : IApiLogProvider<T> where T : BaseLog
    {
        private readonly ILogsRepositorybase<T> _repository;

        public ApiLogProvider(ILogsRepositorybase<T> repository)
        {
            _repository = repository ?? throw new ArgumentNullException(nameof(repository));
        }

        public async Task<IEnumerable<T>> GetAll()
        {
            
            return await _repository.GetListAsync();
        }

        public async Task<T> Get(ObjectId id)
        {
          
            return await _repository.GetByIdAsync(id);
        }
    }
}
