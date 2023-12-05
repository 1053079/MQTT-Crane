using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using MongoDB.Bson;
using Wex1.Elephant.Logger.Core.Filters;

namespace Wex1.Elephant.Logger.Core.Interfaces.Services.CrudService
{
    public interface ICrudService<TDto> where TDto : class
    {
        Task<IActionResult> GetById(ObjectId id);
        Task<IActionResult> GetAllPaged(PaginationFilter filter, HttpRequest request);
        Task<IActionResult> Add(TDto dto);
        Task<IActionResult> Update(TDto dto);
        Task<IActionResult> Delete(ObjectId id);
    }
}
