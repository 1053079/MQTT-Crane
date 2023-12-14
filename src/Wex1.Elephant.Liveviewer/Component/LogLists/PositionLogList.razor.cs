using Microsoft.AspNetCore.Components;
using Wex1.Elephant.Liveviewer.Model;
using Wex1.Elephant.Liveviewer.Services.Interfaces;
using Wex1.Elephant.Liveviewer.Services.Mapper;

namespace Wex1.Elephant.Liveviewer.Component.LogLists
{
    public partial class PositionLogList
    {
        private PositionLog[] PositionLogs;
        private string ErrorMessage;
        private bool IsError;


        private int currentPageNumber = 1;
        private int pageSize = 30;
        private int totalPages;

        [Inject]
        private IApiPositionLogProvider _positionLogProvider { get; set; }

        protected override async Task OnInitializedAsync()
        {
            await FetchPositionLogs();
        }
        private async Task HandlePageChangeAsync(int newPageNumber)
        {
            await Task.Run(() => { currentPageNumber = newPageNumber; });
            await FetchPositionLogs();
        }
        private async Task FetchPositionLogs()
        {
            try
            {
                IsError = false;
                var pageDto = await _positionLogProvider.GetPage(currentPageNumber, pageSize);
                PositionLogs = pageDto.Data.MapToLog().ToArray();
            }
            catch (Exception ex)
            {
                IsError = true;
                ErrorMessage = $"Positionlogs could not be shown due to an error: \n {ex.Message}";

            }
        }
        
    }
}
