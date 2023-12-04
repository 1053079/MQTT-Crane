using MongoDB.Bson;
using MongoDB.Driver;
using Wex1.Elephant.Logger.Core;
using Wex1.Elephant.Logger.Core.Entities;
using Wex1.Elephant.Logger.Core.Interfaces.Repositories;


namespace Wex.Elephant.Logger.Infrastructure.Repositories
{
    public class LogsRepositoryBase<T> : ILogsRepositorybase<T> where T : BaseLog
    {

        protected readonly MongoClient _client;
        private string _collectionName;
        protected IMongoCollection<T> _collection;
        public LogsRepositoryBase(string collectionName)
        {
            _collectionName = collectionName;
            _client = new MongoClient(Constants.MongoDbConnectionUrl);
            _collection = _client.GetDatabase("Logger").GetCollection<T>(_collectionName);
        }
        public IMongoCollection<T> GetAll()
        {
            return _collection;
        }
        public async Task<IEnumerable<T>> GetListAsync()
        {
            return await _collection.Find(_ => true).ToListAsync();
        }
        public async Task<T> GetByIdAsync(ObjectId id)
        {
            var filter = Builders<T>.Filter
                .Eq(T => T.Id, id);

            return await _collection.Find(filter).FirstOrDefaultAsync();
        }

        public async Task AddAsync(T entity)
        {
            await _collection.InsertOneAsync(entity);
        }

        public Task<bool> UpdateAsync(T entity)
        {
            throw new NotImplementedException();
        }

        public Task<bool> DeleteAsync(T entity)
        {
            throw new NotImplementedException();
        }

        public async Task<IEnumerable<T>> GetPagedData(IEnumerable<T> data, int pageNumber, int pageSize)
        {
            return data
                .Skip((pageNumber - 1) * pageSize)
                .Take(pageSize)
                .ToList();
        }


    }
}
