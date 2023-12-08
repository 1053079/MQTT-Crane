using Microsoft.AspNetCore.Mvc;
using MongoDB.Bson;
using Wex1.Elephant.Logger.Core.Dto.SpeedLogs;
using Wex1.Elephant.Logger.Core.Filters;
using Wex1.Elephant.Logger.Core.Interfaces.Repositories;
using Wex1.Elephant.Logger.Core.Interfaces.Services;
using Wex1.Elephant.Logger.Core.Interfaces.Services.CrudService;
using Wex1.Elephant.Logger.WebApi.Helpers;
using Wex1.Elephant.Logger.WebApi.Wrappers.Mapper;

namespace Wex1.Elephant.Logger.WebApi.Services.CrudServices
{
    public class SpeedLogsCrudService : ISpeedLogCrudService
    {
        private readonly ISpeedLogRepository _speedLogRepository;
        private readonly IUriService _uriService;

        public SpeedLogsCrudService(
            ISpeedLogRepository speedLogRepository,
            IUriService uriService)
        {
            _speedLogRepository = speedLogRepository;
            _uriService = uriService;
        }

        public async Task<IActionResult> GetAllPaged(PaginationFilter filter, HttpRequest request)
        {
            var route = request.Path.Value;
            var validFilter = new PaginationFilter(filter.PageNumber, filter.PageSize);

            var pagedData = await _speedLogRepository.GetPagedData(validFilter.PageNumber, validFilter.PageSize);
            var totalRecords = await _speedLogRepository.CountRecords();

            if (totalRecords < 0)
            {
                return new NotFoundObjectResult("No speed logs were found.");
            }

            var pagedResponse = PaginationHelper.CreatePagedReponse(pagedData.MapToDto(), validFilter, totalRecords, _uriService, route);

            return new OkObjectResult(pagedResponse);

        }

        public Task<IActionResult> GetById(ObjectId id)
        {
            throw new NotImplementedException();
        }
        public Task<IActionResult> Add(SpeedLogsRequestDto dto)
        {
            throw new NotImplementedException();
        }
        public Task<IActionResult> Update(SpeedLogsRequestDto dto)
        {
            throw new NotImplementedException();
        }

        public Task<IActionResult> Delete(ObjectId id)
        {
            throw new NotImplementedException();
        }

    }
}
