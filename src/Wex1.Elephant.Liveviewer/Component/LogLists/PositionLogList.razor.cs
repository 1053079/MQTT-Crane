using Microsoft.AspNetCore.Components;
using Wex1.Elephant.Liveviewer.Model;
using Wex1.Elephant.Liveviewer.Pages;
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

        private DateOnly? selectedDate, minDate, maxDate;
        private bool sortDirection;

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

        private async Task HandleDateChangeAsync(DateOnly? value)
        {
            if (selectedDate != value || value == null)
            {
                selectedDate = value;
                await FetchPositionLogs();
            }
        }

        public async Task HandleSortDirectionChange(ChangeEventArgs e)
        {
            sortDirection = bool.Parse(e.Value.ToString());
            FetchPositionLogs();
        }

        private async Task FetchPositionLogs()
        {
            try
            {
                PositionLogs = null;
                await Task.Delay(500);
                IsError = false;
                var pageDto = await _positionLogProvider.GetPage(currentPageNumber, pageSize, selectedDate, sortDirection);
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
