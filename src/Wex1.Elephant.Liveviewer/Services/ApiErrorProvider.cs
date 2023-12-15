using System.Globalization;
using Wex1.Elephant.Liveviewer.Dto;
using Wex1.Elephant.Liveviewer.Model;
using Wex1.Elephant.Liveviewer.Services.Interfaces;
using Wex1.Elephant.Liveviewer.Services.Mapper;

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

        public async Task<PageDto<ErrorDto>> GetPage(int pageNumber, int pageSize, DateOnly? selectedDate, bool sortDirection)
        {
            DateTime? selectedDateTime = 
                selectedDate?.ToString() != null 
                ? DateTime.Parse(selectedDate.ToString()) 
                : null;

            var url = $"ErrorLogs?PageNumber={pageNumber}&PageSize={pageSize}&SelectedDate={selectedDateTime}&NewestFirst={sortDirection}";

            return await _httpClient.GetFromJsonAsync<PageDto<ErrorDto>>(url);
        }

    }
}
