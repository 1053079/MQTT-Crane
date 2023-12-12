using Wex1.Elephant.Liveviewer.Dto;
using Wex1.Elephant.Liveviewer.Model;
using Wex1.Elephant.Liveviewer.Services.Interfaces;

namespace Wex1.Elephant.Liveviewer.Services
{
    public class ApiSpeedProvider : IApiSpeedLogProvider
    {
        private readonly HttpClient _httpClient;

        public ApiSpeedProvider(HttpClient httpClient)
        {
            _httpClient = httpClient;
            _httpClient.BaseAddress = new Uri(LiveviewerConstants.BaseUrl);
        }

        public async Task<SpeedLog> Get(string id)
        {
            var dto = await _httpClient.GetFromJsonAsync<SpeedDto>($"/SpeedLogs?Id={id}");
            var speedLog = new SpeedLog
            {
                Id = dto.Id,
                Component = dto.Component,
                Type = dto.Type,
                Timestamp = dto.Timestamp,
                Description = dto.Description,
                Speed = dto.Speed
            };
            return speedLog;
        }

        public async Task<IEnumerable<SpeedLog>> GetAll(int pageNumber, int pageSize)
        {

            var dtos = await _httpClient.GetFromJsonAsync<PageDto<SpeedDto>>($"SpeedLogs?PageNumber={pageNumber}&PageSize={pageSize}");

            var speedLogs = dtos.Data.Select(sl => new SpeedLog
            {
                Id = sl.Id,
                Description = sl.Description,
                Component = sl.Component,
                Timestamp = sl.Timestamp,
                Type = sl.Type
            });

            return speedLogs;
        }
    }
}
