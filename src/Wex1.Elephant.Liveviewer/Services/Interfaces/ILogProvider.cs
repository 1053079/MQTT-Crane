using MongoDB.Bson;
using Wex1.Elephant.Liveviewer.Model;
using Wex1.Elephant.Logger.Core.Entities;

namespace Wex1.Elephant.Liveviewer.Services.Interfaces
{
    public interface ILogProvider<T> where T : class
    {
        Task<IEnumerable<T>> GetAll(/*int pageNumber, int pageSize*/);
        Task<T> Get(string id);

    }
}
