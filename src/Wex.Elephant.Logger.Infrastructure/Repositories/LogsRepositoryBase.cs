using MongoDB.Bson;
using MongoDB.Driver;
using Wex1.Elephant.Logger.Core;
using Wex1.Elephant.Logger.Core.Entities;
using Wex1.Elephant.Logger.Core.Filters;
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

        public async Task<IEnumerable<T>> GetPagedData(int pageNumber, int pageSize, DateTime? selectedDate, bool newestFirst)
        {

            var sortFilter = newestFirst
                ? Builders<T>.Sort.Descending("timestamp")
                : Builders<T>.Sort.Ascending("timestamp");

            if (selectedDate is null)
            {
                return _collection
                .Find(_ => true)
                .Sort(sortFilter)
                .Limit(pageSize)
                .Skip((pageNumber - 1) * pageSize)
                .ToList();
            }
            else
            {

                var dateFilter = Builders<T>.Filter.Gte("timestamp", BsonDateTime.Create(selectedDate.Value)) &
                     Builders<T>.Filter.Lt("timestamp", BsonDateTime.Create(selectedDate.Value.AddDays(1)));

                return _collection
               .Find(dateFilter)
               .Sort(sortFilter)
               .Limit(pageSize)
               .Skip((pageNumber - 1) * pageSize)
               .ToList();
            }

        }

        public async Task<long> CountRecords(DateTime? selectedDate)
        {
            if (selectedDate is null)
            {
                return await _collection.CountAsync(_ => true);
            }

            else
            {
                var dateFilter = Builders<T>.Filter.Gte("timestamp", BsonDateTime.Create(selectedDate.Value)) &
                    Builders<T>.Filter.Lt("timestamp", BsonDateTime.Create(selectedDate.Value.AddDays(1)));

                return await _collection.CountAsync(dateFilter);
            }

        }
    }
}
