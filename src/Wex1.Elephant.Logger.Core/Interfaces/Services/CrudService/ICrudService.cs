using Amazon.Runtime;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Wex1.Elephant.Logger.Core.Filters;

namespace Wex1.Elephant.Logger.Core.Interfaces.Services.CrudService
{
    public interface ICrudService<TDto> where TDto : class
    {
        Task<IActionResult> GetById(Guid id);
        Task<IActionResult> GetAllPaged(PaginationFilter filter, HttpRequest request);
        Task<IActionResult> Add(TDto dto);
        Task<IActionResult> Update(TDto dto);
        Task<IActionResult> Delete(Guid id);
    }
}
