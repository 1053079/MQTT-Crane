using Microsoft.AspNetCore.Mvc;
using MongoDB.Bson;
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

        public async Task<IActionResult> GetAllPaged(PaginationFilter filter, HttpRequest request)
        {
            var route = request.Path.Value;
            var validFilter = new PaginationFilter(filter.PageNumber, filter.PageSize);

            var pagedData = await _actionLogRepository.GetPagedData(validFilter.PageNumber, validFilter.PageSize);
            var totalRecords = await _actionLogRepository.CountRecords();

            if (totalRecords < 0)
            {
                return new NotFoundObjectResult("No speed logs were found!");
            }

            var pagedResponse = PaginationHelper.CreatePagedReponse(pagedData.MapToDto(), validFilter, totalRecords, _uriService, route);
            return new OkObjectResult(pagedResponse);
        }


        public Task<IActionResult> GetById(ObjectId id)
        {
            throw new NotImplementedException();
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
