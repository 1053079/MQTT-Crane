using Microsoft.AspNetCore.Mvc;
using MongoDB.Bson;
using Wex.Elephant.Logger.Infrastructure.Repositories;
using Wex1.Elephant.Logger.Core.Dto.Actionlogs;
using Wex1.Elephant.Logger.Core.Filters;
using Wex1.Elephant.Logger.Core.Interfaces.Repositories;
using Wex1.Elephant.Logger.Core.Interfaces.Services;
using Wex1.Elephant.Logger.Core.Interfaces.Services.CrudService;
using Wex1.Elephant.Logger.WebApi.Helpers;
using Wex1.Elephant.Logger.WebApi.Wrappers.Mapper;

namespace Wex1.Elephant.Logger.WebApi.Services.CrudServices
{
    public class ActionLogsCrudService : IActionLogCrudService
    {
        private readonly IActionLogRepository _actionLogRepository;
        private readonly IUriService _uriService;

        public ActionLogsCrudService(
            IActionLogRepository actionLogRepository,
            IUriService uriService)
        {
            _actionLogRepository = actionLogRepository;
            _uriService = uriService;
        }

        public async Task<IActionResult> GetAllPaged(PaginationFilter paginationFilter, DateFilter dateFilter, HttpRequest request)
        {
            var route = request.Path.Value;
            var validPageFilter = new PaginationFilter(paginationFilter.PageNumber, paginationFilter.PageSize);
            var validDateFilter = new DateFilter(dateFilter.SelectedDate, dateFilter.NewestFirst);
            var pagedData = await _actionLogRepository.GetPagedData(validPageFilter.PageNumber, validPageFilter.PageSize, validDateFilter.SelectedDate, validDateFilter.NewestFirst);
            var totalRecords = await _actionLogRepository.CountRecords(validDateFilter.SelectedDate);

            if (totalRecords <= 0)
            {
                return new NotFoundObjectResult("No speed logs were found!");
            }

            var pagedResponse = PaginationHelper.CreatePagedReponse(pagedData.MapToDto(), validPageFilter, totalRecords, _uriService, route);
            return new OkObjectResult(pagedResponse);
        }


        public async Task<IActionResult> GetById(ObjectId id)
        {
            var actionLog = await _actionLogRepository.GetByIdAsync(id);

            if (actionLog is null)
                return new NotFoundObjectResult($"ActionLog with id: {id} couldn't be found!");

            return new OkObjectResult(actionLog.MapToDto());
        }

        public Task<IActionResult> Add(ActionLogRequestDto dto)
        {
            throw new NotImplementedException();
        }
        public Task<IActionResult> Update(ActionLogRequestDto dto)
        {
            throw new NotImplementedException();
        }

        public Task<IActionResult> Delete(ObjectId id)
        {
            throw new NotImplementedException();
        }



    }
}
