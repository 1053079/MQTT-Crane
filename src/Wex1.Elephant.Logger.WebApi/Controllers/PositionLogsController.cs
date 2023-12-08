using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
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
        public Task<IActionResult> Get([FromQuery]PaginationFilter filter)
        {
            return _positionLogCrudService.GetAllPaged(filter, Request);
        }
    }
}
