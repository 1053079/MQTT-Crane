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

        private readonly IErrorLogCrudService _errorLogService;

        public ErrorLogsController(IErrorLogCrudService errorLogService)
        {
            _errorLogService = errorLogService;
        }

        [HttpGet]
        public async Task<IActionResult> Get([FromQuery] PaginationFilter filter)
        {
            return await _errorLogService.GetAllPaged(filter, Request);
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetById(ObjectId id)
        {
            return await _errorLogService.GetById(id);
        }

    }
}
