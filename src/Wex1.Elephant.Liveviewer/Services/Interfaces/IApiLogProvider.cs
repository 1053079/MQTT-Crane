using MongoDB.Bson;
using Wex1.Elephant.Liveviewer.Dto;
using Wex1.Elephant.Liveviewer.Model;

namespace Wex1.Elephant.Liveviewer.Services.Interfaces
{
    public interface IApiLogProvider<T, TDto> where T : Baselog where TDto : class
    {
        Task<PageDto<TDto>> GetPage(int pageNumber, int pageSize);
        Task<T> Get(string id);

    }
}
