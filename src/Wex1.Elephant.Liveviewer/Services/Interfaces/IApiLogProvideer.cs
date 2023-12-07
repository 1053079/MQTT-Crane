using MongoDB.Bson;
using Wex1.Elephant.Logger.Core.Entities;

namespace Wex1.Elephant.Liveviewer.Services.Interfaces
{
    public interface IApiLogProvider<T> where T : BaseLog
    {
        Task<IEnumerable<T>> GetAll(/*int pageNumber, int pageSize*/);
        Task<T> Get(ObjectId id);

    }
}
