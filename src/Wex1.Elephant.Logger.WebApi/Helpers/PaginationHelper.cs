using Wex1.Elephant.Logger.Core.Filters;
using Wex1.Elephant.Logger.Core.Interfaces.Services;
using Wex1.Elephant.Logger.WebApi.Wrappers;

namespace Wex1.Elephant.Logger.WebApi.Helpers
{
    public class PaginationHelper
    {
        public static PagedResponse<IEnumerable<T>> CreatePagedReponse<T>(IEnumerable<T> pagedData, PaginationFilter validFilter, int totalRecords, IUriService uriService, string route)
        {
            var response = new PagedResponse<IEnumerable<T>>(pagedData, validFilter.PageNumber, validFilter.PageSize);

            var totalPages = Convert.ToInt32(Math.Ceiling(((double)totalRecords / (double)validFilter.PageSize)));

            response.NextPage =
                validFilter.PageNumber >= 1 && validFilter.PageNumber < totalPages
                ? uriService.GetPageUri(new PaginationFilter(validFilter.PageNumber + 1, validFilter.PageSize), route)
                : null;

            response.PreviousPage =
                validFilter.PageNumber - 1 >= 1 && validFilter.PageNumber <= totalPages
                ? uriService.GetPageUri(new PaginationFilter(validFilter.PageNumber - 1, validFilter.PageSize), route)
                : null;

            response.FirstPage = uriService.GetPageUri(new PaginationFilter(1, validFilter.PageSize), route);
            response.LastPage = uriService.GetPageUri(new PaginationFilter(totalPages, validFilter.PageSize), route);
            response.TotalPages = totalPages;

            return response;
        }
    }
}
