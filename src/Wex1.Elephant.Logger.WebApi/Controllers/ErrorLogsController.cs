using Microsoft.AspNetCore.Mvc;
using MongoDB.Bson;
using Wex1.Elephant.Logger.Core.Filters;
using Wex1.Elephant.Logger.Core.Interfaces.Services.CrudService;

namespace Wex1.Elephant.Logger.WebApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ErrorLogsController : ControllerBase
    {

        private readonly IErrorLogCrudService _errorLogCrudService;

        public ErrorLogsController(IErrorLogCrudService errorLogCrudService)
        {
            _errorLogCrudService = errorLogCrudService;
        }

        [HttpGet]
        public async Task<IActionResult> Get([FromQuery] PaginationFilter paginationFilter, [FromQuery] DateFilter dateFilter)
        {
            return await _errorLogCrudService.GetAllPaged(filter, Request);
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetById(string id)
        {
            return await _errorLogCrudService.GetById(ObjectId.Parse(id));
            return await _errorLogService.GetAllPaged(paginationFilter, dateFilter, Request);
        }

    }
}
