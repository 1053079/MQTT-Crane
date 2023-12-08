using Wex1.Elephant.Liveviewer.Dto;
using Wex1.Elephant.Liveviewer.Model;
using Wex1.Elephant.Liveviewer.Services.Interfaces;
using Wex1.Elephant.Logger.Core.Interfaces.Repositories;

namespace Wex1.Elephant.Liveviewer.Services
{
    public class ApiActionProvider : IApiActionLogProvider
    {
        private readonly HttpClient _httpClient;

        public ApiActionProvider(HttpClient httpClient)
        {
            _httpClient = httpClient;
            _httpClient.BaseAddress = new Uri(LiveviewerConstants.BaseUrl);
        }

        public async Task<ActionLog> Get(string id)
        {
            var dto = await _httpClient.GetFromJsonAsync<ActionDto>($"ActionLogs?Id={id}");
            var actionlog = new ActionLog
            {
                Id = dto.Id,
                Component = dto.Component,
                Type = dto.Type,
                Timestamp = dto.Timestamp,
                Description = dto.Description
            };
            return actionlog;
        }

        public async Task<IEnumerable<ActionLog>> GetAll(int pageNumber, int pageSize)
        {
            var dtos = await _httpClient.GetFromJsonAsync<PageDto<ActionDto>>($"ActionLogs?PageNumber={pageNumber}&PageSize={pageSize}");
            var actionlogs = dtos.Data.Select(el => new ActionLog
            {
                Id = el.Id,
                Description = el.Description,
                Component = el.Component,
                Timestamp = el.Timestamp,
                Type = el.Type
            });

            return actionlogs;
        }
    }
}
