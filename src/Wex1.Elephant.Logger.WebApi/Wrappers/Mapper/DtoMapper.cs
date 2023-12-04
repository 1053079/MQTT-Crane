using Wex1.Elephant.Logger.Core.Dto.ErrorLogs;
using Wex1.Elephant.Logger.Core.Entities;

namespace Wex1.Elephant.Logger.WebApi.Wrappers.Mapper
{
    public static class DtoMapper
    {
        public static ErrorLogResponseDto MapToDto(this ErrorLog errorLog)
        {
            return new ErrorLogResponseDto
            {
                Id = errorLog.Id.ToString(),
                EventTimeStamp = errorLog.EventTimeStamp,
                EventType = errorLog.EventType,
                component = errorLog.Component,
                Description = errorLog.Description
            };
        }

        public static IEnumerable<ErrorLogResponseDto> MapToDto(this IEnumerable<ErrorLog> errorLogs) 
        {
            return errorLogs.Select(el => el.MapToDto());
        }

    }
}
