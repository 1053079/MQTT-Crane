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

        [Inject]
        private IApiErrorLogProvider _errorLogProvider { get; set; }

        protected override async Task OnInitializedAsync()
        {
            await FetchErrorLogs();
        }

        private async Task HandlePageChangeAsync(int newPageNumber)
        {
            await Task.Run(() => { currentPageNumber = newPageNumber; }) ;
            await FetchErrorLogs();
        }

        private async Task FetchErrorLogs()
        {
            try
            {
                IsError = false;
                try
                {
                    var pageDto = await _errorLogProvider.GetPage(currentPageNumber, pageSize);
                    totalPages = pageDto.TotalPages;
                    ErrorLogs = pageDto.Data.MapToLog().ToArray();
                    await InvokeAsync(StateHasChanged);
                } catch(Exception ex)
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
