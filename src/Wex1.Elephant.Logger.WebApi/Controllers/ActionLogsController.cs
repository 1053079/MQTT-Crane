using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Wex1.Elephant.Logger.Core.Filters;
using Wex1.Elephant.Logger.Core.Interfaces.Services.CrudService;

namespace Wex1.Elephant.Logger.WebApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ActionLogsController : ControllerBase
    {
        private readonly IActionLogCrudService _actionLogCrudService;

        public ActionLogsController(IActionLogCrudService actionLogCrudService)
        {
            _actionLogCrudService = actionLogCrudService;
        }

        [HttpGet]
        public async Task<IActionResult> Get([FromQuery] PaginationFilter filter)
        {
            return await _actionLogCrudService.GetAllPaged(filter, Request);
        }

    }
}
