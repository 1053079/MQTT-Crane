using Microsoft.AspNetCore.Components;
using Wex1.Elephant.Liveviewer.Model;
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

        [Inject]
        private IApiActionLogProvider _actionLogProvider { get; set; }

        protected override async Task OnInitializedAsync()
        {
            await FetchActionLogs();
        }

        private async Task HandlePageChangeAsync(int newPageNumber)
        {
            await Task.Run(() => { currentPageNumber = newPageNumber; });
            await FetchActionLogs();
        }

        private async Task FetchActionLogs()
        {
            try
            {
                IsError = false;
                try
                {
                    var pageDto = await _actionLogProvider.GetPage(currentPageNumber, pageSize);
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
