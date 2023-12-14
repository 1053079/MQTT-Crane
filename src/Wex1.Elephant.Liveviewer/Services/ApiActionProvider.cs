using Wex1.Elephant.Liveviewer.Dto;
using Wex1.Elephant.Liveviewer.Model;
using Wex1.Elephant.Liveviewer.Services.Interfaces;

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
            var actionLog = new ActionLog
            {
                Id = dto.Id,
                Component = dto.Component,
                Type = dto.Type,
                Timestamp = dto.Timestamp,
                Description = dto.Description
            };
            return actionLog;
        }

        public async Task<PageDto<ActionDto>> GetPage(int pageNumber, int pageSize)
        {
            return await _httpClient.GetFromJsonAsync<PageDto<ActionDto>>($"ActionLogs?PageNumber={pageNumber}&PageSize={pageSize}");
        }
    }
}
