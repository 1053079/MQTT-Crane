using Wex1.Elephant.Liveviewer.Dto;
using Wex1.Elephant.Liveviewer.Services.Interfaces;
using PositionLog = Wex1.Elephant.Liveviewer.Model.PositionLog;

namespace Wex1.Elephant.Liveviewer.Services
{
    public class ApiPositionProvider : IApiPositionLogProvider
    {
        private readonly HttpClient _httpClient;

        public ApiPositionProvider(HttpClient httpClient)
        {
            _httpClient = httpClient;
            _httpClient.BaseAddress = new Uri(LiveviewerConstants.BaseUrl);
        }

        public async Task<PositionLog> Get(string id)
        {
            var dto = await _httpClient.GetFromJsonAsync<PositionDto>($"/PositionLogs?Id={id}");
            var positionLog = new PositionLog
            {
                Id = dto.Id,
                Component = dto.Component,
                Type = dto.Type,
                Timestamp = dto.Timestamp,
                Description = dto.Description,
                PositionX = dto.PositionX,
                PositionY = dto.PositionY,
                PositionZ = dto.PositionZ
            };
            return positionLog;
        }

        public async Task<PageDto<PositionDto>> GetPage(int pageNumber, int pageSize)
        {
            return await _httpClient.GetFromJsonAsync<PageDto<PositionDto>>($"PositionLogs?PageNumber={pageNumber}&PageSize={pageSize}");
        }
    }
}
