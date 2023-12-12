using Wex1.Elephant.Liveviewer.Dto;
using Wex1.Elephant.Liveviewer.Model;
using Wex1.Elephant.Liveviewer.Services.Interfaces;

namespace Wex1.Elephant.Liveviewer.Services
{
    public class ApiErrorProvider : IApiErrorLogProvider
    {
        private readonly HttpClient _httpClient;

        public ApiErrorProvider(HttpClient httpClient)
        {
            _httpClient = httpClient;
            _httpClient.BaseAddress = new Uri(LiveviewerConstants.BaseUrl);
        }

        public async Task<ErrorLog> Get(string id)
        {
            var dto = await _httpClient.GetFromJsonAsync<ErrorDto>($"/ErrorLogs?Id={id}");
            var errorLog = new ErrorLog
            {
                Id = dto.Id,
                Component = dto.Component,
                Type = dto.Type,
                Timestamp = dto.Timestamp,
                Description = dto.Description
            };
            return errorLog;
        }

        public async Task<IEnumerable<ErrorLog>> GetAll(int pageNumber, int pageSize)
        {

            var dtos = await _httpClient.GetFromJsonAsync<PageDto<ErrorDto>>($"ErrorLogs?PageNumber={pageNumber}&PageSize={pageSize}");
           
            var errorLogs = dtos.Data.Select(el => new ErrorLog
            {
                Id = el.Id,
                Description = el.Description,
                Component = el.Component,
                Timestamp = el.Timestamp,
                Type = el.Type
            });

            return errorLogs;
        }
    }
}
