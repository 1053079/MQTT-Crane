using Wex1.Elephant.Logger.Core.Filters;

namespace Wex1.Elephant.Logger.Core.Interfaces.Services
{
    public interface IUriService
    {
        Uri GetPageUri(PaginationFilter filter, string route);
    }
}
