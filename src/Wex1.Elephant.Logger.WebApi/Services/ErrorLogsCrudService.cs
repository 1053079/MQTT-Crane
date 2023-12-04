using Microsoft.AspNetCore.Mvc;
using Wex1.Elephant.Logger.Core.Dto.ErrorLogs;
using Wex1.Elephant.Logger.Core.Filters;
using Wex1.Elephant.Logger.Core.Interfaces.Repositories;
using Wex1.Elephant.Logger.Core.Interfaces.Services;
using Wex1.Elephant.Logger.Core.Interfaces.Services.CrudService;
using Wex1.Elephant.Logger.WebApi.Helpers;
using Wex1.Elephant.Logger.WebApi.Wrappers.Mapper;

namespace Wex1.Elephant.Logger.WebApi.Services
{
    public class ErrorLogsCrudService : IErrorLogCrudService
    {
        private readonly IErrorLogRepository _errorLogRepository;
        private readonly IUriService _uriService;

        public ErrorLogsCrudService(
            IErrorLogRepository errorLogRepository,
            IUriService uriService)
        {
            _errorLogRepository = errorLogRepository;
            _uriService = uriService;
        }

        public async Task<IActionResult> GetAllPaged(PaginationFilter filter, HttpRequest request)
        {
            var errorLogs = await _errorLogRepository.GetListAsync();

            var route = request.Path.Value;
            var validFilter = new PaginationFilter(filter.PageNumber, filter.PageSize);

            var pagedData = await _errorLogRepository.GetPagedData(errorLogs, validFilter.PageNumber, validFilter.PageSize);
            var totalRecords = errorLogs.Count();

            if(totalRecords <= 0)
            {
                return new NotFoundObjectResult("No error logs were found.");
            }

            var pagedResponse = PaginationHelper.CreatePagedReponse(pagedData.MapToDto(), validFilter, totalRecords, _uriService, route);

            return new OkObjectResult(pagedResponse);
        }
        public Task<IActionResult> GetById(Guid id)
        {
            throw new NotImplementedException();
        }

        public Task<IActionResult> Add(ErrorLogRequestDto dto)
        {
            throw new NotImplementedException();
        }
        public Task<IActionResult> Update(ErrorLogRequestDto dto)
        {
            throw new NotImplementedException();
        }

        public Task<IActionResult> Delete(Guid id)
        {
            throw new NotImplementedException();
        }

       

        
    }
}
