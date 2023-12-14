using Microsoft.AspNetCore.Components;
using Wex1.Elephant.Liveviewer.Model;
using Wex1.Elephant.Liveviewer.Services.Interfaces;
using Wex1.Elephant.Liveviewer.Services.Mapper;

namespace Wex1.Elephant.Liveviewer.Component.LogLists
{
    public partial class SpeedLogList
    {
        private SpeedLog[] SpeedLogs;
        private string ErrorMessage;
        private bool IsError;

        private int currentPageNumber = 1;
        private int pageSize = 30;
        private int totalPages;

        [Inject]
        private IApiSpeedLogProvider _speedLogProvider { get; set; }

        protected override async Task OnInitializedAsync()
        {
            await FetchSpeedLogs();
        }

        private async Task HandlePageChangeAsync(int newPageNumber)
        {
            await Task.Run(() => { currentPageNumber = newPageNumber; });
            await FetchSpeedLogs();
        }

        private async Task FetchSpeedLogs()
        {
            try
            {
                IsError = false;
                try
                {
                    var pageDto = await _speedLogProvider.GetPage(currentPageNumber, pageSize);
                    totalPages = pageDto.TotalPages;
                    SpeedLogs = pageDto.Data.MapToLog().ToArray();
                    await InvokeAsync(StateHasChanged);
                }
                catch(Exception ex)
                {
                    IsError = true;
                    ErrorMessage = ex.Message;
                }
                
            }
            catch (Exception ex)
            {
                IsError = true;

                ErrorMessage = $"Speedlogs could not be shown due to an error: \n {ex.Message}";

            }
        }
    }
}
