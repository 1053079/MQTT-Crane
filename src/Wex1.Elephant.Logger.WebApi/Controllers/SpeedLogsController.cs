using Microsoft.AspNetCore.Mvc;
using MongoDB.Bson;
using Wex1.Elephant.Logger.Core.Filters;
using Wex1.Elephant.Logger.Core.Interfaces.Services.CrudService;

namespace Wex1.Elephant.Logger.WebApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class SpeedLogsController : ControllerBase
    {
        private readonly ISpeedLogCrudService _speedLogCrudService;

        public SpeedLogsController(ISpeedLogCrudService speedLogCrudService)
        {
            _speedLogCrudService = speedLogCrudService;
        }

        [HttpGet]
        public async Task<IActionResult> Get([FromQuery] PaginationFilter filter)
        {
            return await _speedLogCrudService.GetAllPaged(filter, Request);
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetById(string id)
        {
            return await _speedLogCrudService.GetById(ObjectId.Parse(id));
        }
    }
}
