using MongoDB.Bson;
using Wex1.Elephant.Liveviewer.Model;

namespace Wex1.Elephant.Liveviewer.Services.Interfaces
{
    public interface IApiLogProvider<T> where T : Baselog
    {
        Task<IEnumerable<T>> GetAll(int pageNumber, int pageSize);
        Task<T> Get(string id);

    }
}
