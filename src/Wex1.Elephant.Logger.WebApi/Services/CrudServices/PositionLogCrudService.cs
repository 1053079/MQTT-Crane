using Microsoft.AspNetCore.Mvc;
using MongoDB.Bson;
using Wex.Elephant.Logger.Infrastructure.Repositories;
using Wex1.Elephant.Logger.Core.Dto.PositionLogs;
using Wex1.Elephant.Logger.Core.Filters;
using Wex1.Elephant.Logger.Core.Interfaces.Repositories;
using Wex1.Elephant.Logger.Core.Interfaces.Services;
using Wex1.Elephant.Logger.Core.Interfaces.Services.CrudService;
using Wex1.Elephant.Logger.WebApi.Helpers;
using Wex1.Elephant.Logger.WebApi.Wrappers.Mapper;

namespace Wex1.Elephant.Logger.WebApi.Services.CrudServices
{
    public class PositionLogCrudService : IPositionLogCrudService
    {
        private readonly IPositionLogRepository _positionLogRepository;
        private readonly IUriService _uriService;

        public PositionLogCrudService(
            IPositionLogRepository positionLogRepository,
            IUriService uriService)
        {
            _positionLogRepository = positionLogRepository;
            _uriService = uriService;
        }

        public async Task<IActionResult> GetAllPaged(PaginationFilter paginationFilter, DateFilter dateFilter, HttpRequest request)
        {
            var route = request.Path.Value;
            var validPageFilter = new PaginationFilter(paginationFilter.PageNumber, paginationFilter.PageSize);
            var validDateFilter = new DateFilter(dateFilter.SelectedDate, dateFilter.NewestFirst);
            var pagedData = await _positionLogRepository.GetPagedData(validPageFilter.PageNumber, validPageFilter.PageSize, validDateFilter.SelectedDate, validDateFilter.NewestFirst);
            var totalRecords = await _positionLogRepository.CountRecords(validDateFilter.SelectedDate);

            if (totalRecords <= 0)
            {
                return new NotFoundObjectResult("No position logs were found.");
            }

            var pagedResponse = PaginationHelper.CreatePagedReponse(pagedData.MapToDto(), validPageFilter, totalRecords, _uriService, route);
            return new OkObjectResult(pagedResponse);
        }

        public async Task<IActionResult> GetById(ObjectId id)
        {
            var positionLog = await _positionLogRepository.GetByIdAsync(id);

            if (positionLog is null)
                return new NotFoundObjectResult($"PositionLog with id: {id} couldn't be found!");

            return new OkObjectResult(positionLog.MapToDto());
        }

        public Task<IActionResult> Add(PositionLogRequestDto dto)
        {
            throw new NotImplementedException();
        }

        public Task<IActionResult> Update(PositionLogRequestDto dto)
        {
            throw new NotImplementedException();
        }

        public Task<IActionResult> Delete(ObjectId id)
        {
            throw new NotImplementedException();
        }

    }
}
