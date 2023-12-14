using Microsoft.AspNetCore.Mvc;
using MongoDB.Bson;
using Wex1.Elephant.Logger.Core.Filters;
using Wex1.Elephant.Logger.Core.Interfaces.Services.CrudService;

namespace Wex1.Elephant.Logger.WebApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PositionLogsController : ControllerBase
    {
        private readonly IPositionLogCrudService _positionLogCrudService;

        public PositionLogsController(IPositionLogCrudService positionLogCrudService)
        {
            _positionLogCrudService = positionLogCrudService;
        }

        [HttpGet]
        public Task<IActionResult> Get([FromQuery] PaginationFilter paginationFilter, [FromQuery] DateFilter dateFilter)
        {
            var today = DateOnly.FromDateTime(DateTime.UtcNow);
            return _positionLogCrudService.GetAllPaged(paginationFilter, dateFilter, Request);
        }
        [HttpGet("{id}")]
        public async Task<IActionResult> GetById(string id)
        {
            return await _positionLogCrudService.GetById(ObjectId.Parse(id));
        }
    }
}
