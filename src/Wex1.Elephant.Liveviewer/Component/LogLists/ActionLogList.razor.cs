using Microsoft.AspNetCore.Components;
using Wex1.Elephant.Liveviewer.Model;
using Wex1.Elephant.Liveviewer.Pages;
using Wex1.Elephant.Liveviewer.Services.Interfaces;
using Wex1.Elephant.Liveviewer.Services.Mapper;

namespace Wex1.Elephant.Liveviewer.Component.LogLists
{
    public partial class ActionLogList
    {
        private ActionLog[] ActionLogs;

        private string ErrorMessage;
        private bool IsError;

        private int currentPageNumber = 1;
        private int pageSize = 30;
        private int totalPages;

        private DateOnly? selectedDate, minDate, maxDate;
        private bool sortDirection;

        [Inject]
        private IApiActionLogProvider _actionLogProvider { get; set; }

        protected override async Task OnInitializedAsync()
        {
            selectedDate = null;
            minDate = DateOnly.FromDateTime(DateTime.UtcNow.AddYears(-5));
            maxDate = DateOnly.FromDateTime(DateTime.UtcNow);
            sortDirection = true;
            await FetchActionLogs();
        }

        private async Task HandlePageChangeAsync(int newPageNumber)
        {
            await Task.Run(() => { currentPageNumber = newPageNumber; });
            await FetchActionLogs();
        }
        private async Task HandleDateChangeAsync(DateOnly? value)
        {
            if (selectedDate != value || value == null)
            {
                selectedDate = value;
                currentPageNumber = 1;
                await FetchActionLogs();
            }
        }

        public async Task HandleSortDirectionChange(ChangeEventArgs e)
        {
            sortDirection = bool.Parse(e.Value.ToString());
            FetchActionLogs();
        }


        private async Task FetchActionLogs()
        {
            try
            {
                IsError = false;
                try
                {
                    ActionLogs = null;
                    await Task.Delay(500);
                    var pageDto = await _actionLogProvider.GetPage(currentPageNumber, pageSize, selectedDate, sortDirection);
                    ActionLogs = pageDto.Data.MapToLog().ToArray();
                    totalPages = pageDto.TotalPages;
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
                ErrorMessage = $"Actionlogs could not be shown due to an error: \n {ex.Message}";

            }

        }
    }
}
