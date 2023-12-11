using MongoDB.Bson;
using MongoDB.Driver;
using Wex1.Elephant.Logger.Core.Entities;

namespace Wex1.Elephant.Logger.Core.Interfaces.Repositories
{
    public interface ILogsRepositorybase<T> where T : BaseLog
    {
        IMongoCollection<T> GetAll();
        Task<IEnumerable<T>> GetListAsync();
        Task<IEnumerable<T>> GetPagedData(int pageNumber, int pageSize);
        Task<T> GetByIdAsync(ObjectId id);
        Task AddAsync(T entity);
        Task<bool> UpdateAsync(T entity);
        Task<bool> DeleteAsync(T entity);
        Task<long> CountRecords();
    }
}
