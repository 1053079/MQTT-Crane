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

        public async Task<PageDto<SpeedDto>> GetPage(int pageNumber, int pageSize, DateOnly? selectedDate, bool sortDirection)
        {

            DateTime? selectedDateTime =
                selectedDate?.ToString() != null
                ? DateTime.Parse(selectedDate.ToString())
                : null;

            var url = $"SpeedLogs?PageNumber={pageNumber}&PageSize={pageSize}&SelectedDate={selectedDateTime}&NewestFirst={sortDirection}";

            return await _httpClient.GetFromJsonAsync<PageDto<SpeedDto>>(url);

            
        }
    }
}
