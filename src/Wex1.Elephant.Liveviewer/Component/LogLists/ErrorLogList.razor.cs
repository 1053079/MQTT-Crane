using BlazorBootstrap;
using Microsoft.AspNetCore.Components;
using Wex1.Elephant.Liveviewer.Model;
using Wex1.Elephant.Liveviewer.Services.Interfaces;
using Wex1.Elephant.Liveviewer.Services.Mapper;

namespace Wex1.Elephant.Liveviewer.Component.LogLists
{
    public partial class ErrorLogList
    {
        private ErrorLog[] ErrorLogs;

        private string ErrorMessage;
        private bool IsError;

        private int currentPageNumber = 1;
        private int pageSize = 30;
        private int totalPages;

        private DateOnly? selectedDate, minDate, maxDate;
        private bool sortDirection;

        [Inject]
        private IApiErrorLogProvider _errorLogProvider { get; set; }
        [Inject] 
        protected PreloadService PreloadService { get; set; }
        protected override async Task OnInitializedAsync()
        {
            selectedDate = null;
            minDate = DateOnly.FromDateTime(DateTime.UtcNow.AddYears(-5));
            maxDate = DateOnly.FromDateTime(DateTime.UtcNow);
            sortDirection = true;
            await FetchErrorLogs();
        }

        private async Task HandlePageChangeAsync(int newPageNumber)
        {
            await Task.Run(() => { currentPageNumber = newPageNumber; });
            await FetchErrorLogs();
        }

        private async Task HandleDateChangeAsync(DateOnly? value)
        {
            if(selectedDate!= value || value == null)
            {
                selectedDate = value;
                currentPageNumber = 1;
                await FetchErrorLogs();
            }
        }

        public async Task HandleSortDirectionChange(ChangeEventArgs e)
        {
            sortDirection = bool.Parse(e.Value.ToString());
            FetchErrorLogs();
        }

        private async Task FetchErrorLogs()
        {
            try
            {
                IsError = false;
                try
                {
                    ErrorLogs = null;
                    await Task.Delay(500);
                    var pageDto = await _errorLogProvider.GetPage(currentPageNumber, pageSize, selectedDate, sortDirection);
                    totalPages = pageDto.TotalPages;
                    ErrorLogs = pageDto.Data.MapToLog().ToArray();
                    await InvokeAsync(StateHasChanged);
                }
                catch (Exception ex)
                {
                    IsError = true;
                    ErrorMessage = ex.Message;
                }
               

            }
            catch (Exception ex)
            {
                IsError = true;
                ErrorMessage = $"Errorlogs could not be shown due to an error: \n {ex.Message}";

            }

        }
    }
}
